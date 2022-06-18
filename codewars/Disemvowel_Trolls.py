def disemvowel(string_):
    vowels = "aeiuoAEIUO"
    for a in vowels:
        for b in string_:
            if a == b:
                string_ = string_.replace(a, "")
    return string_

"""Solution 2

    def disemvowel(s):
        for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
"""

disemvowel("This website is for losers LOL!")
