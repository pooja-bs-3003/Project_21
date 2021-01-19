a,b = input("enter two numbers").split()
a = int(a)
b= int(b)
n = int(input(" enter 1 for addition,2 for subtraction,3 for multiplication,4 for exponential"))
if (n == 1) :
    print("sum of two numbers : ",(a+b))
elif (n == 2) :
    print('difference of two numbers :',(a-b))
elif (n == 3) : 
    print("product of two numbers :",(a*b))
elif (n == 4) :
    print("power of %d to raised to %d is : %d" %(a,b,(a**b)))
else :
    print('enter number within 5')