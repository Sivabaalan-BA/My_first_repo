num1 = int(input())
num2 = int(input())
operator = input()

if operator == "+" :
    result = num1 + num2
    print("result =" , result)

elif operator == "-" :
    result = num1 - num2
    print("result =" , result) 

elif operator == "*" :
    result = num1 * num2
    print("result =" , result)

elif operator == "/" :
    if num2 == 0:
        print("cannot divide by zero")
    else:
        result = num1 / num2
        print("result =" , result)
else:
    print("Invalid operation")

# stage 2 part "result check"

if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")