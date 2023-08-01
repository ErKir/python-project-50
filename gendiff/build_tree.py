def build_state_tree(data1, data2):
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())

    union_keys = list(set.union(keys2, keys1))
    union_keys.sort()

    def build_state(key):
        if key in data1 and key in data2:
            value1 = data1[key]
            value2 = data2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                return {
                    'name': key,
                    'state': 'nested',
                    'children': build_state_tree(value1, value2)
                }
            if value1 == value2:
                return {
                    'name': key,
                    'value': value1,
                    'state': 'unchanged',
                }
            else:
                return {
                    'name': key,
                    'value1': value1,
                    'value2': value2,
                    'state': 'updated',
                }
        elif key in data1 and key not in data2:
            value1 = data1[key]
            return {
                'name': key,
                'value': value1,
                'state': 'removed',
            }
        else:
            value2 = data2[key]
            return {
                'name': key,
                'value': value2,
                'state': 'added',
            }

    diff = list(map(build_state, union_keys))
    return diff
