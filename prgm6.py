str1= input("enter a string :")
l1 =""
for i in str1 [-1:]:
    l1 = i+l1
print(l1)
if str1 == l1:
    print("string is a palindrome")
else :
    print("string is not a palindrome") 