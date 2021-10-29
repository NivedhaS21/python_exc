'''Find the greatest of 3 nos, using variable length argument'''
num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
num3 = int(input("enter number3"))

def maximum(*nos):
    for e in nos:
        if num1 > num2 and num1 > num3:
            largest=num1
        elif num2 > num1 and num2 > num3:
          largest=num2
        else:
            largest=num3
    return largest

print(maximum(num1,num2,num3),"is the largest")
