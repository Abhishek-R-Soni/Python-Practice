# check phone no

import re

def is_valid_phone(phone):
    regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = regex.match(phone)
    if match:
        return True
    return False

print(is_valid_phone("123 456-8588"))
print(is_valid_phone("123 456-8588 ads"))
