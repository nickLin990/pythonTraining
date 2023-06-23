#ask user for name
#ask user for last name
#ask user for annual salary 
#ask user for super rate
#ask user for payment start date
#ask user for payment end date
#print our results
print("Welcome to the payslip generator")
first_name = input("what is your first name? \n")
last_name = input("what is your last name \n")
annual_salary = input("what is your annual salary? \n")
super_rate = input("what is your super rate? \n")
payment_start_date = input("what is your payment start date? \n")
payment_end_date = input("what is your payment end date? \n")

full_name = first_name + " " +  last_name
pay_period = payment_start_date, "-", payment_end_date
gross_income = int(annual_salary) / 12 
income_tax = 
net_income = int(gross_income - income_tax)  