n1= int(input("enter number of elements in list1"))
n2= int(input("enter number of elements in list2"))
A =[]
B =[]
for i in range(0,n1):
    x = int(input("enter elements of list"))
    A.append(x)
for i in range(0,n2):
    y= int(input("enter elements of list"))
    B.append(y)
print(A)
print(B)
s1 = set(A)
s2 = set(B)
print(s1 | s2)
print(s1 & s2)
