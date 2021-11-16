import os

# Giving the root folder
# Change the path to the folders if the its not in the same as project folder
directory = "start"


# Making a recursive loop to iterate over all the folders in the directory
def checkFile(directories, folders, currentPath):
    # Checking for any exceptions
    try:
        # Implementing Breadth first Search
        # Iterating over all the folders in the current directory
        for filename in os.listdir(currentPath):
            # Checking if the file name is in lower case 
            # (it will return falls even if one letter in the name is in upper case)
            if not filename.islower():
                # Appends to the current path folders list
                folders.append(currentPath + "/" + filename)
                # Recursively calls the checkFile method to check sub folders until no folders are found
                checkFile(directories, folders, currentPath + "/" + filename)
            #     Checking if the file is an actual file
            elif os.path.isfile(currentPath + "/" + filename):
                # If true add the file to directories file
                directories.append(filename)
            else:
                # Repeats the process and Continues to check the sub folder from the current path
                checkFile(directories, folders, currentPath + "/" + filename, )
    except FileNotFoundError:
        print("Cannot find the file. Please check the currentPath of the file")
        print("try copying the folders directory tp the same directory as that of .py file")


listOfFiles = []
folders = []
checkFile(listOfFiles, folders, directory)
print("path to the folders with upperCase letters in them")
print(folders)
print()
print("Actual files ")
print(listOfFiles)
