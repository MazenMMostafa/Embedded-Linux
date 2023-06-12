
#isupper()	isnumeric()
while True:
    x=int(input("Choose Function\n1-isupper\n2-isnumberic\n"))
    if x == 1:
        # Example 1
        string1 = "HELLO WORLD"
        print("This one \"HELLO WORLD\" Output -> ",string1.isupper())  # Output: True

        # Example 2
        string2 = "Hello World"
        print("This one \"Hello World\" Output -> ",string2.isupper())  # Output: False
    elif x == 2:
        # Example 1
        string1 = "12345"
        print("This one \"12345\" Output -> ",string1.isnumeric())  # Output: True

        # Example 2
        string2 = "12.3"
        print("This one \"12.3\" Output -> ",string2.isnumeric())  # Output: False
    else :
        print("Error !!")
    y=int(input("Enter\n1-continue\n2-End\n"))
    
        
    if y == 2:
        break