hh=[]
hh0=[]
hh1 = []
hh2 = []
hh3 = []
hh4 = []
hh5 = []
hh6 = []
hh7 = []
hh8 = []
hh9 = []
hh10 = []
def none(n, i=0):
    hh.append([n,i])
    if n == 0:
        hh0.append([n, i])
    elif n == 1:
        hh1.append([n, i])
    elif n == 2:
        hh2.append([n, i])
    elif n == 3:
        hh3.append([n, i])
    elif n == 4:
        hh4.append([n, i])
    elif n == 5:
        hh5.append([n, i])
    elif n == 6:
        hh6.append([n, i])
    elif n == 7:
        hh7.append([n, i])
    elif n == 8:
        hh8.append([n, i])
    elif n == 9:
        hh9.append([n, i])
    elif n == 10:
        hh10.append([n, i])
    return none(n-1, i+1)+none(n-2, i+1) if (n > 1) else 1


print(none(10), '\n', hh0, '\n', hh1, '\n', hh2, '\n', hh3, '\n', hh4, '\n', hh5, '\n', hh6, '\n', hh7, '\n', hh8, '\n', hh9, '\n', hh10)
