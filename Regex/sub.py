"""sub function to replace strings"""


import re
import random


phone = "Please call the phone # +12-123 123-123"

# Remove anything other than digits
# re.sub(pattern, repl, string, maximum=0)
num = re.sub(r"\D", "", phone)
print(f"The raw phone number is : {num}")


def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


line = "Learn Scientific Python with Regex"
m = re.sub(r"(\w)(\w+)(\w)", repl, line)

if m:
    print(f"munged : {m}")
else:
    print("No Match!")
