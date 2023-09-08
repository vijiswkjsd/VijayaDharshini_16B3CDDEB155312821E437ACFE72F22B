def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))
num =int(input("Enter a number to find factorial:"))
print("The factorial of", num, "is", factorial(num))