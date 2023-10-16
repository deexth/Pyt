import string


def to_camel_case(text):
    res = ''
    t1 = ''
    t2 = ''
    for i in text:
        if i not in string.ascii_letters:
            text = text.replace(i, " ")

    for i in text:
        if not i[0].isupper():
            t1 = i[0]
            t2
            res = text.title().replace(" ", '')
            res = res.replace(res[0], t1)
        else:
            res = text.title().replace(" ", '')

    print(res)
    # return res


to_camel_case("The_stealth_warrior")
