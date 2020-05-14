def gcd(a, b):
        while a % b != 0:
            mo, no = a, b
            a, b = no, mo % no
        return b
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den
        if self.den<=0:
            self.num = -1*num
            self.den = -1*den
        self.val = self.num/self.den

    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def __int__(self):
        return int(self.val)
    def __chr__(self):
        return chr(int(self.val))
    def __add__(self,sf):
        tp1 = self.num*sf.den+sf.num*self.den
        tp2 = self.den*sf.den
        return Fraction(tp1//gcd(tp1, tp2), tp2//gcd(tp1, tp2))
    def __sub__(self, sf):
        return self+Fraction(sf.num*-1,sf.den)
    def __mul__(self, sf):
        return Fraction(sf.num*self.num, sf.den*self.den)
    def __truediv__(self, sf):
        return Fraction(sf.den*self.num, sf.num*self.den)
    def __eq__(self, sf):
        tp1=self.num*sf.den
        tp2=sf.num*self.den
        return tp1==tp2

a = Fraction(3,5)
b = Fraction(3,3)
print(a==b,a+b,a-b,a*b,a/b)
