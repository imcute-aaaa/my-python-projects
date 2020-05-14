'''52bit program.
0000000000000000000000000000000000000000000000000000
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
||||||||||||||||||||||||||||||||||||||||||||||||||||
1111222222222222222233333333333333334444444444444444
1:Opcode,   2,Param1,   3,Param2,   4,Param3        
0000=Halt   NA          NA          NA              
0001=Add    Sum         Addend1     Addend2         
0010=Sub    Difference  Minuend     Subtrahend      
0011=Iszero Variable    Condition   NA              
0100=Isneg  Variable    Condition   NA              
0101=Jump   Where       Condition   NA              
0110=Output Where       NA          NA              '''
ram = [
#Length checker
#0000000000000000000000000000000000000000000000000000
'0000000000000000000000000000000000000000000000000000'#Halt
]

def main():
    error='''
    01110  10111  10111  01110  10111
    10001  11000  11000  10001  11000
    11111  10000  10000  10001  10000
    10000  10000  10000  10001  10000
    01111  10000  10000  01110  10000
    '''
    iac=0
    def fetch():
        return str(ram[iac])
    def decode():
        tmp = fetch()
        wght = 1
        rslt1 = 0
        for i in range(4):
            rslt1 += int(tmp[3-i])*wght
            wght *= 2
        wght = 1
        rslt2 = 0
        for i in range(16):
            rslt2 += int(tmp[15-i])*wght
            wght *= 2
        wght = 1
        rslt3 = 0
        for i in range(16):
            rslt3 += int(tmp[15-i])*wght
            wght *= 2
        wght = 1
        rslt4 = 0
        for i in range(16):
            rslt4 += int(tmp[15-i])*wght
            wght *= 2
        return {'op': rslt1, 'p1': rslt2, 'p2': rslt3, 'p3': rslt4, }
    def to(number):
        string = ""
        while number != 0:
            remainder = int(number % 2)
            number = (number - remainder) / 2
            string = str(remainder) + string
        return string
    def execute():
        temp=decode()
        tp=fetch()
        p1 = temp['p1']
        p2 = temp['p2']
        p3 = temp['p3']
        if len(tp) != 52:
            raise Exception('Need to be a string that has a length of 52.')
        elif temp['op'] == 0:
            raise Exception('HALT!!!')
        elif temp['op'] == 1:
            ram[p1] = to(ram[p2] + ram[p3])
        elif temp['op'] == 2:
            ram[p1] = to(ram[p2] - ram[p3])
        elif temp['op'] == 3:
            ram[p1] = '0'*27+str(int(ram[p2] == 0))
        elif temp['op'] == 4:
            ram[p1] = '0'*27+str(int(ram[p2] < 0))
        elif temp['op'] == 5:
            if ram[p1]:
                iac=ram[p2]
        elif temp['op'] == 6:
            print(ram[p1])
        else:
            raise Exception(str(to(temp['op']))+',hence '+str(temp['op'])+',is an invalid opcode.')
    while True:
        try:
            fetch()
            decode()
            execute()
        except IndexError:
            raise Exception(error) 
main()
