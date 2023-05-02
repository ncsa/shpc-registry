#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
import re

# Default template for the new version.lua file
template = '''
-- This is the default template for version.lua files
-- Customize this string as needed for your Lmod modules
{{help_section}}

whatis("Version: {{version}}")

load("apptainer")

local version = "{{version}}"
prepend_path("PATH", "{{bin_directory}}")
'''

def get_cli_args():

    parser = argparse.ArgumentParser(description="Create version.lua files based on module.lua files in a directory tree.")
    parser.add_argument("path",
        help="The path to search for module.lua files.")
    parser.add_argument("dstpath", 
        help="The base path for the new version.lua files.")
    return parser.parse_args()


def extract_help_section(file_path):
    help_section = ""
    with file_path.open("r") as f:
        content = f.read()
        help_regex = r"help\(\s*\[\[(.+?)\]\]\)"
        match = re.search(help_regex, content, re.DOTALL)
        if match:
            help_section = match.group(0)
            help_section = help_section.replace("singularity", "apptainer")
            help_section = help_section.replace("SINGULARITY", "APPTAINER")
    return help_section


def create_version_lua(file_path, dest_base_path, template):
    version = file_path.parent.name
    package = file_path.parent.parent.name
    dest_path = dest_base_path / package / f"{version}.lua"
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    help_section = extract_help_section(file_path)
    bin_directory = str(file_path.parent / "bin")
    content = template.replace("{{version}}", version)
    content = content.replace("{{help_section}}", help_section)
    content = content.replace("{{bin_directory}}", bin_directory)
    
    with dest_path.open("w") as f:
        f.write(content)

def main(args):
    search_path = Path(args.path)
    dest_base_path = Path(args.dstpath)
    
    if not search_path.exists():
        sys.stderr.write(f"Error: Path '{search_path}' does not exist.\n")
        sys.exit(1)

    for file_path in search_path.glob("**/module.lua"):
        create_version_lua(file_path, dest_base_path, template)

if __name__ == "__main__":
    args = get_cli_args()
    main(args)
