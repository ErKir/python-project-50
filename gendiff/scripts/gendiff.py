#!/usr/bin/env python3


from gendiff.build_diff import generate_diff
from gendiff.cli import cli


def main():
    user_data = cli()
    print(generate_diff(
        user_data.first_file,
        user_data.second_file,
        user_data.format)
    )


if __name__ == '__main__':
    main()
