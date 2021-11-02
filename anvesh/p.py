# contactInfo mainatains contact list positional meanings
contactInfo = ['Last Name', 'First Name', 'Salutation', 'Contact Type', 'Title', 'Company Name', 'CompanyAddress',
               'Company URL', 'Address', 'Email', 'Comments']

# define a contact as a dictionary with contact info as the keys
contactDict = {}
# define a contact list as a dictionary of contacts key last name
contactList = {}

# inform the user the app is running and function
print('Contact List Application')
print('Application allows for the creation and use of a contact list')

contactListName = ''

# infinite loop used to keep app running

while True:

    # menu for application
    print('---------------------------------------')
    print('Main Menu')
    print('---------------------------------------')
    print('n or N will Name a Contact List')
    print('a or A will Add a contact')
    print('b or B will Find a Contact via Alphabetical Order')
    print('c or C will Find a Contact via Company')
    print('d or D will Delete a Contact')
    print('f or F will Find a Contact via Last Name')
    print('g or G will allow delete of multiple contacts')
    print('m or M will Modify a Contact')
    print('p or P will Print the Contact List')
    print('s or S will Print the Contact List Status')

    print('Z or z will search the contact list based on last name and gives total count')
    print('q or Q quits')
    print('---------------------------------------')
    print(' ')

    x = input('Enter choice: ')  # capture choice

    # a large if-elif-else structure is used to decode & execute menu choices

    # exit application
    if (x == 'q' or x == 'Q'):
        print('Exit')
        break

    # delete multiple contacts
    elif (x == 'g' or x == 'G'):
        delList = input('Enter the list of contacts to delete (comma sep)').split(',')
        if (delList):
            for con in delList:
                if (contactList.get(con) != None):
                    del contactList[con]
                    print('contact ' + con + ' deleted!')
                else:
                    print('contact ' + con + ' not in contact list')
        else:
            print('zero contacts entered')

    # contacts at a company
    elif (x == 'c' or x == 'C'):
        companyFind = input('Enter Company to find contact at: ')
        companyKeys = []
        # get keys from contact list
        for k in contactList.keys():
            v = contactList[k]
            # v is another dictionary now see if company name is matched
            if v['Company Name'] == companyFind:
                companyKeys.append(k)
        # test for empty keys
        if (companyKeys):
            print('***********')
            print('Contacts Found!')
            print('Number of contacts at ' + companyFind + ' ' + str(len(companyKeys)))
            compDict = {}
            for k in companyKeys:
                print(k)
                compDict[k] = contactList[k]
            print('-----------------------------')

            n = 1
            for k, conComp in compDict.items():
                print('*******')
                print('Contact: ' + str(n))
                n += 1
                for k1, v1 in conComp.items():
                    print(k1 + ' : ' + v1)
            print('***********')
        else:
            print('***********')
            print('Contact for Company ' + companyFind + ' Not Found!')
            print('***********')

    # contact list name
    elif (x == 'n' or x == 'N'):
        contactListName = input('Enter the name of the contact List: ')

    # list number of contacts for a given letter
    elif (x == 'b' or x == 'B'):
        alphaIn = input('Enter a letter to list the number of contacts: ')
        foundKeys = []
        for k in contactList.keys():
            if k[0] == alphaIn:
                foundKeys.append(k)

        print('Contacts found for the letter: ' + alphaIn + ' are: ' + str(len(foundKeys)))

        n = 0
        for k in foundKeys:
            n += 1
            print(str(n) + ': ' + k)

    #  Return the status of the contact list
    elif (x == 's' or x == 'S'):
        print('***********')
        print('Contact List Name: ' + contactListName)
        print('Number of Contacts: ' + str(len(contactList)))
        # when we get to functions we can add more stats like number at a given company....
        print('***********')

    # find a contact based on last name
    elif (x == 'f' or x == 'F'):
        conFind = input('Enter Last Name of the Contact to Find: ')
        if conFind not in contactList.keys():
            for i in contactList.keys():
                if i.startswith(conFind):
                    conFind = i
                    for k, v in contactList[conFind].items():
                        print(k + ' : ' + v)
        elif (contactList.get(conFind) != None):
            print('***********')
            print('Contact Found!')
            for k, v in contactList[conFind].items():
                print(k + ' : ' + v)
            print('***********')
            print('***********')
        else:
            print('***********')
            print('Contact Not Found!')
            print('***********')


    # modify a contact
    elif (x == 'm' or x == 'M'):
        conMod = input('Enter the Last Name of the Contact to Modify: ')
        if (contactList.get(conMod) != None):
            print('***********')
            print('Contact Found!')
            copyLast = ''
            for k, v in contactList[conMod].items():
                print('Current Contact Info: ' + k + ' : ' + v)
                itemMod = input('Modify this item (Y/N): ')
                if (itemMod == 'Y' or itemMod == 'y'):
                    newItem = input('Enter new Contact Information: ')
                    if k == 'Last Name':
                        copyLast = newItem
                    contactList[conMod][k] = newItem
                    print('Contact Information Changed!')
            if copyLast:
                contactList[copyLast] = contactList[conMod].copy()
                del contactList[conMod]

            print('***********')
        else:
            print('***********')
            print('Contact Not Found!')
            print('***********')

    # add a contact
    elif (x == 'a' or x == 'A'):
        contactDict = {}
        for conInfo in contactInfo:
            contactData = input('Enter ' + conInfo + ': ')
            contactDict[conInfo] = contactData
            if (conInfo == 'Last Name'):
                key = contactData
        contactList[key] = contactDict

    # delete a contact
    elif (x == 'd' or x == 'D'):
        conDel = input('Enter Last Name of the contact to delete: ')
        res = contactList.pop(conDel, 'None')
        if (res != 'None'):
            print('**********')
            print('Contact Removed!')
            print('**********')
        else:
            print('**********')
            print('Contact Does Not Exist!')
            print('**********')

    # print a contact list
    elif (x == 'p' or x == 'P'):
        n = 0
        if (not (contactList)):
            print('*************')
            print('The Contact List is Empty!')
            print('*************')
        else:
            print('*************')
            print('Number of Contacts in List: ' + str(len(contactList)))
            print(contactList)
            print('*************')
        for key1, conDict in contactList.items():
            print('*************')
            print('Contact Number: ' + str(n + 1))
            n += 1
            for k2, v in conDict.items():
                print(k2 + ' : ' + v)
            print('*************')
