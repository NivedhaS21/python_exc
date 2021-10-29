''' Create a program to compare three numbers and find the bigger numbers. [topics covered:
identified, variable, types, operator, if stateme nt]'''
num1 = int(input("enter  number1"))
num2 = int(input("enter  number2"))
num3 = int(input("enter  number3"))
if(num1 > num2 and num1 > num3 ):
    print("number1 is greater")
elif (num2 > num3 and num2 > num1) :
    print("number2 is greater")
else:
    print("number 3 is greater")