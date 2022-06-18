def solution(string, ending):
    if string.endswith(ending):
        return True
    else:
        return False

"""Solution 2


def solution(string, ending):
    return ending in string[-len(ending):]
    
"""

"""Soluton 3


def solution(string, ending):
    return ending == string[len(string)-len(ending):]
    
"""

# solution('abcde', 'cde')
# solution('abcde', '')
# solution('abcde', 'abc')
# e = 'abc'
# a = 'abcde'
# print(len(e))
# print(a[-len(e)])