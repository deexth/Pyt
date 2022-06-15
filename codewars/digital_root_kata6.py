# def digital_root(x):
#     if x < 10:
#         return x;
#     x = x%10 + digital_root(x//10)
#     return digital_root(x)
    



def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root



digital_root(942)
