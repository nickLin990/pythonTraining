numberStringInt = input("think of a number\n")
number = int(numberStringInt)
if input("do you want to get the sum or product of 1 to your number\n") == "sum":
    i = 0
    result = 0 
    while i <= number:
        result += i
        i += 1

    print(f"{result}")
else:
    product = 1
    for i in range(1, number + 1):
     product *= i
    print(f"The product of numbers from 1 to {number} is {product}")