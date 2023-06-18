# dulicate Function
def duplicate_num(x):
        _size = len(x)
        repeated = []
        for i in range(_size):
                k = i + 1
                for j in range(k, _size):
                        if x[i] == x[j] and x[i] not in repeated:
                                repeated.append(x[i])
        return repeated

# main Code
list1 = [4, 3, 2, 7, 8, 2, 3, 1]
print (duplicate_num(list1))
