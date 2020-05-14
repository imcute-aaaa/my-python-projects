#Machine language --> Assembly
pairs = {
    '0000': 'Halt',
    '0001': 'Add',
    '0010': 'Sub',
    '0011': 'Ifneg',
    '0100': 'Ifzero',
    '0101': 'Jump',
    '0110': 'Output'}
def to(s):
    rslt = 0
    wght = 1
    for i in range(32):
        rslt += int(s[31-i])*wght
        wght *= 2
    return rslt
def cvt(s):
    try:
        pairs[str(s[:4])]
    except KeyError:
        raise KeyError('invalid opcode: '+s[:4])
    return {'op': pairs[str(s[:4])], 'p1': to(s[4:36]), 'p2': to(s[36:68]), 'p3': to(s[68:])}
a = []
c = input()
while c:
    a.append(cvt(c))
    c=input()
print(a)
