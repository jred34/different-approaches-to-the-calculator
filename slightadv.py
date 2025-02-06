
print("Calculator with def()🧮!")
def dipen(a,b):
    return a+b
def j(a,b):
    return a-b
def red(a,b):
    return a*b
def cj(a,b):
    if b==0:
        return "division by 0 is not divisible🤔"
    return a/b
def grove(a,b):
    if b==0:
        return "division by 0 is not possible🤔"
    return a%b
def street(a,b):
    return a**b

while True:
    operator=input("Choose only out of these operations(+,-,*,/,%,**): ")

    if operator in ("+","-","*","/","%","**"):
        try:
            num1=float(input("enter a valid 1st number🔢: "))
            num2=float(input("enter a valid 2nd number🔢: "))
        except ValueError:
            print("Please only enter a valid number and nothing else!")
            continue

        else:
            if operator == '+':
                print("The sum is: ",dipen(num1,num2))
            elif operator == '-':
                print("The difference is: ",j(num1,num2))

            elif operator =='*':
                print("The product is: ",red(num1,num2))

            elif operator =="/":
                print("The quotient is: ",cj(num1,num2))

            elif operator =='%':
                print("The remainder is: ",grove(num1,num2))
            elif operator =='**':
                print(f"The power of {num1} is ",street(num1,num2))
    else:
        print("Please choose only a valid operation out of these(+,-,*,/,%,**)")
        continue
    again=input("Do you want to use this calculator again(y/n): ").strip().lower()
    if again!='y':
        print("Thank you for using this calculator😁!")
        break



