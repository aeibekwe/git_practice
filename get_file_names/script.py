from os import listdir
from os.path import isfile, isdir

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

# maybe you could make a File Class here that you'll put into the get_file_names function that will limit how deep the function recurses...you could also just add a counter/limiter in the function itself... if you make the class though then you might be able to just input the filename as opposed to the absolute path of the file name...
#class Dir:
#    def __init__(self, dirname=None, dirloc='./'):
#        self.path = dirloc + dirname
#        if isdir(self.path):


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

print('\nContents of {0} (\'cat\' or \'open -e\' latest_output.txt for results):\n\n{1}'.format(path, result))

# Here's a function that writes to a file
# file_name = str, option = str, the_content = str/var(containing str), writestyle = default(write), if the_content is a list, then use 'writelines', or input anything else other than write...
def write_to_file(file_name, option, the_content, write_style='write'):
    a_file = open(file_name, option)
    if write_style == 'write':
        a_file.write(the_content)
    else:
        a_file.writelines(the_content)
    a_file.close()

# This overwrites the contents of latest_output.txt to make space for new content and writes in the header
write_to_file('latest_output.txt', 'w', '\nContents of {0} with absolute path:\n\n'.format(path))

# Here's a function to modify the end of the results
def append_to_result(the_result, append_this):
    contents = []
    for i in the_result:
        i += append_this
        contents.append(i)
    return contents

contents = append_to_result(result, '\n') # This now adds a newline after each list item
write_to_file('latest_output.txt', 'a', contents, 'writelines')
write_to_file('latest_output.txt', 'a', '\nContents of {0} with relative path:\n\n'.format(path))

# This function removes the root/searched directory from each list item, returning relative paths
def remove_inputted_path_from_result(the_results, the_path):
    results_stripped = []
    inputted_path = the_path + '/'
    start_index = len(inputted_path)
    for i in the_results:
        if the_path in i:
            i_stripped = i[start_index:]
            results_stripped.append(i_stripped)
        else:
            print('A problem was encountered in the remove_inputted_path_from_result function...')
    return results_stripped

contents_stripped = remove_inputted_path_from_result(contents, path)
write_to_file('latest_output.txt', 'a', contents_stripped, 'writelines')
write_to_file('latest_output.txt', 'a', '\nNote: Check the other output files for other formats.')

# This is to add a list of items separated by only one space, so that it's easier to copy if need be.
# note: you might want to create a second file for the contents to be copied... that way you can just open that and select all.
contents_cp = append_to_result(result, ' ')
write_to_file('latest_output.ssv', 'w', contents_cp, 'writelines')

# Here is space for additional code to add a csv file, and a list of files minus the inputted directory path
contents_csv = append_to_result(result, ',')
write_to_file('latest_output.csv', 'w', contents_csv, 'writelines')

# This is for a tsv (tab-separated values) file
contents_tsv = append_to_result(result, '\t')
write_to_file('latest_output.tsv', 'w', contents_tsv, 'writelines')

# Extra Step Needed! If filenames have spaces, you need to replace those with '\ ' to escape the space, so the terminal will read it!
def no_spaces(the_results):
    no_spaces_edit = []
    for i in the_results:
        x = i.replace(' ', '\\ ').replace('\'', '\\\'').replace('&', '\\&')
        no_spaces_edit.append(x)
    return no_spaces_edit

# some code to escape the spaces and apostrophe's... hopefully that'll be the last of the formatting stuff... we can clean this up later.
relpath_result = remove_inputted_path_from_result(result, path)
result_with_no_spaces = no_spaces(relpath_result)
result_with_no_spaces_ssv = append_to_result(result_with_no_spaces, ' ')
write_to_file('copy.txt', 'w', result_with_no_spaces_ssv, 'writelines')