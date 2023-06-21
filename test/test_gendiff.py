#!/usr/bin/env python3
import os
from gendiff.scripts.build_diff import generate_diff


def get_fixture_path(file_name):
    return os.path.join('test/fixtures', file_name)


FORMATS = ['stylish', 'plain']


def test_with_json():
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')
    for format in FORMATS:
        result_file_name = f'result_{format}.txt'
        result = open(get_fixture_path(result_file_name))
        expected = result.read()
        actual = generate_diff(filepath1, filepath2, format)
        assert actual == expected


def test_with_yml():
    filepath1 = get_fixture_path('file1.yml')
    filepath2 = get_fixture_path('file2.yaml')
    for format in FORMATS:
        result_file_name = f'result_{format}.txt'
        result = open(get_fixture_path(result_file_name))
        expected = result.read()
        actual = generate_diff(filepath1, filepath2, format)
        assert actual == expected
