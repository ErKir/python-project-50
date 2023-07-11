import argparse


def cli():
    desc = 'Compares two configuration files and shows a difference.'

    parser = argparse.ArgumentParser(
        prog='Gendiff',
        description=desc,
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
    return args
