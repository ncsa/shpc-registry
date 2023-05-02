import argparse
from pathlib import Path
import yaml
import hashlib

def add_entry_to_tags(yml_file, version, sha256_hash, latest):
    with yml_file.open("r") as file:
        data = yaml.safe_load(file)

    if "tags" not in data:
        data["tags"] = {}

    data["tags"][version] = sha256_hash

    if latest:
        data["latest"] = {version: sha256_hash}

    with yml_file.open("w") as file:
        yaml.safe_dump(data, file)

    print(f"Added entry to {yml_file} under tags section for version '{version}' with SHA256 '{sha256_hash}'")
    if latest:
        print(f"Updated 'latest' tag with version '{version}' and SHA256 '{sha256_hash}'")

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with file_path.open("rb") as file:
        while (chunk := file.read(65536)):
            sha256.update(chunk)
    return 'sha256:' + sha256.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Add an entry to a YAML file")
    parser.add_argument("yml_file", type=Path, help="Path to the YAML file")
    parser.add_argument("version", type=str, help="Version string")
    parser.add_argument("target_file", type=Path, help="Path to the target file to compute the SHA256 hash")
    parser.add_argument("--latest", action="store_true", help="Add/replace the latest tag in the YAML file")
    args = parser.parse_args()

    yml_file = args.yml_file
    version = args.version
    target_file = args.target_file
    latest = args.latest

    sha256_hash = calculate_sha256(target_file)
    add_entry_to_tags(yml_file, version, sha256_hash, latest)

if __name__ == "__main__":
    main()
