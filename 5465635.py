hh=[0,1]
def none(n):
    for i in range(n):
        hh.append(hh[i+1]+hh[i])
    #global hh
none(1000)
print(len(tuple(str(hh[-1]))))