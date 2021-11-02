# Defining a main class
class Main:
    # Creating a constructor to initialize the variables
    def __init__(self, teacher, credits, courseName):
        # Defining the variables
        self.teacher = teacher
        self.credts = credits
        self.courseName = courseName

    # Definig a report method to return the data in the class.
    def report(self):
        return "name : " + self.teacher + " Credits : " + str(self.credts) + " Coursename: " + self.courseName

    # Defining a method to update the teacher variable in the class
    def updateTeacherName(self, name):
        self.teacher = name

    # Defining a method to update the credit variable in the  class
    def updateCredits(self, credits):
        self.credts = credits


# Creating a main function
def main():
    # Creating two instants of the class
    teacher1 = Main("Teacher1", 15, "Python for porgrammers")
    teacher2 = Main("Teacher2", 15, "Java for porgrammers")
    # Printing the values of the two instances
    print(teacher1.report())
    print(teacher2.report())
    print("enter the name to update the teacher")
    # Updating the teacher variable in the instacne
    teacher1.updateTeacherName(input())
    # Iterates over the loop until the user enters a valid value.
    while True:
        try:
            # Taking the input from te user
            credit = int(input("enter the credit hours to update\n"))
            # Breaks if the input is valid
            break
        #     Catching the value error exception if the user  enters a invalid value.
        except ValueError:
            print("invalid number please try again")
    teacher1.updateCredits(credit)
    print("Teacher after updating the values")
    # Showing the updated teacher instance
    print(teacher1.report())


# Starting the program only if it run as a program and is not imported.
if __name__ == "__main__":
    main()
