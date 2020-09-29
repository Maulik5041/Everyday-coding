"""RegEx search function"""


import re


line = "Learn to Analyze Data with Scientific Python"

m = re.search(r"(.*) to (.*?) .*", line, re.M | re.I)

if m:
    print(f"m.group() : {m.group()}")
    print(f"m.group(1) : {m.group(1)}")
    print(f"m.group(2) : {m.group(2)}")
else:
    print("No Match!")


# Till this point, it looks similar to match function
# Then why is search important? See below example

email = "hello@leremove_thisarntoanalyzedata.com"

# m = re.match("remove_this", email)
n = re.search("remove_this", email)

if m or n:
    print(f"email address : {email[:n.start()] + email[n.end():]}")
else:
    print("No Match!")


# Line 24 will not work as match function only looks for
# the start of the string.
# Line 25 will work as search functin looks anywhere in
# the string
