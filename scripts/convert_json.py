import json
import os

JSON_PATH = r"c:\Users\Pichau\Desktop\corvo do poço - modulo foundry\scripts\data\content_bundle.json"
JS_PATH = r"c:\Users\Pichau\Desktop\corvo do poço - modulo foundry\scripts\data\content_bundle.js"


def convert():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = f.read()

        # Verify it's valid JSON
        json.loads(data)

        js_content = f"export const contentBundle = {data};"

        with open(JS_PATH, "w", encoding="utf-8") as f:
            f.write(js_content)

        print(f"Successfully converted {JSON_PATH} to {JS_PATH}")
    except Exception as e:
        print(f"Error converting JSON: {e}")


if __name__ == "__main__":
    convert()
