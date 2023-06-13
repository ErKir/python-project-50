#!/usr/bin/env python3

REPLACER = '  '
CHANGES = {
    'unchanged': '  ',
    'deleted': '- ',
    'added': '+ ',
}


OPEN_BRACKET = '{\n'
CLOSE_BRACKET = '}'


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


def to_string(diff, deep=1):
    result = OPEN_BRACKET
    for item in diff:
        state = item['state']
        if state == 'nested':
            name, state, children = item.values()
            result += f'{REPLACER * deep}{name}: '
            result += f'{to_string(children, deep + 1)}\n'
        elif state == 'updated':
            name, value1, value2, state = item.values()
            result += f'{REPLACER * deep}{CHANGES["deleted"]}{name}: '
            result += f'{serialize(value1)}\n'
            result += f'{REPLACER * deep}{CHANGES["added"]}{name}: '
            result += f'{serialize(value2)}\n'
        else:
            name, value1, state = item.values()
            # print('item -->', item)
            # print('value1 -->', value1)
            # print('name -->', name)
            # print('state -->', state)
            result += f'{REPLACER * deep}{CHANGES[state]}{name}: '
            result += f'{serialize(value1)}\n'

    result += f'{REPLACER * deep}{CLOSE_BRACKET}'
    return result
