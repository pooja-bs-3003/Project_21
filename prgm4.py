number = int(input("enter a number"))
n = number
fact =1
while number > 0:
    fact= fact*number
    number = number -1
print("factorial of %d is : %d" %(n,fact))
