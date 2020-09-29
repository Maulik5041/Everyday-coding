"""RegEx lookbehind functions"""


import re


string = "begin:learner1:scientific:learner2:scientific:learner3:end"

# Positive lookbehind
print(re.findall(r"(?<=learner\d:)(\b\w*\b)", string))

# Negative lookbehind
print(re.findall(r"^(?<!learner\d:)(\b\w*\b)", string))
