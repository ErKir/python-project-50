#!/usr/bin/env python3

import argparse
from gendiff.scripts.build_diff import generate_diff

parser = argparse.ArgumentParser(
                    prog='Gendiff',
                    description='Compares two configuration files and shows a difference.',
                    )

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def main():
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
    