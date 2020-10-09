from os import listdir
from os.path import isfile, isdir, abspath

def flatten(alist):
    result = []
    for i in alist:
        if isinstance(i, list):
            flat_list = flatten(i)
            result += flat_list
        else:
            result.append(i)
    return result

def get_file_names(file):
    file_list = listdir(file)
    full_file_list = []
    for i in file_list:
        full = file + '/' + i
        full_file_list.append(full)

    for i in range(len(full_file_list)):
        if isfile(full_file_list[i]):
            continue
        else:
            full_file_list[i] = get_file_names(full_file_list[i])

    flat = flatten(full_file_list)
    
    return flat


path = input('Specify chosen path [format = \'/directory\']: ')
result = get_file_names(path)

print('Contents of {0} (check latest_output.txt for results): {1}\n'.format(path, result))

file_one = open('latest_output.txt', 'w')
file_one.write('Contents of {0}:\n\n'.format(path))
file_one.close()

# This is to add a newline character after each list item
contents = []

for i in result:
    i += ' \n'
    contents.append(i)

file_two = open('latest_output.txt', 'a')
file_two.writelines(contents)
file_two.close()

# This is to add a list of items separated by only one space, so that it's easier to copy if need be.

contents_cp = []

for i in result:
    i += ' '
    contents_cp.append(i)

file_three = open('latest_output.txt', 'a')
file_three.write(
    '\n\nHere is the same list only separated by a single space, to make it easier to copy...\n\n'
)
file_three.writelines(contents_cp)
file_three.close()