# Provided Instructions:
# Complete the solution so that it splits the string 
# into pairs of two characters. If the string contains
# an odd number of characters then it should replace
# the missing second character of the final pair with 
# an underscore ('_').

def solution(s):
    return ["".join(x) for x in zip(s[::2], s[1::2] + "_")]

print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))