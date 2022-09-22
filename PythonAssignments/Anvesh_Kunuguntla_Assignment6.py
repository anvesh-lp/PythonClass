# Defining a class 
class MyNumberList:
    # initializing the constructor
    def __init__(self, values=[]):
        self.__li = []
        # Adding values to the list
        if len(values) != 0:
            for i in values:
                self.__li.append(i)

    # Add function to add to the list
    def add(self, value):
        # Cheking the validity of the inputs
        if isinstance(value, int) or isinstance(value, float):
            self.__li.append(value)
        else:
            print("Input must be either int or float")

    def updateList(self, updatedList):
        # To update the list
        self.__li = updatedList

    def remove(self, value):
        # To remove the elements from the list after storing it in the seperate list
        temp = []
        for i in self.__li:
            if i != value:
                temp.append(i)
        self.__li = temp

    # Method to get the head element of the list
    def head(self):
        return self.__li[0]

    # Get list method to get the value in the list
    def getList(self):
        return list(self.__li)

    # Overring the methods to print the results
    def __str__(self):
        return " ".join(str(v) for v in self.__li)

    def __repr__(self):
        return " ".join(str(v) for v in self.__li)


class myRevOrderedNumberList(MyNumberList):
    def __init__(self, elements):
        MyNumberList.__init__(self, elements)
        # Calling super class function to reverse the list of elements
        self.updateList(sorted((v for v in self.getList()), reverse=True))


def mainfunction():
    lis = []
    # Creating the insatance
    subsample = MyNumberList()
    print("enter the list of elements \n(enter 'Q' to stop) ")
    count = 1
    # While loop ot make user enter the inputs untill he finished
    while True:
        num = input(str(count) + " : ")
        # Checking if the user wants to quit
        if num.lower() == "q":
            break
        #     Try block to catch invalid values
        try:
            if len(num.split(".")) == 2:
                num = float(num)
            else:
                num = int(num)
            subsample.add(num)
            lis.append(num)
            count += 1
        except ValueError:
            print("Inputs must be either floats or integers. Please enter a valid input")

    # Calling the respective class functions

    print(subsample)
    print("Head of the list ", end=" ")
    print(subsample.head())
    while True:
        print("enter an element to remove from the list ", end=" ")
        # Checking the validity of the input
        try:
            n = int(input())
            print(subsample.getList())
            if n in subsample.getList():
                subsample.remove(n)
                break
            else:
                print("element not in the list")
        except ValueError:
            print("** invalid Input try again **")
    print("After removing the element ")
    print(subsample)

    print("--------------------------SubClass operations--------------------------")
    print("Elements before passing to the sub class ")
    print(lis)
    subclass = myRevOrderedNumberList(lis)
    print("elements of the subclass list ")
    print(subclass)
    print("Head of the list ", end=" ")
    print(subclass.head())
    while True:
        print("enter an element to remove from the list ", end=" ")
        # Checking the validity of the input
        try:
            n = int(input())
            print(subclass.getList())
            if n in subclass.getList():
                subclass.remove(n)
                break
            else:
                print("element not in the list")
        except ValueError:
            print("invalid Input, Please try again")
    print("After removing the element ")
    print(subclass)


if __name__ == "__main__":
    mainfunction()
else:
    print("can only be executed as main program")
