a = [1, 2, 3]
for i in a[0::]:
    for j in a[i::]:
        for k in a[j::]:
            print(i, j, k);
