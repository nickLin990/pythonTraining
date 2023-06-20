numberStringInt = input("think of a number\n")
number = int(numberStringInt)
if number % 3 == 0 or number % 5 == 0:
    i = 0
    result = 0 
while i <= number:
    result += i
    i += 1

print(f"{result}")
