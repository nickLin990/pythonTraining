n = int(input("Enter a number: "))  # Ask the user for a number and convert it to an integer

choice = input("Enter 'sum' to compute the sum or 'product' to compute the product: ")  # Ask for the user's choice

if choice == 'sum':
    # Compute the sum of numbers from 1 to n
    sum_of_numbers = sum(range(1, n + 1))
    print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)
elif choice == 'product':
    # Compute the product of numbers from 1 to n
    product_of_numbers = 1
    for i in range(1, n + 1):
        product_of_numbers *= i
    print("The product of numbers from 1 to", n, "is:", product_of_numbers)
else:
    print("Invalid choice! Please enter either 'sum' or 'product'.")
