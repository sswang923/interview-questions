def compare(x,y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    else:
        if str(x) + str(y) == str(y) + str(x):
            return 0
        else:
            return 1
print sorted([1, 2, 3], cmp=compare)
