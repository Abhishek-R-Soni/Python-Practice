# pick random item

from random import choice

name = ["Abhi",
        "Tami",
        "Dhimant"]

ch = choice(name)
print(ch)

if ch in name:
    print(True)

