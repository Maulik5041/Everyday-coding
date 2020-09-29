"""RegEx split function"""


import re


line = "Learn, Scientific, Python"

# re.split(pattern, string, maxsplit=0, flags=0)
m = re.split("\W+", line)

if m:
    print(m)
else:
    print("No Match!")


line2 = "+61Lean4567Scientific23456"

n = re.split('[A-Za-z]+', line2, re.I)

if n:
    print(n)
else:
    print("No Match!")


# split function is very similar to that in normal Python strings
# the difference is, here, we mention what pattern do we want to
# split it around
# Python: string.split() would split all words
# RegEx: re.split(pattern, string)
