#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
                    prog='Gendiff',
                    description='Compares two configuration files and shows a difference.',
                    )

parser.add_argument('first_file')
parser.add_argument('second_file')

args = parser.parse_args()
# print(args.first_file, args.second_file)


def main():
    print('Hello!')


if __name__ == '__main__':
    main()
    