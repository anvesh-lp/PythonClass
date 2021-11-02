# Creating a class pet
class Pet:
    # initializing a constructor
    def __init__(self, name, animal_type, age):
        # Defining attributes
        self.name = name
        self.animal_type = animal_type
        self.age = age

    # Show method to display the values of attributes
    def show(self):
        print("name : {}  animal_type : {}  age : {}".format(self.name, self.animal_type, self.age))


# Creating pet instants
pet1 = Pet("puppy1", "dog", 4)
pet2 = Pet("kitty1", "cat", 1)
pet3 = Pet("puppy2", "dog", 2)
# Calling pet instants show method to display the values and print the information
pet1.show()
pet3.show()
pet2.show()
