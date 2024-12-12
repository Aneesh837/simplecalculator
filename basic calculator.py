print("Welcome to Basic calculator")
while 1:
    a=float(input("Enter First Number: "))
    b=float(input("Enter Second Number: "))
    print("Operations")
    print("1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(x)\n4. Division(/)\n5. Exit")
    ch=int(input("Choose an operation(1,2,3,4,5):"))
    if ch==1:
        print("Addition of",a,'and',b,'is:',a+b)
    elif ch==2:
        print("Subtraction of",a,'and',b,'is:',a-b)
    elif ch==3:
        print(f'Multiplication of {a} and {b} is {a*b}')
    elif ch==4:
        print(f"Division of {a} and {b} is {a/b:.3f}")
    elif ch==5:
        print("The End")
        break
    else:
        print("Please enter right operation")