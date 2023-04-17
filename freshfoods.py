#Name: CARDINALE
#program purpose: To calculate gross and net pay for employees at a grocery store

import datetime

# Define pay rates
CASHIER_PAY_RATE = 16.50
STOCKER_PAY_RATE = 15.75
JANITOR_PAY_RATE = 15.75
MAINTENANCE_PAY_RATE = 19.50

# Define deduction rates
FEDERAL_TAX_RATE = 0.12
STATE_TAX_RATE = 0.03
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145

# Define function to calculate deductions
def calculate_deductions(gross_pay):
    federal_tax = gross_pay * FEDERAL_TAX_RATE
    state_tax = gross_pay * STATE_TAX_RATE
    social_security = gross_pay * SOCIAL_SECURITY_RATE
    medicare = gross_pay * MEDICARE_RATE
    total_deductions = federal_tax + state_tax + social_security + medicare
    return total_deductions

# Define function to calculate net pay
def calculate_net_pay(gross_pay, total_deductions):
    net_pay = gross_pay - total_deductions
    return net_pay


# Start loop to ask for employee data
while True:
    # Ask for employee data
    job_category_code = input("Enter job category code (C, S, J, M): ")
    hours_worked = float(input("Enter number of hours worked: "))

    # Determine pay rate based on job category code
    if job_category_code == "C":
        pay_rate = CASHIER_PAY_RATE
        job_title = "Cashier"
    elif job_category_code == "S":
        pay_rate = STOCKER_PAY_RATE
        job_title = "Stocker"
    elif job_category_code == "J":
        pay_rate = JANITOR_PAY_RATE
        job_title = "Janitor"
    elif job_category_code == "M":
        pay_rate = MAINTENANCE_PAY_RATE
        job_title = "Maintenance"
    else:
        print("Invalid job category code. Please try again.")
        continue

    # Calculate gross pay, deductions, and net pay
    gross_pay = hours_worked * pay_rate
    total_deductions = calculate_deductions(gross_pay)
    net_pay = calculate_net_pay(gross_pay, total_deductions)

    # Print employee pay information
    print("")
    print("Employee Pay Information")
    print("-----------------------")
    print(f"Job Category:   {job_title}")
    print(f"Hours Worked:   {hours_worked:.2f}")
    print(f"Gross Pay:      ${gross_pay:>7.2f}")
    print(f"Federal Tax:    ${gross_pay * FEDERAL_TAX_RATE:>7.2f}")
    print(f"State Tax:      ${gross_pay * STATE_TAX_RATE:>7.2f}")
    print(f"Social Security:${gross_pay * SOCIAL_SECURITY_RATE:>7.2f}")
    print(f"Medicare:       ${gross_pay * MEDICARE_RATE:>7.2f}")
    print(f"Total Deductions:${total_deductions:>7.2f}")
    print(f"Net Pay:        ${net_pay:>7.2f}")
    print("")

    # Ask if user wants to input data for another employee
    another_employee = input("Would you like to input data for another employee? (y/n): ")
    if another_employee.lower() == "y":
        continue
    else:
        break
