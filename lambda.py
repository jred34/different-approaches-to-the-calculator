operations={
    '+': lambda *args:sum(args),
    '-': lambda *args:args[0]-sum(args[1:]),
    '*': lambda *args:(lambda product=args[0]: [product:=product*dip for dip in args][-1])(),
    '/': lambda *args:"❌ Not divisible by 0" if 0 in args[1:] else (lambda quotient=args[0]: [quotient:=quotient/dip for dip in args][1:][-1])(),
    '%': lambda *args:"❌ Not divisible by 0" if 0 in args[1:] else (lambda remainder=args[0]: [remainder:=remainder%dip for dip in args][1:][-1])(),
    '**': lambda *args:(lambda square=args[0]: [square:=square**dip for dip in args][1:][-1])()
}
while True:
    print("🔢lambda-based calculator")

    operation=input("Choose any of the following operations you want to perform(+,-,*,/,%,**): ")
    if operation not in operations:
        print("Not a valid operator❌! Please choose only from the following(+,-,*,/,%,**)")
        continue

    try:
        numbers=list(map(float, input("Enter the numbers you want to enter but separate them with space!: ").split()))

    except ValueError:
        print("Please enter only numbers and nothing else🔢!")
        continue

    print("Final result:",operations[operation](*numbers))

    again=input("Would you like to continue using the calculator again(y/n): ").strip().lower()

    if again!='y':
        print("Understood! Thank you for using this calculator🧮")
        break

