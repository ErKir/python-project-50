#!/usr/bin/env python3

def get_state_tree(file1, file2):
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    union_keys = list(set.union(keys2, keys1))
    union_keys.sort()
    # print('union_keys = ', union_keys)

    def get_state(key):
        if key in file1 and key in file2:
            # print('key-', key)
            # print('key in file1 and key in file2', 'unchanged', 'updated')
            value1 = file1[key]
            value2 = file2[key]
            # print('value1 = ', file1[key])
            if type(value1) is dict and type(value2) is dict:
                return {
                    'name': key,
                    'state': 'nested',
                    'children': get_state_tree(value1, value2)
                }
            if value1 == value2:
                # print('value1 == value2')
                return {
                        'name': key,
                        'value': value1,
                        'state': 'unchanged',
                        }
            else:
                # print('value1 not equal value2')
                return {
                        'name': key,
                        'value1': value1,
                        'value2': value2,
                        'state': 'updated',
                        }
        elif key in file1 and key not in file2:
            value1 = file1[key]
            # print('key in file1 and not key in file2')
            return {
                    'name': key,
                    'value': value1,
                    'state': 'deleted',
                    }
        else:
            # print('added key in file2')
            value2 = file2[key]
            return {
                    'name': key,
                    'value': value2,
                    'state': 'added',
                    }

    diff = list(map(get_state, union_keys))
    return diff
