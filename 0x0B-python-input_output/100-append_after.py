#!/usr/bin/python3
"""
create a function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a lines of text to a file
    after each line containing specific string
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_line_list = []
        while True:
            file_lines = f.readline()
            if file_lines == "":
                break
            file_line_list.append(file_lines)
            if search_string in file_lines:
                file_line_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as fn:
        fn.writelines(file_line_list)
