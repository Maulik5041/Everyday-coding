"""Python greedy and non-greedy functions"""


import re


regex = re.compile(r"(scientific )?programming")
m1 = regex.search('Learn programming')
m2 = regex.search('Learn scientific programming')

print(m1.group())
print(m2.group())
