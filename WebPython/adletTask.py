def eachThird(array):
    a = 0
    for i in range(len(array)):
        if a % 3 == 0:
            print(array[i])
        a = a + 1


eachThird([1, 2, 3, 4, 5, 6, 7, 8])
