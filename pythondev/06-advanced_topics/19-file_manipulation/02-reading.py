'''
Files - Operation Modes:

    1) W - Write
    2) A - Append
    3) R - Read
'''

with open('data/names.txt', 'r', encoding='utf-8') as file:
    print(file.read())

    # we also can read the file like this:

    for line in file:
        print(f'Hello, {line.rstrip()}')

   