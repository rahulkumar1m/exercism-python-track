import re


def is_valid(isbn: str) -> bool:
    isbn_ = re.compile('^([-0-9]+)(X)?$')
    check_match = isbn_.match(isbn)
    if (check_match):
        valid_chars = [int(n) for n in check_match.group(1) if n != '-']
        if check_match.group(2):
            valid_chars.append(10)
        if len(valid_chars) == 10:
            return sum([num * (10-index) for index, num in enumerate(valid_chars)]) % 11 == 0
    return False