def dictmap(d, f):
    for i in d.keys():
        d[i] = f(d[i])