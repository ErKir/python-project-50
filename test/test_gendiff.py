#!/usr/bin/env python3
import os
from gendiff.scripts.build_diff import generate_diff


def get_fixture_path(file_name):
    return os.path.join('test/fixtures', file_name)


result = open(get_fixture_path('result.txt'))
expected = result.read()


def test_with_json():
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')
    actual = generate_diff(filepath1, filepath2)
    assert actual == expected


def test_with_yml():
    filepath1 = get_fixture_path('file1.yml')
    filepath2 = get_fixture_path('file2.yaml')
    actual = generate_diff(filepath1, filepath2)
    assert actual == expected
