def move_zeros(array):
    """
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """
    # print(sorted(lst, key=lambda x: x == 0 and type(x) is not bool))
    # return sorted(lst, key=lambda x: x == 0 and type(x) is not bool)
    nonZeroes = [i for i in array if i != 0]
    zeroesCount = len(array) - len(nonZeroes)
    print(nonZeroes+ [0]*zeroesCount)
    # return lst


# move_zeros([0, 9, 0, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0])
move_zeros([0, 0, 0, 0, 0, 0, 0, 10, 0])
# move_zeros([1, 0, 1, 2, 0, 1, 3])
# move_zeros([1, 1, 2, 1, 3, 0, 0])
