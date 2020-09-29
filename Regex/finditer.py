"""RegEx finditer function"""


import re
import requests


# re.finditer(pattern, string, flags=0)
html = requests.get("https://docs.python.org/2/library/re.html").text
pattern = r"\b(the\s+\w+)\s+"
regex = re.compile(pattern, re.IGNORECASE)
for match in regex.finditer(html):
    print(f"{match.start()}: {match.group(1)}")
