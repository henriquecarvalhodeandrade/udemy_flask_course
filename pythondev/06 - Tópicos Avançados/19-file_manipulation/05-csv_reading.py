with open('data/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        # line = line.rstrip().split(',')
        # print(line)

        language, category = line.rstrip().split(',')
        print(f'{language} - {category}')