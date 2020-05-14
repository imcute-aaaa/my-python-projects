#If you think Machine Language is very complicated,try this!
lt=[
    {'op':'Add','p1':2,'p2':2,'p3':2},
    {'op':'Jump','p1':0,'p2':2,'p3':0},
    1
]
pairs = {
    'Halt': '0000',
    'Add': '0001',
    'Sub': '0010',
    'Ifneg': '0011',
    'Ifzero': '0100',
    'Jump': '0101',
    'Output': '0110'}
def to(number,dig=32):
    string = ""
    # 再次重复这些步骤：
    # 获取余数、减去余数和追加字符串。
    # 记住二进制用另一种方式表示 '2'！
    while number != 0:
        # 我们得到了余数。
        remainder = number % 2
        # 这是我们的迭代方法。这里的 'number' 减掉了余数。
        number = number // 2
        # 将字符串加在余数的后面。
        string = str(remainder) + string
    # 最后，我们要返回我们构建的字符串。
    if len(string) > dig:
        raise Exception('')
    while len(string) < dig:
        string='0'+string
    return string
class line:
    def __init__(self,lmn,nxt):
        try:
            self.op=pairs[lmn['op']]
            self.params=[lmn['p1'],lmn['p2'],lmn['p3']]
        except TypeError:
            self.it=lmn
        self.nxt=nxt
    def convert(self,lst):
        try:
            self.cnvrtd = self.op+to(self.params[0])+to(self.params[1])+to(self.params[2])
        except AttributeError:
            self.cnvrtd = to(self.it,100)
        lst+=self.cnvrtd
        if self.nxt:
            self.nxt.convert(lst)
        else:
            return lst
def cvt(lst):
    tmp=None
    for i in range(len(lst)):
        if type(lst[len(lst)-i-1])=='dict':
            temp = {'op': lst[len(lst)-i-1]['op'], 'p1': lst[len(lst)-i-1]
                ['p1'], 'p2': lst[len(lst)-i-1]['p2'], 'p3': lst[len(lst)-i-1]['p3']}
        else:
            temp = lst[len(lst)-i-1]
        tmp = line(temp, tmp)
    return tmp
rslt=''
cvt(lt).convert(rslt)
print(rslt)
