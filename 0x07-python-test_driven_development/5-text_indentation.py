#!/usr/bin/python3
def text_indentation(text):
    """
    prints a txt with two lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text2= ""
    for c in text:
        text2 = text2 + c
        if c in [".", "?", ":"]:
            text2 = text2 + "\n\n"

    print(text2.rstrip())
