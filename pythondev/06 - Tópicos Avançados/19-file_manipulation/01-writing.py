name = input('Insert the student name:\n')

'''
Files - Operation Modes:

    1) W - Write
    2) A - Append
    3) R - Read
'''

# # using write
# file = open('data/names.txt', 'w')
# file.write(f'{name}\n')
# file.close()

# # using append
# file = open('data/names.txt', 'a', encoding='utf-8')
# file.write(f'{name}\n')
# file.close()

with open('data/names.txt', 'a', encoding='utf-8') as file:
    file.write(f'{name}\n')

