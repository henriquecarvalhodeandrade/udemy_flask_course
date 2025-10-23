'''
Programa Principal
'''
# forma de realizar import de seus módulos

import modulos.math_operations as math_operations

print(math_operations.sum(5, 3))
print(math_operations.subtract(5, 3))
print(math_operations.multiply(0, 3))
print(math_operations.divide(5, 2))

# ou outra forma de importação:

from modulos.math_operations import multiply, divide

print(multiply(0, 3))
print(divide(5, 2))

import modulos.string_utils as string_utils

print(string_utils.capitalize("abcdefgh"))
print(string_utils.reverse_string("abcdefgh"))
print(string_utils.count("abcdefgh"))