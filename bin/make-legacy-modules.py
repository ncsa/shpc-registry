#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path

LMOD_WRAPPER_TEMPLATE = """\
help([[This module is deprected. Use 'module load {module}' instead."]])

io.stderr:write("Warning: The module '{legacy}' is deprecated.\\n")
io.stderr:write("Please start using the new module name: '{module}'.\\n")

load("{module}")
"""

def read_csv_file(file_path):

    with file_path.open() as csvfile:
        reader = csv.DictReader(csvfile)
        module_mapping = [
            {'legacy': row['legacy'], 'module': row['module']}
            for row in reader
        ]
    return module_mapping


def create_lmod_files(output_dir, module_mapping):
    for mapping in module_mapping:
        module_file = output_dir / f"{mapping['legacy']}.lua"
        if mapping['module']: 
            module_file.parent.mkdir(parents=True, exist_ok=True)
            with module_file.open('w') as f:
                f.write(LMOD_WRAPPER_TEMPLATE.format(**mapping))
            print(f"Created Lmod module wrapper for {mapping['legacy']} -> {mapping['module']}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate Lmod module wrappers for deprecated module names."
    )
    parser.add_argument( "csv_file", type=Path, 
        help="CSV file with 'module' and 'legacy' columns."
    )
    parser.add_argument( "output_dir", type=Path,
        help="Directory where the Lmod module wrappers will be generated.",
    )
    return parser.parse_args()

def main(args):
    module_mapping = read_csv_file(args.csv_file)
    create_lmod_files(args.output_dir, module_mapping)

if __name__ == "__main__":
    args = parse_arguments()
    main(args)
