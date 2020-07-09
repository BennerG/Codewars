# Convert string to camel case
#
# Provided Instructions:
# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. The first word within the output 
# should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).

import re

# here's what I believe to be the readable method of solving this problem
def to_camel_case(text):
    # split based on '-' or '_' and return a list of words
    words = re.split(r'-|_', text)
    # initialize an empty string, so we can store the result
    result = ""
    for word in words:
        # if we're not dealing with the first word
        if word != words[0]:
            # captialize the first character and append it to the rest of the word
            word = word[0].upper() + word[1:]
        # concatenate the word to the result string
        result += word
    return result

# here, I throw everything inside of a generator that iterates through the resultant list
def to_camel_case1(text):
    return "".join(w[0].upper() + w[1:] if w != re.split(r'-|_', text)[0] else w for w in re.split(r'-|_', text))

# test
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))