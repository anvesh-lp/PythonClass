# define a class
class Person:

    def __init__(self, name, phone):  # this init sets fields
        self.name = name
        self.phone = phone


# Inheriting the person class
class Employee(Person):

    # initializing the attributes in the employee class
    def __init__(self, name, phone, id, department, jobTitle):
        super(Employee, self).__init__(name, phone)
        self.id = id
        self.department = department
        self.jobtitle = jobTitle


# Creating employee objects
employee1 = Employee("Susan Meyers", 212 - 555 - 1212, 47899, "Accounting", "Vice_President")
employee2 = Employee("Mark Jones", 212 - 555 - 2468
                     , 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 212 - 555 - 9753
                     , 81774, "Operations", "Engineer")


# printing the data of the employee objects
print("{} {} {} {} {}".format(employee1.name, employee1.id, employee1.department, employee1.jobtitle, employee1.phone))
print("{} {} {} {} {}".format(employee2.name, employee2.id, employee2.department, employee2.jobtitle, employee2.phone))
print("{} {} {} {} {}".format(employee3.name, employee3.id, employee3.department, employee3.jobtitle, employee3.phone))
