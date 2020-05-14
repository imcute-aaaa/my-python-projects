'''at=[
    'Add 3 3 3',
    'Output 0 3',
    'Jump 0 3',
    '1'
]'''
def setdp():
    pass#Delete this
def con():
    import re
    global lt
    global inp
    inp=input()
    at=re.split(r'/',inp)
    lt=[]
    for i in at:
        lp = False
        try:
            tp = int(re.split(r' ', i)[0])
        except ValueError:
            lp = True
        if lp:
            lt.append(tuple(re.split(r' ', i)))
        else:
            lt.append(int(re.split(r' ', i)[0]))
def loop(iac):
    if len(lt[iac]) == 4:
        if lt[iac][0] == 'Add':
            lt[int(lt[iac][1])] = (lt[int(lt[iac][2])] + lt[int(lt[iac][3])])
        elif lt[iac][0] == 'And':
            lt[int(lt[iac][1])] = (int(lt[int(lt[iac][2])] and lt[int(lt[iac][3])]))
        elif lt[iac][0] == 'Or':
            lt[int(lt[iac][1])] = (int(lt[int(lt[iac][2])] or lt[int(lt[iac][3])]))
        elif lt[iac][0] == 'Xor':
            lt[int(lt[iac][1])] = (int(int(lt[int(lt[iac][2])]) + int(lt[int(lt[iac][3])]) == 1))
        else:
            raise Exception()
    elif len(lt[iac]) == 3:
        if lt[iac][0] == 'Isneg':
            lt[int(lt[iac][1])]=(lt[int(lt[iac][2])] < 0)
        elif lt[iac][0] == 'Iszero':
            lt[int(lt[iac][1])]=(lt[int(lt[iac][2])] == 0)
        elif lt[iac][0] == 'Jump':
            iac = lt[iac][1] if lt[int(lt[iac][2])] else iac
        elif lt[iac][0] == 'Output':
            print(lt[iac][1]+":"+lt[int(lt[iac][2])])
        elif lt[iac][0] == 'Input':
            lt[int(lt[iac][1])] = datapins[int(lt[iac][2])]
        elif lt[iac][0] == 'Isnot':
            lt[int(lt[iac][1])] = (int(not lt[int(lt[iac][2])]))
        else:
            raise Exception()
    elif len(lt[iac]) == 1:
        if lt[iac][0] == 'Halt':
            raise Exception('HALT!!!')
        elif lt[iac][0][0] == '#':
            print(eval(lt[iac][2:]))
    else:
        raise Exception()
    iac+=1
    return None
def init():
    datapins=[]*(2**32)
    setdp()
    con()
    print(inp)
iac=0
init()
while True:
    loop(iac)
