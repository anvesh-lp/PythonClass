# Taking input from user
distance = int(input("Enter the distance in metres"))
miles=distance*0.000621371
decimalportion=str(miles).split(".")[1]
miles=int(decimalportion)
print("no of miles is "+str(int(miles)))
feet=miles*5280
print(feet)
print("No of feet is "+str(int(feet)))
inches=feet*12
print("no of inches is "+str(int(inches)))



