from pathlib import Path
from textwrap import dedent
import os

def generate_schema_md(schema_version: str, relative_path: str, target_dir: Path):
    with open(target_dir / f"test_submission_schema_{schema_version}.md", "w") as md:
        md.write(dedent(
            f"""
            # Version {schema_version}

            This document describes the schema of the ``test_submission_schema/{schema_version}.json`` 
            files as part of the submission. To get the latest JSON schema file, please visit the 
            Test Submission Schema repository.

            ```{{jsonschema}} {relative_path}
                :lift_definitions:
                :auto_reference:
            """
        ))

def main() -> None:
    source_dir = Path(__file__).parent.parent.parent.parent / "test_submission_schema"
    target_dir = Path(__file__).parent.parent.parent / "reference"
    
    for schema in source_dir.rglob("v*.json"):
        relative_path = os.path.relpath(schema, target_dir)
        generate_schema_md(schema.stem, relative_path, target_dir)


if __name__ == "__main__":
    main()
