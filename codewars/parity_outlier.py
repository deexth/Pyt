def find_outlier(integers):
    odd = []
    even = []
    for i in range(len(integers)):
        if (integers[i] % 2) == 0:
            even.append(integers[i])
        else:
            odd.append(integers[i])
    if len(even) > 1:
        print(odd[0])
    else:
        print(even[0])


find_outlier([2, 4, 6, 8, 10, 3])
