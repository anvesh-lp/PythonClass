#######################################################
#  File     : problem2.py
#  Author   : Uday Kumar Reddy Vudavagandla
#  Date     : January 30, 22
#######################################################

# print headings
print("\n...............Problem 2 ............")
print("========================================")


# taking inputs
ID = int(input("\nPlease enter your ID: "))
rPay = int(input("\nPlease enter pay rate: "))
hours = int(input("\nPlease enter the hours worked: "))
tRate = int(input("\nPlease enter the tax rate %: "))
ehours = int(input("\nPlease enter any extra hours worked(type 0 if got no): ")

# calculations
tax = float(tRate) / 100
extraPay = float(ehours) * (rPay + rPay / 2)
grossPay = float(hours * rPay) + extraPay
taxowed = float(grossPay) * tax
netpay = float(grossPay) - taxowed

# output values
print("\nTotal gross pay is $", grossPay)
print("\nTotal tax owed is $", taxowed)
print("\nTotal net pay is $", netpay)
# end program
