print("EMI Calculator.\n")

#Importing Python library
from prettytable import PrettyTable
import cmath

#Taking inputs
principal = float(input("Enter principal amount: "))
time = float(input("Enter tenure of loan in number of months: "))
cibil = float(input("Enter CIBIL Score: "))

#Considering rate acc to the CiBIL Score
if cibil >= 800:
    rate = 7.5 / (100 * 12)
else:
    rate = 8.3 / (100 * 12)

#EMI calculation
emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)

#Printing EMI
print(f"\nEMI is: Rs {emi}\n")

#Creating table
table = PrettyTable()
table.field_names = ["Month", "EMI", "Principal Amount", "Interest Amount", "Balance Amount"]

#Initializing balance
out_balance = principal

#Calculating EMI, Interest Amount, Balance Amount for each month
for i in range(1, int(time) + 1):
    interest_amt = out_balance * rate
    principal_amt = emi - interest_amt
    out_balance -= principal_amt

    #Appending respective values to the table
    table.add_row([
        i,
        f"Rs {emi}",
        f"Rs {principal_amt}",
        f"Rs {interest_amt}",
        f"Rs {out_balance}"
    ])

#Printing the final schedule
print("EMI Payment Schedule:\n")
print(table)
