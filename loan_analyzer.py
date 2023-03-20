"""Module 1 Challenge - Loan Analyzer"""

import csv
from pathlib import Path

# part 1
print("Part 1 -->")

loan_costs = [500, 600, 200, 1000, 450]

# use `len` function to calculate total number of loans in list
# print number of loans 
print("Number of loans in the list is:", len(loan_costs))

# use `sum` function to calculate total of all loans in list 
# print sum of all loans 
print("Sum of all loans in the list is: $", sum(loan_costs))

# use sum of all loans and total number of loans to calculate average loan price
# print average loan amount
average_loan_amount = (sum(loan_costs)/len(loan_costs))
print("Average loan price is: $", average_loan_amount)

# part 2 
print("Part 2 -->")

loan_data = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# use get() on dictionary to extract Future Value and Remaining Months on loan
# print(future_value)
# print(remaining_months)
future_value = loan_data.get("future_value")
remaining_months = loan_data.get("remaining_months")
print("Future value is: $", future_value)
print("Remaining months are:", remaining_months)

# use formula for Present Value to calculate "fair value" of loan using minimum required return of 20% discount rate
# use **monthly** version of present value formula
# print present value
present_value = future_value / (1 + .20 / 12) **9
print(f"Present value is $", f"{present_value:.2f}")

# wrote conditional statement to decide if present value represents loan's fair value
# if present value of loan is greater than or equal to cost, print message that says the loan is worth at least the cost to buy it
# else, present value of loan is less than loan cost, print message that says that the loan is too expensive 
loan_price = loan_data.get("loan_price")
if present_value >= loan_price:
    print("Good buy! The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")

# part 3
print("Part 3 -->")

# define new function to be used to calculate present value
# function includes parameters `future_value`, `remaining_months`, and the `annual_discount_rate`
# function returns `present_value` for the loan
def calc_pres_val (future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
    "annual_discount_rate": 0.2
}

# define new function to calculate present value of new loan
present_value = calc_pres_val(new_loan["future_value"], new_loan["remaining_months"], new_loan["annual_discount_rate"])

# print present value of new loan
print(f"The present value of the loan is $ {present_value:.2f}")

# part 4 
print("Part 4 -->")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# create empty list called `inexpensive_loans`
inexpensive_loans = []

# loop through all loans and append any that cost $500 or less to `inexpensive_loans` list
for loan in loans:
    loan_price = loan.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan)

# print `inexpensive_loans` list
print("Inexpensive loans:", inexpensive_loans)

# part 5 
print("Part 5 -->")

# set output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# set output file path
output_path = Path("inexpensive_loans.csv")

# output list of inexpensive loans to a csv file
# use `with open` to open new CSV file
# create `csvwriter` using `csv` library
# use new csvwriter to write header variable as first row
# use for loop to iterate through each loan in `inexpensive_loans`
# use csvwriter to write `loan.values()` to row in CSV file
csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
