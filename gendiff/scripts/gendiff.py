#!/usr/bin/env python3

import argparse
from gendiff.scripts.build_diff import generate_diff

DESC = 'Compares two configuration files and shows a difference.'

parser = argparse.ArgumentParser(
                    prog='Gendiff',
                    description=DESC,
                    )

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    default='stylish',
    help='output format (default: stylish)',
    )

args = parser.parse_args()


def main():
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
