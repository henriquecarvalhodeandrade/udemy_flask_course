import glob, os, zipfile

#1 - Current Working Directory
print(os.getcwd())

#2 - List all files of directory
for file in glob.glob('data/*.txt'):
    print(file)

for file in glob.glob('data/*.csv'):
    print(file)

#3 - Compact files
with zipfile.ZipFile('data/names.zip', 'w') as zip:
    for file in glob.glob('data/*.txt'):
        zip.write(file)

#4 - Compacting all files
with zipfile.ZipFile('data/code.zip', 'w') as zip:
    for file in glob.glob('*'):
        zip.write(file)