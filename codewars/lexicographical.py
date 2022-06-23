# def in_array(array1, array2):
#     # arr1 = np.array(array1)
#     # arr2 = np.array(array2)
#     arr3 = []
#     for i in range(len(array1)):
#         for j in range(len(array2)):
#             if array1[i].lower() in array2[j].lower():
#                 arr3.append(array1[i])
#     # res = set(arr3)
        
#     # print(sorted(list(set(arr3))))
#     return sorted(list(set(arr3)))
# def in_array(array1, array2):
#     arr1 = array1
#     arr2 = array2
#     arr3 = []
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             try:
#                 arr2[j].lower().index(arr1[i].lower())
#             except ValueError:
#                 # print("No substrin' found.")
#                 continue
#             else:
#                 arr3.append(array1[i])
                
#     print(sorted(list(set(arr3))))
def in_array(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    print(res)

a1 = ["arp", "ohio", "strong"]
a2 = ["lively", "ohaio", "harp", "sharp", "armstrong"]
in_array(a1, a2)
