while True:
    print("1-Add\n2-Subtract\n3-Multiply\n4-Divide\n5-exit")
    option = int(input("Choose an operation:"))
    if (option in [1,2,3,4]):
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        if (option==1):
            result = num1+num2
        elif (option==2):
            result = num1-num2
        elif (option == 3):
            result = num1 * num2
        elif (option==4):
            result = num1//num2
        else:
            pass
        print("The result of the operation is {}".format(result))
    else:
        print("Invalid operation entered!")
        exit(0)
