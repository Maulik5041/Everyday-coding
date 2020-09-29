"""RegEx match function"""


import re


line = 'Learn to Analyze Data with Scientific Python'
m = re.match(r'(.*) to (.*?) .*', line, re.M | re.I)
n = re.match(r'(\w+) (\w+)', line, re.M | re.I)

if m:
    print(f'm.group(0) : {m.group()}')
    print(f'n.group() : {n.group()}')
    print(f'm.group(1) : {m.group(1)}')
    print(f'm.group(2) : {m.group(2)}')
    print(f'n.group(1, 2) : {n.group(1, 2)}')
else:
    print('No match!')

values = ["Learn", "Live", "Python"]

for value in values:
    # Match the start of a string
    result = re.match("\AL.+", value)
    if result:
        print("START MATCH [L]:", value)

    # Match the end of a string
    result2 = re.match(".+n\Z", value)
    if result2:
        print("END MATCH [n]:", value)
