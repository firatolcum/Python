number = input("Please enter an integer number: ")
power = len(number)
result = 0
if number.startswith("-") or "." in number or "," in number or (not number.isdigit()):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in number:
        result = result + int(i) ** power
    if int(number) == result:
        print(number, " is an Armstrong number")
    else:
        print(number, " is not an Armstrong number")
