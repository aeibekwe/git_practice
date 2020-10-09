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
    print('Contents of {0}: {1}\n'.format(file, flat))
    return flat


path = input('Specify chosen path: ')

get_file_names(path)
