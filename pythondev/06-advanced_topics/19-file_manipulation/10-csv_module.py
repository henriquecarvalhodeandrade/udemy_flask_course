import csv



with open('data/courses.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    courses = list(reader)
    print(courses)