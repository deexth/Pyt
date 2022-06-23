import string


def to_camel_case(text):
    res = ''
    for i in text:
        if i not in string.ascii_letters:
            text = text.replace(i, " ")
            
    if text[0].isupper():
        text = text.title().replace(" ", '')
    else:
        res = text[0]
        text = text.title().replace(" ", '')
        text = text.replace(text[0], res)

    print(text[0].isupper())   
    # return text
    

to_camel_case("the_stealth_warrior")
