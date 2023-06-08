#!/usr/bin/env python3

REPLACER = '  '
CHANGES = {
    'unchanged': '  ',
    'deleted': '- ',
    'added': '+ ',
}


def serialize(v):
    match v:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return v


def to_string(diff):
    result = '{\n'
    for item in diff:
        state = item['state']
        if state == 'updated':
            name, value1, value2, state = item.values()
            result += f'{REPLACER}{CHANGES["deleted"]}{name}: '
            result += f'{serialize(value1)}\n'
            result += f'{REPLACER}{CHANGES["added"]}{name}: '
            result += f'{serialize(value2)}\n'
        else:
            name, value1, state = item.values()
            print('item -->', item)
            print('value1 -->', value1)
            print('name -->', name)
            print('state -->', state)
            result += f'{REPLACER}{CHANGES[state]}{name}: '
            result += f'{serialize(value1)}\n'

    result += '}'
    # print(result)
    print('stylish', result)
    return result
