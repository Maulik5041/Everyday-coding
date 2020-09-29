"""RegEx lookahead functions"""


import re


string = "begin:learner1:scientific:learner2:scientific:learner3:end"

# Positive lookahead
print(re.findall(r"(\w+)(?=:scientific)", string))

# Negative lookahead
print(re.findall(r"(learner\d+)(?!:scientific)", string))
