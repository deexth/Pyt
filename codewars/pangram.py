import string

def is_pangram(s):
    l = []
    for i in s.lower():
        if i in string.ascii_lowercase and i not in l:
            l.append(i)
    
    
    if len(string.ascii_lowercase) == len(l):
        print("Pangram")
    else:
        print("not a Pangram")


pangram = "Cwm fjord bank glyphs vext quiz"
is_pangram(pangram) 
