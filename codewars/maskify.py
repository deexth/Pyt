def maskify(cc):
    f = cc[:-4]
    if len(cc) <= 4:
        return cc
    else:
        for c in f:
            f = f.replace(c, "#")
        cc = f + cc[-4:]
        # return cc
        print(cc)
        
"""solution 2

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
    
    """


maskify("SF$SDfgsd2eA")


