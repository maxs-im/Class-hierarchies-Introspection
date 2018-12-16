class Root:
    gggvp = int()
    def do(self): print("Do Roots")
    def kkdd(self): pass
    #def __init__(self): print("Booobb")

class A(Root):
    atr = str()
    pr = str()
    def get(self): return self.pr
    pr = property(get)
    def do(self): print("Do A")
    def doA(self): print("DoA A")
    @staticmethod
    def doSt(): print("Do static A")
class B(Root):
    def do(self): print("Do B")
class C(A):
    def __init__(self, a = ""): 
        self.a = a
        print("papa") 
    def do(self): print("Do C")
    def doA(self): print("DoA C")
    @staticmethod
    def doSt(): print("Do static C")
class D(B):
    def __init__(self): print("Mda hahah")
    def do(self): print("Do B")
class E(C, D):
    kkdd = int()
    def __init__(self): print("da")
    def do(self): print("Do E")
    def atr(self): print("Atr")
    kek = str()
    #@staticmethod
    #def doSt(): print("Do static E")
class F(D, C):
    def do(self): print("Do F")