numberStringInt = input("think of a number\n")
number = int(numberStringInt)
i = 0
result = 0
while i <= number:
    result += i
    i += 1

print(f"{result}")
