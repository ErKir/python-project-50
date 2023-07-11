from gendiff.parsers import parse
from gendiff.build_tree import build_state_tree
from gendiff.formatters import formatted


def get_extension(file):
    name_parts = file.split('.')
    extension = name_parts[len(name_parts) - 1].lower()
    return extension


def generate_diff(file1_path, file2_path, format='stylish'):
    with open(file1_path) as file1, open(file2_path) as file2:
        parsed_file1 = parse(file1, extension=get_extension(file1_path))
        parsed_file2 = parse(file2, extension=get_extension(file2_path))
        diff = build_state_tree(parsed_file1, parsed_file2)
        result = formatted(diff, format)
        return result
