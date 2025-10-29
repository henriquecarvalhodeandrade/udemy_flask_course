import csv

language = input('Inform a programing language name:\n')
category = input('Inform its category:\n')

with open('data/courses.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([language, category])