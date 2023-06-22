#ask user for name
#ask user for last name
#ask user for annual salary 
#ask user for work start year
#calculate full name
#calculate monthly salary 
#calculate magic year
#print our results
print("welcome to the magic year calculator")
first_name = input("what is your first name? \n")
last_name = input("what is your last name? \n")
annual_salary = input("what is your annual salary? \n")
work_start_year = input("what is your work start year? \n")

full_name = first_name + " " + last_name 
monthly_salary = int(annual_salary) / 12
magic_year = int(work_start_year) + 65

print("your magic age details")
print("Name: " + full_name)
print("Monthly salary: " + str(monthly_salary))
print("magic year: " + str(magic_year))
