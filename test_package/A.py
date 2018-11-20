class A:
    varNum = None

    def __init__(self, num):
        self.varNum = num

    def printA(self):
        print("Hello, A")

    def printAint(self, num):
        print(("In A ", num))

    def printAself(self):
        print(*("In A self var ", self.varNum))

    @staticmethod
    def printAstatic():
        print("Static A")

    @staticmethod
    def printAstaticNum(num):
        print(("Static A with "), num)