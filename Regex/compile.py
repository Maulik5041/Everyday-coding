"""RegEx compile function"""


import re
import os


def main():
    f = open("index.html")
    pattern = re.compile(r"(?P<start><.+?>)(?P<content>.*?)(</.+?>)")
    output_text = []
    for text in f:
        match = pattern.match(text)
        if match is not None:
            output_text.append(match.group('content'))

    fixed_content = ' '.join(output_text)

    print(fixed_content)

    f.close()


if __name__ == "__main__":
    main()
