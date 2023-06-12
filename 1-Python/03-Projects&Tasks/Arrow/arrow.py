import os as cmd
import time
cmd.system("cls")
Size=int(input("Enter Size: "))
Counter=-1
#Size=5
def Rotate(Count):
    cmd.system("cls")
    print('\n' * 4)
    if Count == 0:
        # Look Up
        print('\n'*4)
        for i in range(Size):
            space=11*Size-i
            Star=2*i+1
            print(" "*space + "*"*Star)
        for i in range(Size):
            print(" "*Size*11 + "*")

    elif Count==1:
        # Look Right
        print('\n' * 4)
        for i in range(Size * 2):
            if i < Size:
                Space = Size - i
                Star = i
                print(" " * (Size * 10) + " " * Space + "*" * Star)
            elif i > Size:
                Space = i - Size
                Star = 2 * Size - i
                print(" " * (Size * 10) + " " * Space + "*" * Star)
            elif i == Size:
                Space = i - Size
                Star = i + 6
                print(" " * (Size * 10) + " " * Space + "*" * Star)
    elif Count == 2:
        # Look Down
        print('\n' * 4)
        for i in range(Size):
            print(" " * Size * 11 + "*")
        for i in range(Size,-1,-1):
            space = 11 * Size - i
            Star = 2 * i + 1
            print(" " * space + "*" * Star)


    elif Count ==3:
        # Look Left
        print('\n' * 4)
        for i in range(Size * 2):
            if i < Size:
                Space = Size + 1
                Star = i
                print(" " * (Size * 10) + " " * Space + "*" * Star)
            elif i > Size:
                Space = Size + 1
                Star = 2 * Size - i
                print(" " * (Size * 10) + " " * Space + "*" * Star)
            elif i == Size:
                Space = Size
                Star = i + Size + 1
                print(" " * (Size * 10 - Size) + " " * Space + "*" * Star)


while True:
    z = int(input())
    if z == 1:
        Counter +=1
        if Counter > 3:
            Counter = 0
    elif z==2:
        cmd.system("cls")
        Size=int(input("Enter Size:"))
    elif z == 3:
        break

    cmd.system("cls")
    Rotate(Counter)