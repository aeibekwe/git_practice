from os import listdir
from os.path import isfile, isdir, abspath

# get_file_names will return embedded lists if there is a directory within a directory.  this function will flatten them out.
def flatten(alist):
    result = []
    for i in alist:
        if isinstance(i, list):
            flat_list = flatten(i)
            result += flat_list
        else:
            result.append(i)
    return result

# this function recursively goes through all the contents in a specified directory and checks whether it is a file or directory.  if it encounters a file, it adds it to a list.  if it encounters a directory, it opens that and repeats.  it doesn't stop until all files are retrieved.
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

# this is to add some exception handling on the user input so if you mess up, you don't have to go back and relaunch the script...
path = input('Specify chosen path [format = \'/directory\']: ')
while(isdir(path) != True):
    path = input('\nUh-Oh, that didn\'t work. You might want to double-check your spelling...\n\n\nSpecify chosen path: ')

result = get_file_names(path)

print('\nContents of {0} (\'cat\' or \'open\' latest_output.txt for results):\n\n{1}'.format(path, result))

# This overwrites the contents of latest_output.txt to make space for new content and writes in the header
file_one = open('latest_output.txt', 'w')
file_one.write('Contents of {0}:\n\n'.format(path))
file_one.close()

# This is to add a newline character after each list item
contents = []
for i in result:
    i += ' \n'
    contents.append(i)

file_two = open('latest_output.txt', 'a') #Changed the mode from overWrite to Append
file_two.writelines(contents)

# This is to add a list of items separated by only one space, so that it's easier to copy if need be.
contents_cp = []
for i in result:
    i += ' '
    contents_cp.append(i)

file_two.write('\nHere is the same list only separated by a single space, to make it easier to copy...\n\n')
file_two.writelines(contents_cp)
file_two.close()