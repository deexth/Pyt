# import string

# def to_camel_case(text):
#     # Change code to camel case
#     t1 = text[0]
#     r_text = ''
#     for i in text:
#         if i not in string.ascii_letters:
#             r_text = text.replace(i, ' ')
        
#     r_text = t1 + r_text.title().replace(' ', '')
#     print(r_text.replace(r_text[1], ''))
#     print(t1, text[0])
    

import string


def to_camel_case(text):
    # Change code to camel case
    t1 = text[0]
    r_text = ''
    for i in text:
        if i not in string.ascii_letters:
            r_text = text.replace(i, ' ').split()
    
    print(r_text[0])

to_camel_case("the-stealth-warrior")