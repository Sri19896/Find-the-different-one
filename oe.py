def find_outlier(s):
    e = 0
    o = 0
    p = 0

    for i in s:
        if i % 2 == 0:
            e = e+1
        elif i % 2 != 0:
            o = o+1
    if e > 1:
        for i in s:
            if i % 2 != 0:
                return(i)
    if o > 1:
        for i in s:
            if i % 2 == 0:
                return(i)
