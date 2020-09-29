"""RegEx findall function"""


import re


# re.findall(pattern, string, flags=0)
line = "your alpha@scientificprogramming.io, blah beta@scientificprogramming.io blah user"
# [start with any word, . , - | @ | start with any word, . , -]
emails = re.findall(r"[\w\.-]+@[\w\.-]+", line)

tuples = re.findall(r"([\w\.-]+)@([\w\.-]+)", line)

if emails:
    print(emails)
else:
    print("No Match!")

"""If the pattern includes 2 or more parenthesis groups,
then instead of returning a list of strings, findall()"""
if tuples:
    print(tuples)
else:
    print("No Match!")
