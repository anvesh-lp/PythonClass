
# define a class person
class Person:

    # Creating a constructor for instantiating the fields
    def __init__(self, name, number):
        self.name = name
        self.phoneNumber = number


# Main function
def main():
    p1 = Person("Rakesh", 10000000)
    p2 = Person("Rakesh2", 10000000)
    p3 = Person("Rakesh3", 10000000)

    print(p1.name, "@", p1.phoneNumber, )
    print(p2.name, "@", p2.phoneNumber, )
    print(p3.name, "@", p3.phoneNumber, )
    print()


# technique to start process from main() it wont run if the module is imported
if __name__ == "__main__":
    main()
