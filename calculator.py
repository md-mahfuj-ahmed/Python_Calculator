num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))
op = input("operation (+,-,*,/): ")

if op == "+" :
    print("result", num1 + num2)
elif op == "-" :
    print("result", num1 - num2)
elif op == "*" :
    print("result", num1 * num2)
elif op == "/" :
    print("result", num1 / num2)
else :
    print("invalid operation!")