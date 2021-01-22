class multiplication:
    def __init__(self,m,n):
        self.m = m
        self.n = n
    def display__value(self):
        print("numbers to be multiplied are :",self.m,self.n)
    def product__value(self):
        print("product of two numbers : %d" %(self.m*self.n))
p1= multiplication(15,18)
p1.display__value()
p1.product__value()