def in_array(array1, array2):
    r = []
    l = []
    k = []
    for i in range(len(array2)):
        for j in range(len(array1)):
            if array1[j].lower() in array2[i].lower():
                k.append(array1)
    print(k)
    for i in range(len(k)):
        for j in range(len(k[i])):
            l.append(k[i][j])
    r = set(l)
    
    print(sorted(list(r)))
    # return sorted(list(r))


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1, a2)
