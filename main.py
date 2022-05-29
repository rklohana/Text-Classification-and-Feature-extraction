import os
from bs4 import BeautifulSoup

# Folder Path
num = 0
path = r"C:\Users\yuno gasai\Downloads\course-cotrain-data\course-cotrain-data\fulltext\course"  # input folder path
path1 = r"C:\Users\yuno gasai\Downloads\my_data"  # output folder path
# Change the directory
os.chdir(path)


# parse html files
def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


# Read text File
def read_text_file(file_path, num):
    with open(file_path, 'r') as f:
        s = f.read()
        output = remove_tags(s)
        output_path = path1 + '\\' + str(num) + '.txt'
        print(output_path)
        write_file = open(output_path, 'w',encoding='utf-8')
        write_file.write(output)
        write_file.close()


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    # split_tup = os.path.splitext(file)
    # file_name = split_tup[0]
    # file_extension = split_tup[1]
    # if file.endswith(file_extension):
    file_path = f"{path}\{file}"
    num = num + 1
    # call read text file function
    read_text_file(file_path, num)