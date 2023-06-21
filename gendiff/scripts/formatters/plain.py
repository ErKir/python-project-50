#!/usr/bin/env python3


def stringify(value):
    if value is int:
        return value
    if value is str:
        return f'${value}'
    if value is not dict:
        return f'${value}'
    return '[complex value]'


def plain(item):
    def iter(currentItem, propNames):
        def callback(obj):
            name, value, type = obj.values()
            currentPropName = [*propNames, name]
            match(type):
                case 'added':
                    result = f'Property {".".join(currentPropName)} was {type}'
                    result += f'with value: {stringify(value)}'
                    return result
                case 'deleted':
                    return f'Property {".".join(currentPropName)} was {type}'
                case 'updated':
                    result = f'Property {".".join(currentPropName)} was {type}.'
                    result += f' From {stringify(obj["value1"])}'
                    result += f' to {stringify(obj["value2"])}'
                    return result
                case 'nested':
                    return iter(value, currentPropName)
                case 'unchanged':
                    return ''

        lines = map(callback, currentItem)

        return '\n'.join(list(filter(lambda string: string != '', lines)))

    return iter(item, [])
