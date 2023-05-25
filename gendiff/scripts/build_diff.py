#!/usr/bin/env python3
import json


def generate_diff(file1_path, file2_path, format='plain'):
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    # print('format - ', format)
    # print('file 1\n', file1)
    # print('file 2\n', file2)
    deleted = '  - '
    added = '  + '
    not_changed = '    '
    closed_bracket = '}'
    result = '{\n'

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    union_keys = list(set.union(keys2, keys1))
    union_keys.sort()
    # print('union_keys = ', union_keys)
    for key in union_keys:
        if key in file1 and key in file2:
            # print('key-', key)
            # print('key in file1 and key in file2')
            value1 = str(file1[key])
            value2 = str(file2[key])
            if value1 == value2:
                # print('value1 == value2')
                result += f'{not_changed}{key}: {value1}\n'
            else:
                # print('value1 not equal value2')
                result += f'{deleted}{key}: {value1}\n{added}{key}: {value2}\n'
        elif key in file1 and key not in file2:
            # print('key in file1 and not key in file2')
            value1 = str(file1[key])
            result += f'{deleted}{key}: {value1}\n'
        else:
            # print('added key in file2')
            value2 = str(file2[key])
            result += f'{added}{key}: {value2}\n'
    result += closed_bracket
    print(result)
    return result
