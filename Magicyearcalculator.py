calculate_magic_year 
magic_number = 10
print("Magic Year Calculator")
name = input("what is your name")
Surname = input("what is your surname:")
year_of_birth = int(input("What is your year of birth: "))
annual_salary = input("What is your annaul salary")
work_start_year = input("What is your work start year")
monthly_salary = annual_salary / 12
magic_year = calculate_magic_year(work_start_year)
