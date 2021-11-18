class Person:
    '''
    This is a person class
    '''

    __account = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.__accountNo = Person.__account + 1
        Person.__account += 1

    def printData(self):
        return "name " + self.fname + " last name " + self.lname + " account number " + str(self.getAccount())

    def getAccount(self):
        return self.__accountNo


person1 = Person("anvesh", "Kunuguntla")
person12 = Person("Vamshi", "kunuguntla")
print(person1.printData())
print(person12.printData())
print(Person.__doc__)
