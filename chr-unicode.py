def hlp(a,txt):
    eng = [[65, 90], [97, 122]]
    lat = [192, 691]
    grk = [910, 1117]
    space = [2043, 2207]
    maya = [2304, 4351]
    chi = [11904, 40918]
    h = [44032, 55203]
    al = [0, 55296]
    if txt:
        for i in range(0, 55296):
            a(((str(i) + ' ') + chr(i)), end = '   ')
if __name__='__main__':
    for i in range(0, 55296):
            print(((str(i) + ' ') + chr(i)), end='   ')
