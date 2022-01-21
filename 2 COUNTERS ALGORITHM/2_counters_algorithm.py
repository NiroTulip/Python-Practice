def get_intersection(a, b):
    c = []
    i1=0
    i2=0

    while i1 < len(a) and i2 < len(b):
        if a[i1] == b[i2]:
            c.append(a[i1])
            i1 += 1
            i2 += 1
        else:
            if a[i1] > b[i2]: i2+=1
            else: i1+=1
    return c

a = [0, 1, 1, 2, 5, 7, 10, 11,12]
b = [-1, 1, 1, 3, 7, 9, 12, 13]
print(get_intersection(a, b))

