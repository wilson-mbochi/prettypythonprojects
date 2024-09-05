# This is a calculator program for doing basic math incorporating for loops and if, elif conditional statements
# loop program 5 times
for i in range(0,5):
    print(f"Welcome to my Calculator!",5-i,"more trial uses left!" '\n' "1=Addition 2=Subtraction 3=Multiplication 4=Division")
    MathChoice = int(input("Choose the type of math you want calculate:"))

    if MathChoice == 2:
        print("a - b = difference")
    elif MathChoice == 1:
        print("a + b = sum")
    elif MathChoice == 3:
        print("a x b = Multiplication")
    elif MathChoice == 4:
        print("a ÷ b = Division")
    else:
        print("Not a valid choice. Run program again!")
        quit()

    a = int(input("a="))
    b = int(input("b="))

    if MathChoice == 1:
        print("Your answer is:",(a+b))

    elif MathChoice == 2:
        print("Your answer is:",(a-b))

    elif MathChoice == 3:
        print("Your answer is:",(a*b))

    elif MathChoice == 4:
        print("Your answer is:", (a/b))
print("\nthanks for running the program!")
