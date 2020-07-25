# Provided Instructions:
# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
#
# Examples:
#
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.

# first attempt
def increment_string1(strng):
    if not strng:
        return '1'
    i = len(strng) - 1
    while i >= 0 and strng[i].isnumeric(): i -= 1
    num = int(strng[i + 1:]) + 1 if strng[i + 1:] else 1
    length = len(strng[i + 1:])
    return f"{strng[:i + 1]}{num:0{length}d}"

# better
from re import sub
def increment_string(strng):
    return sub(r'\d*$', lambda m: f'{int(m.group(0) or 0) + 1:0{len(m.group(0))}d}', strng, 1)

print(increment_string(""))
print(increment_string("1"))
print(increment_string("01"))
print(increment_string("foo"))
print(increment_string("foobar099"))
print(increment_string("f09aoo00001"))
print(increment_string("foo01"))