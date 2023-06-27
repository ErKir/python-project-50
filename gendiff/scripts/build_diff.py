#!/usr/bin/env python3

from gendiff.scripts.parsers import parse
from gendiff.scripts.get_state import get_state_tree
from gendiff.scripts.formatters.main import formatted


def build_diff(file1_path, file2_path, format='stylish'):
    file1 = parse(file1_path)
    file2 = parse(file2_path)
    diff = get_state_tree(file1, file2)
    result = formatted(diff, format)
    print(result)
    return result
