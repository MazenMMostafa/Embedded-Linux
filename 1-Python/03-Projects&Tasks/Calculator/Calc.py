
from enum import Enum
class Operation(Enum):
    SUM=1
    SUB=2
    MULT=3
    DIV=4
    POWER=5
    ROOT=6
#Scientific Calculator
def sum(Num1,Num2):
    Result=Num1+Num2
    return Result
def sub(Num1,Num2):
    Result =Num1-Num2
    return Result
def mult(Num1,Num2):
    Result =Num1*Num2
    return Result
def div(Num1,Num2):
    Result =(Num1/Num2)
    return Result
def power(Num1,Pow):
    Result= Num1**Pow
    return Result
def root(Num1,root):
    pow=1/root
    Result= power(Num1,pow)
    return Result
operation = int(input("Enter a Number\n1-sum\n2-sub\n3-mult\n4-div\n5-power\n6-root\n"))
if operation == 1:
    num1=int(input("Number1: "))
    num2=int(input("Number2: "))
    result =sum(num1,num2)
    print(result)
elif operation == 2:
    num1=int(input("Number1: "))
    num2=int(input("Number2: "))
    result=sub(num1, num2)
    print(result)
elif operation == 3:
    num1=int(input("Number1: "))
    num2=int(input("Number2: "))
    result=mult(num1, num2)
elif operation == 4:
    num1=int(input("Number1: "))
    num2=int(input("Number2: "))
    result=div(num1, num2)
    print(result)
elif operation == 5:
    num1=int(input("Num1: "))
    num2=int(input("Power: "))
    result=power(num1, num2)
    print(result)
elif operation == 6:
    num1 = int(input("Number: "))
    num2 = int(input("Root Number: "))
    result=root(num1, num2)
    print(result)

