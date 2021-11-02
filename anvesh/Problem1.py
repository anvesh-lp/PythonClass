temp = int(input("enter the temperature in Fahrenheit\n"))  # Taking input
if temp >= 212:  # Checking condition
    print("water is in Gaseous state")
elif temp <= 32:
    print("Water is in solid state")
else:
    print("water is in liquid state")
