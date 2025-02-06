# simplest claculator

print("🧮 Basic Calculator")
while True:
    try:
        a=float(input("Enter any number of your choice🔢: "))
        b=float(input("Enter any number of your choice🔢: "))
    except ValueError:
        print("👎🏽 Enter only a number!")
        continue


    operator=input("Choose any operation of these(+,-,*,/,%,**): ")
    if operator == "+":
        print("The sum is: ",a+b)
    elif operator == "-":
        print("The difference is: ",a-b)
    elif operator =="*":
        print("The product is: ",a*b)
    elif operator =="/":
        if b==0:
            print("Division by 0 is undefinable!")
        else:
            print("The product is: ",a/b)
    elif operator =="%":
        if b==0:
            print("Division by 0 is not possible!")
        else:
            print("The remainder is: ",a%b)

    elif operator =="**":
        print("The power is: ",a**b)
    else:
        print("Please choose only the valid operations as prompted🤔")

    again=input("Do you want to continue using this calculator🔢🧮(y/n): ").strip().lower()
    if again!='y':
        break
print("Thank you for using this calculator😁!")