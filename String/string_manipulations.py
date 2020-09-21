"""Basic string operations"""


def find_str_char(s):
    """Find index of a char in string"""
    a = s.find('b')
    b = s.find('ccc')
    return [a, b]


if __name__ == '__main__':
    print(find_str_char('aaabbcccc'))
