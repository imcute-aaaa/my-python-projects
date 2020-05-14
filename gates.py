#Gates#
class NAND:
    def __init__(self,inlc1,inlc2):
        self.in1=inlc1.ot
        self.in2=inlc2.ot
        self.ot=not self.in1 and self.in2
        self.t=0
    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = not self.in1 and self.in2
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class NOR:
    def __init__(self, inlc1, inlc2):
        self.in1 = inlc1.ot
        self.in2 = inlc2.ot
        self.ot = not self.in1 or self.in2
        self.t = 0

    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = not self.in1 or self.in2
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class XOR:
    def __init__(self, inlc1, inlc2):
        self.in1 = inlc1.ot
        self.in2 = inlc2.ot
        self.ot = (self.in1 or self.in2)and not(self.in1 and self.in2)
        self.t = 0

    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = (self.in1 or self.in2)and not(self.in1 and self.in2)
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class OR:
    def __init__(self, inlc1, inlc2):
        self.in1 = inlc1.ot
        self.in2 = inlc2.ot
        self.ot = self.in1 or self.in2
        self.t = 0

    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = self.in1 or self.in2
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class AND:
    def __init__(self, inlc1, inlc2):
        self.in1 = inlc1.ot
        self.in2 = inlc2.ot
        self.ot = self.in1 and self.in2
        self.t = 0

    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = self.in1 and self.in2
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class XNOR:
    def __init__(self, inlc1, inlc2):
        self.in1 = inlc1.ot
        self.in2 = inlc2.ot
        self.ot = not((self.in1 or self.in2)and not(self.in1 and self.in2))
        self.t = 0

    def tick(self, inlc1, inlc2):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.in2 = inlc2.ot
            self.ot = not((self.in1 or self.in2)and not(self.in1 and self.in2))
            inlc1.tick()
            inlc2.tick()
            self.t = 0
class NOT:
    def __init__(self, inlc1):
        self.in1 = inlc1.ot
        self.ot = not self.in1
        self.t = 0

    def tick(self,inlc1):
        if self.t == 0:
            self.t = 1
            self.in1 = inlc1.ot
            self.ot = not self.in1
            inlc1.tick()
            self.t = 0
#In/Out puts#
class ipt:
    def __init__(self,val):
        self.ot = val
    def stvl(self,val):
        self.ot = val
class opt:
    def __init__(self,inlc):
        self.val=inlc.ot
    def tick(self, inlc):
        self.val = inlc.ot
        inlc.tick()
#Components#
def comp_half_adder(in1,in2):
    ti1 = ipt(in1)
    ti2 = ipt(in2)
    tg1 = XOR(ti1,ti2)
    tg2 = AND(ti1,ti2)
    to1 = opt(tg1)
    to2 = opt(tg2)
    return [to2.val,to1.val]
def comp_half_suber(in1,in2):
    ti1 = ipt(in1)
    ti2 = ipt(in2)
    tg1 = XOR(ti1, ti2)
    tg2 = AND(ti1, NOT(ti2))
    to1 = opt(tg1)
    to2 = opt(tg2)
    return [to2.val, to1.val]
#Sets#
def compset_full_adder(in1,in2,carry):
    tti1 = ipt(in1)
    tti2 = ipt(in2)
    ttc = ipt(carry)
    tti1plustti2 = ipt(comp_half_adder(tti1,tti2)[1])
    tttempc = ipt(comp_half_adder(tti1,tti2)[0])
    tto1 = opt(comp_half_adder(tti1plustti2,ttc)[1])
    tto2 = opt(OR(tempc, comp_half_adder(tti1plustti2, ttc)[0]))
    return [tto1.val, tto2.val]
def compset_full_suber(in1,in2,carry):
    tti1 = ipt(in1)
    tti2 = ipt(in2)
    ttc = ipt(carry)
    tti1plustti2 = ipt(comp_half_suber(tti1, tti2)[1])
    tttempc = ipt(comp_half_suber(tti1, tti2)[0])
    tto1 = opt(comp_half_suber(tti1plustti2, ttc)[1])
    tto2 = opt(OR(tempc, comp_half_suber(tti1plustti2, ttc)[0]))
    return [tto1.val, tto2.val]
#Sets of sets#

#IC#
