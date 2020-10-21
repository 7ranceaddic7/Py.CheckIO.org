# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

def split_pairs(a):
    list(a)
    print(type(a))
    print(a)
    # if len(a) % 2 == 0:
    #     half = len(a) / 2
    #     print(half)
    # listA = a[:half]
    # listB = a[half:]
    # return listA, listB


# if __name__ == '__main__':
    # print("Example:")
    print(list(split_pairs('abcd')))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(split_pairs('abcd')) == ['ab', 'cd']
    # assert list(split_pairs('abc')) == ['ab', 'c_']
    # assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    # assert list(split_pairs('a')) == ['a_']
    # assert list(split_pairs('')) == []
    # print("Coding complete? Click 'Check' to earn cool rewards!")

# TOGETHER800K
