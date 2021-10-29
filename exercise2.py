'''Write the above solution in a function which takes three numbers and return the bigger number
[topic covered: function]'''
num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
num3 = int(input("enter number3"))

def max(a,b,c):
    if a > b and a > c:
        print(a, 'is greater')
    elif b > a and b > c:
        print(b, 'is greater')
    else:
        print(c, 'is greater');

max(num1,num2,num3);
