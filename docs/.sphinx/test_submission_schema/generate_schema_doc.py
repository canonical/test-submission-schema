from pathlib import Path
from textwrap import dedent
from typing import Any
import os
import json

def get_keys_to_hide(schema: dict[str, Any]) -> str:
    has_hide_keys = False
    hide_keys = []

    if not schema.get("additionalProperties", None):
        hide_keys.append("/**/additionalProperties")
        has_hide_keys = True
    
    return ":hide_key: " + ",".join(hide_keys) if has_hide_keys else ""

def generate_schema_md(schema_path: Path, target_dir: Path):
    relative_path = os.path.relpath(schema_path, target_dir)
    with open(target_dir / f"test_submission_schema_{schema_path.stem}.md", "w") as md:
        with open(schema_path, "r") as schema_file:
            schema: dict = json.load(schema_file)

        try:
            schema_version = schema["properties"]["version"]["const"]
        except KeyError:
            raise ValueError("Schema is missing version property")

        hide_keys = get_keys_to_hide(schema)

        md.write(dedent(
            f"""
            # Version {schema_version}

            This document describes the schema of the `test_submission_schema/{schema_path.name}` 
            files as part of the submission.

            ```{{jsonschema}} {relative_path}
                :lift_definitions:
                :auto_reference:
                {hide_keys}
            """
        ))

def main() -> None:
    source_dir = Path(__file__).parent.parent.parent.parent / "test_submission_schema"
    target_dir = Path(__file__).parent.parent.parent / "reference"
    
    for schema_path in source_dir.rglob("v*.json"):
        generate_schema_md(schema_path, target_dir)


if __name__ == "__main__":
    main()
