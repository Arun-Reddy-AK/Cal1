
class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("Addition of A and B  is :",self.a+self.b)

    def sub(self):
        print("Substraction of A and B is:",self.a-self.b)

    def mul(self):
        print("Multiplication of A and B is:",self.a*self.b)

    def div(self):
        print("Division of A and B is: ",self.a/self.b)

    def modu(self):
        print("Modular division of A and B is: ",self.a%self.b)


obj=Calculator(a=int(input("Enter the value for A")),b=int(input("Enter the value for B")))

obj.add()

obj.sub()

obj.mul()

obj.div()

obj.modu()