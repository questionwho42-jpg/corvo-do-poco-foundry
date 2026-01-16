import os
import re
import json

ROOT_DIR = r"c:\Users\Pichau\Desktop\jogo\mundo"
OUTPUT_FILE = r"c:\Users\Pichau\Desktop\corvo do poço - modulo foundry\scripts\data\content_bundle.json"

bundle = {"actors": [], "journals": []}


def parse_key_value(text):
    data = {}
    lines = text.split("\n")
    current_key = None
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match "- **Key:** Value"
        m = re.match(r"- \*\*(.+?):\*\*\s*(.*)", line)
        if m:
            key = m.group(1).lower()
            val = m.group(2)
            data[key] = val
            current_key = key
        elif current_key and line.startswith("- "):
            # sub-list items, append to current key if it's stats or similar
            if isinstance(data[current_key], list):
                data[current_key].append(line[2:])
            elif isinstance(data[current_key], str):
                # convert to list if multiple items found or just append text?
                # For now, simplistic approach: append text
                data[current_key] += " " + line
        else:
            # Continuation of text
            if current_key and isinstance(data[current_key], str):
                data[current_key] += "\n" + line
    return data


def read_file_safe(filepath):
    encodings = ["utf-8", "cp1252", "latin-1"]
    for enc in encodings:
        try:
            with open(filepath, "r", encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    print(f"ERROR: Could not read {filepath} with supported encodings.")
    return ""


def parse_actors(filepath, category):
    content = read_file_safe(filepath)
    if not content:
        return

    # Split by ### headers
    entries = re.split(r"^###\s+", content, flags=re.MULTILINE)[1:]  # skip preamble

    for entry in entries:
        lines = entry.split("\n")
        header = lines[0].strip()
        body = "\n".join(lines[1:])

        header = re.sub(r"^\d+\.\s*", "", header)
        name = header.split("(")[0].strip()

        metadata = parse_key_value(body)

        actor_type = "npc"

        bio = ""
        for k, v in metadata.items():
            if k not in [
                "prompt",
                "mecânica",
                "estatísticas sociais (pf2e)",
                "influência",
            ]:
                bio += f"<p><strong>{k.title()}:</strong> {v}</p>"

        prompt = None
        for k in metadata:
            if "prompt" in k:
                prompt = metadata[k].replace("`", "").strip()
                break

        actor = {
            "name": name,
            "type": actor_type,
            "folder": category.title(),
            "biography": bio,
            "img_prompt": prompt,
            "system": {},
        }
        bundle["actors"].append(actor)


def parse_journals(filepath, category):
    content = read_file_safe(filepath)
    if not content:
        return

    filename = os.path.basename(filepath)
    name = filename.replace(".md", "").replace("_", " ").replace("-", " ").title()

    html_content = content
    html_content = re.sub(
        r"^##\s+(.+)$", r"<h2>\1</h2>", html_content, flags=re.MULTILINE
    )
    html_content = re.sub(
        r"^###\s+(.+)$", r"<h3>\1</h3>", html_content, flags=re.MULTILINE
    )
    html_content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html_content)
    html_content = html_content.replace("\n", "<br>")

    journal = {"name": name, "folder": category.title(), "content": html_content}
    bundle["journals"].append(journal)


def main():
    # Ensure output dir
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Walk directories
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if not file.endswith(".md") or file.startswith("GUIA"):
                continue

            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, ROOT_DIR)

            if "bestiario" in rel_path or "populacao" in rel_path:
                category = "Bestiario" if "bestiario" in rel_path else "Populacao"
                print(f"Parsing Actor: {rel_path}")
                parse_actors(path, category)
            elif "lore" in rel_path or "missoes" in rel_path:
                category = "Lore" if "lore" in rel_path else "Missoes"
                print(f"Parsing Journal: {rel_path}")
                parse_journals(path, category)

    print(f"Total Actors: {len(bundle['actors'])}")
    print(f"Total Journals: {len(bundle['journals'])}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    print("Bundle created.")


if __name__ == "__main__":
    main()
