# Muhammad Luqman
# G00353385
# Run a few expressions

import regex

tests = [
    ["a.b|b*", "bbbbbb", True],
    ["a.b|b*", "bbx", False],
    ["a.b", "ab", True],
    ["b**","b",True],
    ["b*", "",True]
]
for test in tests:
    assert regex.match(test[0],test[1]) == test[2],test[0] + \
    ("should match " if test[2] else "should not match ")+ test[1]

