num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if(num1 >num2 and num1> num3):
    print("\nMaximum",num1)
elif(num2> num1 and num2 > num3):
    print("\nMaximum",num2)
else:
    print("\nMaximum",num3)


a = int(input("\nEnter first number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))
print("\nMaximum",max(a,b,c))