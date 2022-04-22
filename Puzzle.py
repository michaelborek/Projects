import os
import re

print("HI")
print(os.getcwd())

os.chdir('/Users/misiu/PycharmProjects/pythonProject/Work/extracted_content/')
print(os.listdir())
code = open('Instructions.txt', 'r')
print(code.read())
print('\n')

for folders, sub_folders, files in os.walk('/Users/misiu/PycharmProjects/pythonProject/Work/extracted_content/'):
    print(f'Current looking at: {folders}')
    os.chdir(folders)
    print('\n')
    print('The subfold are: ')
    for sub_folder in sub_folders:
        print(f'\t The subfold is : {sub_folder}')

    print('\n')
    print('The files are: ')
    for file in files:
        print(f'The file is: {file}')
        a = open(file, 'r')
        phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', a.read())
        if phone:
            print(phone.group())
            break
    print('\n')




