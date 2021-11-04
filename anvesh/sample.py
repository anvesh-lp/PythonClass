# variable="python"
# v2=3
# print(variable*3)
# print(variable-v2)
# print(variable+v2)
# print(variable*v2)
# print(300000)
# x = 34 - 23
# y = "hell"
# z = 3.14
# if x == 2 or y == "hello":
#     x += 2
#     z += 2
# else:
#     z%=2
# print(type(z))
# print(z)
# print(x)

# a = ['help', 'copyight', 'credits', 'licence']
# b = a
# b.append("added")
# print(a)
# print(b)
# b = ['help', 'copyight', 'credits', 'licence', 'not-added']
# a = ['help', 'copyight', 'credits', 'licence']
# print(b)
# print(a)

# for i in range(9):
#     print(i)
#     if i == 8:
#         print("end of the loop")
#         break
# else:
#     print("For loop exhausted")
# print("loopis broken due to if statement")

# string="Anvesh"
# string=string[0]
# print("{a}".format(a=string))

# li=(1,2,2,2,1,1,1,2)
# st='anvesh'
# li=tuple(st)
# print(li)

# Definition for singly-linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
#
#
# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         temp = ListNode()
#         self.merger(l1, l2, temp)
#         return temp
#
#     def merger(self, l1, l2, resultlist):
#         if l1 is None:
#             resultlist.next = l2
#         elif l2 is None:
#             resultlist.next = l1
#         if (l1.val < l2.val):
#             temp = ListNode(l1.val)
#             resultlist.next = temp
#             self.merger(l1.next, l2, resultlist.next)
#         else:
#             temp = ListNode(l2.val)
#             resultlist.next = temp
#             self.merger(l1, l2.next, resultlist.next)

# def checkreference(temoList):
#     temoList[0] = "changed"
#
#
# templist = ["unchanged", "unchanged", "unchanged"]
# checkreference(temoList=templist)
# print(templist)
#

# y = "hello this is anvesh"
# x = "hello world"
# # print(y)
# print(y[6:])
# print(y[:-3])
# print(y[-3:-1])
# print(len(y))
# print(type(y))
# print(id(y) == id(x))
# print(id(y))
# print(id(x))
# s = list(y)
# print(s)
# s[6] = "z"
# print(s)
# print(" ".join(s))
# a = 3
# y = "hello"
# if x == 2:
#     print("x is 2")
# elif x == 3 and y == "hello":
#     print("x is 3 and hello")
# else:
#     print("x!=22 and x!=3")
#
# for x in range(0,3):
#     print("hello")
# x=1
# while(x<3):
#     print("three")
#     x+=1
# first = int(input("enter age\n"))
# last = input("enter second name\n")
# print(str(first) + " " + last + " !")


# def checkPrime(num):
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")
#
#
# def findPositivePrimeNumber():
#     pass
#

# s = "hello world"
# for i in range(len(s) + 1):
#     print(s[:i])
# # Using join and list comprehension
# s = "hello world"
# print("\n".join((s[:i] for i in range(len(s) + 1))))  # First it iterates over tge string and joins
# # everything with a
#
# s = "heaven"
# for i in range(-1, len(s)):
#     if i > 0 and "l" in s[:i + 1]:
#         continue
#     else:
#         print(s[:i + 1])


# lis = ['a', 'v', 'anvesh']
# print(len(lis))
# print(lis.index('a'))
# print(str(3)+"anvesh")

# def funfun(x=1, y, z=4):
#     return x+y+z
#
#
# print(funfun(2,y=2))

# def printA(*args):
#     for c, v in enumerate(args):
#         print('{}--{}'.format(c, v), end=" ")
#
#
# def printKwargs(**args):
#     for c, v in args.items():
#         print('{}=={}'.format(c, v), end=" ")
#     print()
#
#
# printKwargs(fruit='apple', fruit2='banana', veg="cabbage")
# printKwargs(fruit1='apple', fruit2='banana', veg1="cabbage", fruit3="pineapple", fruit4="apple")
# printKwargs(a="apple")

# def square(x):
#     return x * x
#
#
# def pr(a, b):
#     return a(b)
#
#
# print(pr(square, 2))


# strings = ["1", "2", "3"]
# for i in strings:
#     print(type(i), end=" ")
# print()
# integers = map(int, strings)
# square = map(lambda x: x * x, integers)
# map(print, square)
# for i in square:
#     print(i
#     , end=" ")

# print(list(filter(lambda x: x > 0, [-1, -2, 0, 1, 2, 3, 4])))

# print(reduce(lambda x, y: x * y, filter(lambda x: x > 0, [-1, -2, 0, 1, 2, 3, 4])))

# print(['anvesh', "fruit", 2, 3])
# lists = ["anvesh", "anvesh1", "anvesh3"]
# # sets={[1,2,3],[12]}
# # print(sets)
# for i in lists:
#     print(i + "" + str(lists.index(i)))
#
# for i in range(0, len(lists)):
#     print("{} {}".format(i, lists[i]))

# sets2 = {1, 1, 1, 1}
# lists2 = set(sets2)
# print(lists2)
# set1 = {1, 2, 3, 4}
# _set2 = {1, 2, 5, 6}
# print(set1 - _set2, _set2 - set1)
# print(set1 | _set2, _set2 & set1, end=print())
# print(set1 ^ _set2)
# l1 = list(_set2)
# l2 = list(set1)
# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# print(len(l1) == len(set(l1) & set(l2)))

# name = "Ganesh"
# name = list(name)
# dicto = {}
# d = {'a': 0, "b": 0, "c": 0, "d": 0}
# print(d.get("k"))
# for i in name:
#     if dicto.get(i) is None:
#         dicto[i] = 1
#     else:
#         dicto[i] = dicto[i] + 1
# print(dicto)


# ages = {1: 4, 2: 2, 3: 2}
# couny = 1
# c = {}
# for i in ages.keys():
#     c[i] = ages[i]
#     c[str(i)+"1"] = math.sqrt(ages[i])
# print(c)


# print(reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, (x for x in range(1, int(input("Enter a value\n")))))))


# d = {"user": 2, "pass": 1234, "new": 2}
# print(d["user"])
# print(d["pass"])
# print(d)
# del d["user"]
# print(d)
# print(d.get("hello"))
# d=["anvesh","123"]
# del d["123"]
# print(d)

# f = open("sam.txt", )
# print(f.readline())
# print(f.readline())
# for i in f.readlines():
#     if 'from' in i:
#         print(i)
#
# strings = [1, 2, 3]

# def rand(num, num2):
#     return num + num2


# ************************************ class 5 (errors and exceptions)*********************************************


# try:
#     x="anvesh"
#     age=23
#     print(x+age)
#     print(age/0)
# except TypeError:
#     print("cannot concat")
# except ZeroDivisionError:
#     print("cannot divide")
# else:
#     print("everything is fine")


# string="anvesh"
# age=23
# try:
#     print(string+age)
#     f=open("")
# except TypeError:
#     print("cannot conanct string and int")
# else:
#     f.close()

# fname = "anvesh"
# print("printing 5 stars", " not 5 stars", sep=" *** ")
# print("printing arrow start", " not 5 stars ", sep=" -> ")
#
#
# name="anvesh"
# age=23
#

#
# iterator = sum([x for x in range(999999999)])
# print(iterator)
# generator = sum((x for x in range(999999999)))
# print(generator)

# print('{:.5}'.format('xylophone'))


# *************************************** generators and iterators **********************


# def generaotr():
#     for i in open("text1.txt").readlines():
#         for k in i.split(" "):
#             yield k
#
#
# g = generaotr()
# try:
#     while True:
#         print(next(g))
# except StopIteration:
#     print("generator completed")
#

# def generatorFib(num):
#     f = 0
#     f1 = 1
#     for i in range(num):
#         fn = f + f1
#         yield fn
#         f = f1
#         f1 = fn
#
#
# fib = generatorFib(4)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# ******************************************* modules and randome *****************************************

# import testModule as t
#
# t.printrandome()
# print(dir(t))

# listofDictionaries = [{"anvesh": ["kunuguntla", 989898999]}, {"surya": ["tej", 9898989]},
#                       {"kavya": ['kay', 4879823798]}]
# for k in listofDictionaries:
#     for key, val in k.items():
#         print("lastName: {} , firstName: {} , PhoneNumber: {}".format(key, val[0], val[1]))

# set1 = {'john', "rob", "pete", "paul", "mary"}
# _set2 = {"ROB", "MARY"}
# # Declaring the empty list
# update = []
# for i in set1:
#     # converting the lowercase to upper case.
#     update.append(i.upper())
# #     converts list into set
# set1 = set(update)
# # intersection of two sets
# print(_set2 & set1)
#
# l1 = [1, 2, 3, 4]
# l2 = [8, 9, 10, 11]
# di = {1: l1, 2: l2}
# print(di[1][0])

# List comprehension
# li = []
# for x in range(0, 10):
#     li.append(x)
# print(li)
#
# print([x for x in range(0, 10)])
# li = [2, 3, 4, 5]
#
#
# def square(x):
#     print(x * x)
#
#


# for args in li:
#     print(args)

# def addtwonumbers(x, y):
#     print(x + y)
#
#
# def addthreeNumber(x, y, z):
#     print(x + y + z)
#
#
# def addNumber(*args):
#     print(sum(args))
#
#
# addNumber(1, 2, 3, 4)
#
#
# def addNumberQwargs(**args):
#     print(args)
#     s = 0
#     for key, value in args.items():
#         s += value
#     print(s)
#
#
# addNumberQwargs(number1=1, number=2, number3=3)
# li = [1, 2, 3, 4, 5]
#
#
# def square(x):
#     print(x * x)
#
#
# for i in li:
#     square(i)
#
# print((map(lambda x: x * x, li)))

# square(2)
# c = lambda x: x * x
# print(c(2))
# s="Rob"
# print(s[-2])
# print()
# set1 = {'john', "rob", "pete", "paul", "mary"}
# set2 = {"ROB", "Mary"}
# # Declaring the empty list
# update = []
# for i in set1:
#     # converting the lowercase to upper case.
#     update.append(i.upper())
# #     converts list into set
# set1 = set(update)
# # intersection of two sets
# print(set2 & set1)
# di={1:2,2:3}
# for k,v in di():
#     print()

# testDict = {'key1': [1, 2, 3], "key2": [10, 11, 12]}
# for k in testDict.keys():
#     t=testDict.get(k)
#     t.append("EXAM")
# print(testDict)
# mylist = ['john', "dave", "rob", "mary","todd"]
# index=mylist.index("rob")
# print("Index of rob")
# print(index)
# print("printing rob from list")
# print(mylist[index])
# mylist.remove("rob")
# print("After deleting the rob from list")
# print(mylist)

# mydict = {}
# for k in range(1, 4):
#     mydict["key " + str(k)] = [x for x in range(0, 5)]
# print(mydict)
# list1 = ["surya", "anvesh", "tej", "ghuna"]
# list2 = ["anvesh", "surya", "hganesh", "putta", "bunny"]
# # Conversting to dict
# li = [list1, list2]
# d = {}
# for i in range(2):
#     d["set" + str(i + 1)] = set(li[i])
# print("printing the dictionary of sets")
# print(d)
# # Extrracting the sets from dictionaries
# print("Two sets from dictionaries")
# set1 = d["set1"]
# set2 = d["set2"]
# print(set1, set2)
# print("interaction of two sets")
# print(set1 & set2)

# myList = [1, 1000.1, 'Pet']
# for i in myList:
#     print(i)
# k=math.pi
# print("{:.15f}".format(k))
#
# myList=[1,1000.1,'Pet']
# for count,ele in enumerate(myList):print(f"element {count} is {ele}")

# ******************************************** os path modules ******** ***************************************


# if platform.system() == "Darwin":
#     print("mac oc here..doesnt works quite well")
# else:
#     print(os.system('ls -l'))

# Get current working directory
# print(os.getcwd())
# Change current
# print(os.chdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/PythonAssignments"))
#
# print(os.listdir(os.getcwd()))

# Creating the directory
# os.mkdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry")
# os.chdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry")
# print("current working direcotry")
# print(os.getcwd())
# # Renaming the directory
# print("---renaming hte directory ---------------")
# print(os.rename("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry","/Users"
#
#                                                                                                     "/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/ChangedDirecotry"))
# print("----------after changing  the name of direcotyr-----------")
# print(os.getcwd())
# # Removing the directory
# os.rmdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/ChangedDirecotry")
# try:
#     print(os.getcwd())
# except FileNotFoundError:
#     print("----------directory not found------------")
#
# os.chdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh/")
#
# print("---------------")
# print(os.getcwdu())

# Absolute path of the file
# print(os.path.abspath("sample.py"))
# print(os.path.exists("sample.py"))
# anvesh="/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/anvesh"
# print()
# if not os.path.exists("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry"):
#     os.mkdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry")
#     for i in range(3):
#         os.mkdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry")
#     print(os.listdir("/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry"))


# Defining the path
# path = "/Users/nagaanveshkunuguntla/Desktop/PythonProjects/SampleProject/CreatedDirecotry"
# # Checking if the path already exists
# if not os.path.exists(path):
#     # Creating the directory
#     os.mkdir(path)
#     for i in range(3):
#         # Creating three sub directories/Files in the directory
#         os.mkdir(path+"/created" + str(i))
#     # Listing the directories under given the path
#     print(os.listdir(path))


# # ****************** problem one ********************
# try:
#     with open("text1.txt") as file1:
#         filesOneLines = file1.read().split("\n")
#     with open("text2.txt") as file2:
#         filesTwoLines = file2.read().split("\n")
# except FileNotFoundError:
#     print("Cant open files")
#
# c = 0
# d = 0
# while d < len(filesTwoLines) and c < len(filesTwoLines):
#     choice = int(input("Enter 1 to read file one and 2 to read line in file 2\n"))
#     print()
#     if choice == 1:
#         if c < len(filesOneLines):
#             print(filesOneLines[c])
#             c += 1
#         else:
#             print("no more line in file 1")
#     else:
#         if d < len(filesTwoLines):
#             print(filesTwoLines[d])
#             d += 1
#         else:
#             print("No more line in file 2")
#
# # **************************** problem 2 **************************


#
#
# try:
#     with open("text1.txt") as file:
#         while True:
#             input()
#             try:
#                 print(file.readline(), end="")
#             except EOFError:
#                 print("No more lines in the file")
#                 break
#
# except FileNotFoundError:
#     print("not found")

# class Person:
#     __account = 0
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         self.__account += 1
#
#     def getAccountNumber(self):
#         return self.__account
#
#     def __repr__(self):
#         return "Account number " + str(self.__account) + "  name : " + self.fname
#
#
# p1 = Person("anvesh", "kun")
# print(p1)
#
# try:
#     with open("sam.txt", 'r') as file:
#         for i in range(0, 99):
#             print(file.readline())
#             # print("\n", line)
#             # time.sleep(2)
# except:
#     print("Can't Open ", file)
#
# import random
#
# print(random.choice([1, 2, 3, 4]))
#


# ********************************************* object oriented programming in python *****************


# *************************
# Name:  Contactlist.py
#
# Description:  This module will be the main module for our contact
# list appication.  We have started this or looked at it several times
# and will continue to do so throughout the term.  This 'refractoring'
# of our code is a normal design evolution.
#
#
# Dependancies: None
#
# Revision History
#
# 9/7/21	RA		Origin
# 9/14/21   RA      List of List demo version
# 9/21/21   RA      More details on List of List Version
# 9/28/21   RA      Dictionary verison created will continue with this...
# 10/9/21   RA 		Added company search option
#
# *************************

# print("anvesh".upper())
# dict = {1: 2, 3: 4}
# l = [1, 23, 2, "a"]
# print(l)
# print(dict.keys())

# Class teacher
# class Teacher:
#     university = "newhaven"
#     count = 0
#     __priclass = 23
#
#     # initializing the attributes
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#         self.__pri = 1
#         self.__increment()
#
#     #     Getter for the variables
#     def getName(self):
#         # returnig the name
#         return self.name
#
#     def getSubject(self):
#         return self.subject
#
#     # Setting the name
#     def setName(self, setna):
#         self.name = setna
#
#     def __increment(self):
#         self.__class__.count += 1
#
#     def getPrivateVariables(self):
#         return str(self.__pri) + " " + str(Teacher.__priclass)
#
#
# sam = Teacher("professor mekni", "python")
# sam2 = Teacher("professor mekni", "Python2")
# # print(Teacher.__priclass)
# print(sam2.getPrivateVariables())

# print(sam.name)
# print(sam.university)
# print(Teacher.count)


# print(sam2.count)


# class Coutnter:
#     t = 0
#
#     def __init__(self):
#         self.mt = 0
#
#     def increment(self):
#         Coutnter.t += 1
#         self.mt += 1
#

#
# a = Coutnter()
# b = Coutnter()
# a.increment()
# b.increment()
# b.increment()
# print(a.mt)
# print(b.mt)
# print(Coutnter.t)
# print(hasattr(Coutnter, "t"))

#  ******************************************************************** https------------
import ssl
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context

req = urlopen("https://www.youtube.com/")
print(req.info().get('Link'))
print(req.info().get('Date'))
print(req.info().get('Content-Type'))
print(req.info().keys())


# print(req.getcode())


