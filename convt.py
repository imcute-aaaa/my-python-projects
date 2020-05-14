pairs={
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
def cvt(n):
    t=list(n)
    c=0
    for i in range(len(t)):
        try:
            if pairs[t[i+1]] <= pairs[t[i]]:
                c += pairs[t[i]]
            else:
                c -= pairs[t[i]]
        except IndexError:
            c += pairs[t[i]]
    return c
print(cvt('IIXVII'))
