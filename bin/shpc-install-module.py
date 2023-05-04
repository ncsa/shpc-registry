#!/usr/bin/env python3

import argparse
from pathlib import Path
import re

LMOD_TEMPLATE = '''\
help([[
{help_statement}
]])

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())

{container_module}

prepend_path("PATH", "{bin_dir}")

'''

def extract_help_statement(src_module_file):

    help_pattern = re.compile(r'help\s*\(\s*\[\[\s*(.*?)\s*\]\]\s*\)', 
            re.DOTALL)

    with open(src_module_file, 'r') as f:
        content = f.read()

    help_match = help_pattern.search(content)

    if help_match:
        return help_match.group(1).strip()
    else:
        return "This module wraps an apptainer container."


def create_lmod_file(src_module_file, dest_module_file, 
        container_option, external_template_file=None):

    src_dir = src_module_file.parent
    help_statement = extract_help_statement(src_module_file)

    if container_option == "apptainer":
        container_module = 'load("apptainer")'
    elif container_option == "singularity":
        container_module = 'load("singularity")'
    else:
        container_module = ""

    if external_template_file and external_template_file.exists() \
            and external_template_file.is_file():
        with open(external_template_file, 'r') as f:
            template = f.read()
    else:
        template = LMOD_TEMPLATE

    lmod_content = template.format(help_statement=help_statement,
            bin_dir=(src_dir / "bin").resolve(), 
            container_module=container_module)

    dest_module_file.parent.mkdir(parents=True, exist_ok=True)

    with open(dest_module_file, 'w') as f:
        f.write(lmod_content)

    print(f"Lmod module file successfully written to {dest_module_file}")

def parse_args():
    parser = argparse.ArgumentParser(description="module file creation")
    parser.add_argument("src_module_file", type=Path, 
            help="Path to an existing module.lua file")
    parser.add_argument("dest_module_file", type=Path, 
            help="Destination path for the new module file")
    parser.add_argument("-t", "--template", type=Path, 
            help="Path to an external template file (optional)", default=None)
    parser.add_argument("-c", "--container", 
            choices=["apptainer", "singularity", "none"], default="apptainer",
            help="Container to load: apptainer (default), singularity, or none")

    return parser.parse_args()

def main(args):

    src_module_file, dest_module_file, external_template_file, container_option = args.src_module_file, args.dest_module_file, args.template, args.container

    if not src_module_file.exists() or not src_module_file.is_file():
        raise ValueError("The src_module_file must exist and be a file")

    create_lmod_file(src_module_file, dest_module_file, container_option, 
            external_template_file)

if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)
