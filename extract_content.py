import os
import re
import json

ROOT_DIR = r"c:\Users\Pichau\Desktop\jogo\mundo"
OUTPUT_FILE = r"c:\Users\Pichau\Desktop\corvo do poço - modulo foundry\scripts\data\content_bundle.json"

bundle = {"actors": [], "journals": []}

# --- PF2e Monster Creation Rules (Simplified - Moderate Values) ---
# Source: GM Core / Monster Creation
PF2E_STATS = {
    -1: {
        "ac": 15,
        "hp": 8,
        "atk": 6,
        "dmg": 2,
        "save_high": 5,
        "save_low": 2,
        "per": 4,
    },
    0: {
        "ac": 16,
        "hp": 15,
        "atk": 7,
        "dmg": 3,
        "save_high": 6,
        "save_low": 3,
        "per": 5,
    },
    1: {
        "ac": 16,
        "hp": 20,
        "atk": 7,
        "dmg": 4,
        "save_high": 7,
        "save_low": 4,
        "per": 6,
    },
    2: {
        "ac": 18,
        "hp": 30,
        "atk": 9,
        "dmg": 6,
        "save_high": 9,
        "save_low": 5,
        "per": 7,
    },
    3: {
        "ac": 19,
        "hp": 45,
        "atk": 11,
        "dmg": 8,
        "save_high": 10,
        "save_low": 6,
        "per": 9,
    },
    4: {
        "ac": 21,
        "hp": 60,
        "atk": 13,
        "dmg": 10,
        "save_high": 12,
        "save_low": 8,
        "per": 11,
    },
    5: {
        "ac": 22,
        "hp": 75,
        "atk": 14,
        "dmg": 12,
        "save_high": 13,
        "save_low": 9,
        "per": 12,
    },
    6: {
        "ac": 24,
        "hp": 95,
        "atk": 16,
        "dmg": 15,
        "save_high": 15,
        "save_low": 11,
        "per": 14,
    },
    7: {
        "ac": 25,
        "hp": 115,
        "atk": 18,
        "dmg": 17,
        "save_high": 16,
        "save_low": 12,
        "per": 15,
    },
    8: {
        "ac": 27,
        "hp": 135,
        "atk": 19,
        "dmg": 20,
        "save_high": 18,
        "save_low": 13,
        "per": 16,
    },
    10: {
        "ac": 30,
        "hp": 175,
        "atk": 23,
        "dmg": 25,
        "save_high": 21,
        "save_low": 16,
        "per": 20,
    },
}

MONSTER_LEVEL_MAP = {}  # name -> level


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


def load_monster_levels():
    """Parses bestiary markdown tables to map monster names to levels."""
    bestiary_dir = os.path.join(ROOT_DIR, "bestiario")
    if not os.path.exists(bestiary_dir):
        return

    for root, _, files in os.walk(bestiary_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
            content = read_file_safe(os.path.join(root, file))

            # Find markdown tables
            # | ... | Inimigo | Nível ... |
            lines = content.split("\n")
            for line in lines:
                if "|" in line and "**" in line:
                    # simplistic parse for | d12 | **Name** | Level |
                    # Try to extract bolded name and valid number
                    parts = line.split("|")
                    if len(parts) < 4:
                        continue

                    name_match = re.search(r"\*\*(.+?)\*\*", line)
                    if not name_match:
                        continue
                    name = name_match.group(1).strip()

                    # Try to find level in other columns
                    level = 0
                    for part in parts:
                        part = part.strip()
                        if part.isdigit() or (
                            part.startswith("-") and part[1:].isdigit()
                        ):
                            level = int(part)
                            break

                    MONSTER_LEVEL_MAP[name] = level
                    # normalize name variations (lowercase)
                    MONSTER_LEVEL_MAP[name.lower()] = level


def generate_pf2e_stats(name, level=0, generated=False):
    """Generates PF2e stats dictionary based on level."""
    stats = PF2E_STATS.get(level, PF2E_STATS[0])

    system = {
        "details": {
            "level": {"value": level},
            "languages": {"value": [], "details": ""},  # Required by V13
            "publication": {
                "title": "Corvo do Poço",
                "authors": "Antigravity",
                "license": "OGL",
                "remaster": True,
            },
            "publicNotes": "",
            "privateNotes": "",
            "blurb": "",  # Required by V13
        },
        "attributes": {
            "hp": {"value": stats["hp"], "max": stats["hp"], "details": ""},
            "ac": {"value": stats["ac"], "details": ""},
            "speed": {
                "value": 25,
                "otherSpeeds": [],
                "details": "",
            },  # 'details' required by NPC schema
            "allSaves": {"value": ""},
        },
        "initiative": {"statistic": "perception"},  # Required by V13
        "abilities": {
            "str": {"mod": 3},  # Defaults to simulate a threat
            "dex": {"mod": 3},
            "con": {"mod": 3},
            "int": {"mod": 0},
            "wis": {"mod": 0},
            "cha": {"mod": 0},
        },
        "perception": {
            "mod": stats["per"],
            "senses": [],
            "vision": True,
            "details": "",
        },
        "saves": {
            "fortitude": {"value": stats["save_high"], "saveDetail": ""},
            "reflex": {"value": stats["save_low"], "saveDetail": ""},
            "will": {"value": stats["save_low"], "saveDetail": ""},
        },
        "traits": {"size": {"value": "med"}, "rarity": "common", "value": []},
    }

    items = []

    # Generic Strike
    if generated:
        items.append(
            {
                "name": "Ataque Básico",
                "type": "melee",
                "img": "icons/weapons/swords/sword-short-iron.webp",
                "system": {
                    "damageRolls": {
                        "0": {
                            "damage": f"1d6 + {stats['dmg']}",
                            "damageType": "bludgeoning",
                        }
                    },
                    "bonus": {"value": stats["atk"]},
                    "traits": {"value": []},
                    "attackEffects": {"value": []},
                    "rules": [],
                },
            }
        )

    return system, items


def parse_social_stats(text):
    """Parses NPC social stats format."""
    stats = {"per": 0, "will": 0, "skills": []}

    # Percepção: +X
    m_per = re.search(r"Percepção:?\s*\+(\d+)", text)
    if m_per:
        stats["per"] = int(m_per.group(1))

    # Vontade: +X
    m_will = re.search(r"Vontade:?\s*\+(\d+)", text)
    if m_will:
        stats["will"] = int(m_will.group(1))

    # Perícias: **Skill** +X, ...
    m_skills = re.search(r"Perícias:?\s*(.+)", text)
    if m_skills:
        skill_line = m_skills.group(1)
        # Parse comma separated "**Name** +X"
        for part in skill_line.split(","):
            s_match = re.search(r"\*\*(.+?)\*\*\s*\+(\d+)", part)
            if s_match:
                stats["skills"].append(
                    {"name": s_match.group(1), "mod": int(s_match.group(2))}
                )
            else:
                # Try unbolded
                s_match2 = re.search(r"([a-zA-Zçã\s]+)\s*\+(\d+)", part)
                if s_match2:
                    stats["skills"].append(
                        {
                            "name": s_match2.group(1).strip(),
                            "mod": int(s_match2.group(2)),
                        }
                    )

    return stats


def parse_full_stat_block_md(text):
    """Parses explicit stat block from markdown blockquotes."""
    # Look for > **CA:** 19; **Fort** +6
    lines = text.split("\n")

    extracted = {
        "ac": None,
        "hp": None,
        "saves": {},
        "attribs": {},
        "skills": [],
        "strikes": [],
    }

    for line in lines:
        line = line.replace(">", "").strip()

        # AC & Saves
        # **CA:** 19; **Fort** +6, **Ref** +10, **Vont** +8
        if "**CA:**" in line or "**AC:**" in line:
            m_ac = re.search(r"\*\*(?:CA|AC):\*\*\s*(\d+)", line)
            if m_ac:
                extracted["ac"] = int(m_ac.group(1))

            for save in ["Fort", "Ref", "Will", "Vont"]:
                m_save = re.search(rf"\*\*{save}\*\*.*?\+(\d+)", line)
                if m_save:
                    if save == "Fort":
                        key = "fortitude"
                    elif save == "Ref":
                        key = "reflex"
                    else:
                        key = "will"
                    extracted["saves"][key] = int(m_save.group(1))

        # HP
        # **PV:** 45; **Fraquezas:** Prata 5
        if "**PV:**" in line or "**HP:**" in line:
            m_hp = re.search(r"\*\*(?:PV|HP):\*\*\s*(\d+)", line)
            if m_hp:
                extracted["hp"] = int(m_hp.group(1))

        # Attributes
        # **Atributos:** For +2, Des +4, Con +2, Int +0, Sab +2, Car +1
        if "**Atributos:**" in line or "**Attributes:**" in line:
            # Simple parse
            mapping = {
                "For": "str",
                "Des": "dex",
                "Con": "con",
                "Int": "int",
                "Sab": "wis",
                "Car": "cha",
            }
            for pt, eng in mapping.items():
                m_attr = re.search(rf"{pt}\s*([+-]\d+)", line)
                if m_attr:
                    extracted["attribs"][eng] = int(m_attr.group(1))

        # Strikes / Attacks
        # **Corpo a corpo** ♦ **Espada Curta** +10 ... **Dano** 1d6+4 perfurante
        if "**Corpo a corpo**" in line or "**Melee**" in line:
            # Clean prefix to avoid matching the type header
            clean_line = (
                line.replace("**Corpo a corpo**", "")
                .replace("**Melee**", "")
                .replace("♦", "")
            )

            # Regex: **Name** (optional text) +Number ... **Dano** Damage
            m_atk = re.search(
                r"\*\*([^\*]+)\*\*[^\+]*\+(\d+).*?\*\*Dano\*\*\s*(.+)", clean_line
            )
            if m_atk:
                name = m_atk.group(1).strip()
                bonus = int(m_atk.group(2))
                dmg_str = m_atk.group(3).strip()
                extracted["strikes"].append(
                    {
                        "name": name,
                        "type": "melee",
                        "system": {
                            "damageRolls": {
                                "0": {
                                    "damage": dmg_str,
                                    "damageType": "untyped",  # Placeholder, ideally parse/prompt user
                                }
                            },
                            "bonus": {"value": bonus},
                            "traits": {"value": []},
                            "attackEffects": {"value": []},
                            "rules": [],
                        },
                    }
                )

    return extracted


def populate_actor_from_extracted(extracted_stats, base_system):
    """Updates base_system with extracted explicit stats."""
    if extracted_stats["ac"]:
        base_system["attributes"]["ac"]["value"] = extracted_stats["ac"]
    if extracted_stats["hp"]:
        base_system["attributes"]["hp"]["value"] = extracted_stats["hp"]
        base_system["attributes"]["hp"]["max"] = extracted_stats["hp"]

    for save, val in extracted_stats["saves"].items():
        base_system["saves"][save]["value"] = val

    for attr, val in extracted_stats["attribs"].items():
        if "abilities" not in base_system:
            base_system["abilities"] = {}
        base_system["abilities"][attr] = {"mod": val}

    items = extracted_stats["strikes"]
    return base_system, items


def parse_actors(filepath, category):
    content = read_file_safe(filepath)
    if not content:
        return

    # Regex for Actors header
    entries = re.split(r"^###\s+", content, flags=re.MULTILINE)[1:]

    for entry in entries:
        lines = entry.split("\n")
        header = lines[0].strip()
        body = "\n".join(lines[1:])

        # Clean Header: "1. Prefeito Thaddeus (Humano, 62 anos)"
        header_clean = re.sub(r"^\d+\.\s*", "", header)
        name = header_clean.split("(")[0].strip()

        # Extract Lore/Bio
        metadata = {}
        lore_html = ""
        prompt = ""

        # Simple extraction
        for line in lines:
            if line.startswith("- **"):
                parts = line.split(":**", 1)
                if len(parts) > 1:
                    key = parts[0].replace("- **", "").lower().strip()
                    val = parts[1].strip()
                    metadata[key] = val
                    if "prompt" in key:
                        prompt = val.replace("`", "")
                    elif key not in [
                        "estatísticas sociais (pf2e)",
                        "influência",
                        "mecânica",
                        "lore",
                    ]:
                        # Capture only non-lore keys as extra info, lore is handled below or via body
                        lore_html += f"<p><strong>{key.title()}:</strong> {val}</p>"
            elif "**Lore:**" in line:  # Fix for "Lore" often being inline
                # - **Lore:** xyz
                pass

        # Additional Bio extraction: just raw text that isn't key-value
        # This is a bit weak but covers most cases

        # Determine if we have social stats or full block
        is_social = "Estatísticas Sociais (PF2e)" in body

        # Try to find level from map if not explicit
        level = MONSTER_LEVEL_MAP.get(
            name, MONSTER_LEVEL_MAP.get(name.lower(), 1)
        )  # Default 1 to avoid 0 weakness

        # Base System (Generated)
        system, items = generate_pf2e_stats(name, level, generated=True)

        # 1. Social Stats Override
        if is_social:
            social = parse_social_stats(body)
            if social["per"]:
                system["perception"]["mod"] = social["per"]
            if social["will"]:
                system["saves"]["will"]["value"] = social["will"]
            # Skills would need item mapping, simpler to put in flags or raw data for now,
            # or just rely on generic stats. Sticking to generic for simplicity unless explicit.

        # 2. Add Lore (Include the raw body or structured lore)
        # For simplicity, we just dump the cleaned up body as bio
        bio_text = re.sub(
            r"- \*\*.+?:\*\* .+\n", "", body
        )  # Remove keys to avoid duplication? No, keep it.
        # Use our extracted KV HTML
        full_bio = lore_html
        if "lore" in metadata:
            full_bio = f"<p><strong>Lore:</strong> {metadata['lore']}</p>" + full_bio

        system["details"]["biography"] = {"value": full_bio, "public": full_bio}

        actor = {
            "name": name,
            "type": "npc",
            "folder": category.title(),
            "img_prompt": prompt,
            "system": system,
            "items": items,
        }
        bundle["actors"].append(actor)


def parse_mission_bosses(filepath, category):
    """Special parser for mission files to find bosses with statblocks."""
    content = read_file_safe(filepath)
    if not content:
        return

    # Check for "Ficha Oficial" or embedded stat block
    if "### 👹 Ficha da Ameaça" in content:
        # Extract Name
        # ## Ameaça Principal: O Rei dos Ratos (Wererat)
        m_name = re.search(r"## Ameaça.*?: (.+?)(?:\(|$)", content)
        name = m_name.group(1).strip() if m_name else "Unknown Boss"

        # Parse logic
        block_text = ""
        capture = False
        for line in content.split("\n"):
            if "> **CA:**" in line or "> **AC:**" in line:
                capture = True
            if capture and line.strip().startswith(">"):
                block_text += line + "\n"

        if block_text:
            extracted = parse_full_stat_block_md(block_text)
            # Level?
            m_lvl = re.search(r"\*\*Nível:\*\*\s*(\d+)", content)
            level = int(m_lvl.group(1)) if m_lvl else 3

            system, items = generate_pf2e_stats(name, level, generated=False)
            system, explicit_items = populate_actor_from_extracted(extracted, system)

            # Add items
            actor = {
                "name": name,
                "type": "npc",
                "folder": "Bosses",
                "img_prompt": "",  # Might be missing here
                "system": system,
                "items": explicit_items,
            }
            bundle["actors"].append(actor)


def parse_journals_simple(filepath, category):
    # Reuse old logic slightly simplified
    content = read_file_safe(filepath)
    if not content:
        return
    filename = os.path.basename(filepath)
    name = filename.replace(".md", "").replace("_", " ").title()
    bundle["journals"].append({"name": name, "folder": category, "content": content})


def main():
    load_monster_levels()

    # 1. Bestiary & Populacao (Actors)
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            path = os.path.join(root, file)
            if "bestiario" in root and file.endswith(".md"):
                parse_actors(path, "Bestiario")
            elif "populacao" in root and file.endswith(".md"):
                parse_actors(path, "Populacao")
            elif "missoes" in root and file.endswith(".md"):
                # Check for bosses
                parse_mission_bosses(path, "Missoes")

            # Lore Journals
            elif "lore" in root and file.endswith(".md"):
                parse_journals_simple(path, "Lore")

    # Output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    print(
        f"Extracted {len(bundle['actors'])} actors and {len(bundle['journals'])} journals."
    )


if __name__ == "__main__":
    main()
