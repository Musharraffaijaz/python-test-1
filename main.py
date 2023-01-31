# age = 21;
#
# print(age);
# print("I am " + str(age) + " years old")
# print("I am", age,  "years old")
# print(f"I    am {age} years old")

# name = 'Musharaf'
# age = 21
# gpa = 9.5
# student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))


#now lets change or typecast the dataTypes
# gpa = int(gpa)
# age = float(age)
# print(type(age)) changed to a floating point from integer
# print(type(gpa)) changed to a integer from floating point

#Learning Input Tags in Python

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Your name is {name}")
# print(f"Your age  is {age}")

#Lets make a fun game

# adjective1 = input("Enter the first adjective: ")
# noun = input("Enter a noun: ")
# adjective2 = input("Enter the second adjective: ")
# verb1 = input("Enter the first verb: ")
# verb2 = input("Enter the second verb: ")
#
# print(f"Today I went to a {adjective1} mental asylum") #huge
# print(f"there I saw {noun}") #Farooq Abdullah
# print(f"He was {adjective2} and {verb1}ing")#bezerk and barking
# print(f"everyone saw him and {verb2} him!")#murdered

#Some Mathematics

import math
# print(math.pi)
# print(math.e)

#calculate the circumfrence

# radius = float(input("Enter a value of radius: "))
# circumfrence = 2 * math.pi * radius
# print("The circumfrence is: {round(circumfrence, 2)}")

#calculate the area
# length = float(input("Enter Length: "))
# breadth = float(input("Enter Breadth: "))
# area = length*breadth
# print(f"Calculated area is {area} cm^2")
#calculate the volume
# length = float(input("Enter Length: "))
# breadth = float(input("Enter Breadth: "))
# height = float(input("Enter Height: "))
# volume = length*breadth*height
# print(f"Calculated volume is {volume} cm^3")

#calculate the hypotneous
# base = float(input("Enter a base value: "))
# perpendicular = float(input("Enter a perpendicular value: "))
# hypotneous = math.sqrt(pow(base, 2) + pow(perpendicular, 2))
# print(hypotneous)

#if else statement
# age = int(input("Enter your age: "))
# if(age >= 100):
#     print("You are too old to cast a vote!")
# elif (age >= 18):
#     print("you are now eligible to vote!")
# elif(age < 0):
#     print("Enter a valid age")
# else:
#     print("You need to be at least 18 years old to cast a vote!")

#calculator program
# operator = input("Enter an operand: ")
# num1 = float(input("Enter first Number: "))
# num2 = float(input("Enter second Number: "))
#
# if (operator == "+" ):
#     result = num1 + num2
#     print(result)
# elif (operator == "-" ):
#     result = num1 - num2
#     print(result)

#Validate any name using python

# username = input("Enter your name: ")
# if len(username) > 12 :
#     print("Username can't be more than 12 characters.")
# elif not username.find(" ") == -1:
#     print("Username can't have spaces.")
# elif not username.isalpha():
#     print("Username can't have any alpha.")
# else:
#     print("Welcome User.")

#compound intrest calculator

# principle = 0
# interest = 0
# time = 0
#
# while principle <= 0:
#     principle = float(input("Enter the principle amount:  "))
#
#     if principle <= 0 :
#         print("Principle can't be less or equal to zero.")
#
# while interest <= 0:
#     interest = float(input("Enter the interest amount:  "))
#
#     if interest <= 0 :
#         print("interest can't be less or equal to zero.")
#
# while time <= 0:
#     time = int(input("Enter the time period:  "))
#
#     if time <= 0 :
#         print("Time can't be less or equal to zero.")
#
# finalAmount = principle * pow((1 + interest/100 ), time)
# print(finalAmount)

#time counter application

# import time
#
# myTime = int(input("Enter your countdown time: "))
#
# for x in range(myTime, 0, -1):
#     seconds = int(x % 60)
#     minutes =  int(x / 60 )  % 60
#     hours = int(x / 3600)
#     print(f" {hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("Times up!!!")

#Pyton quiz time
#
# questions = ("Elements in a periodic table?: ",
#              "Animal which lays the largest egg?: ",
#              "Most abundant gas in earth atmosphere?: ",
#              "Bones in a human body?: ",
#              "Hottest planet in the solar system?: ")
#
# options = (("A.116", "B.117", "C.118", "D.119"),
#            ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
#            ("A.NO2", "B.CO2", "C.O2", "D.SO2"),
#            ("A.206", "B.207", "C.209", "D.208"),
#            ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"))
#
# answers = ("C", "D", "A", "A")
#
# guesses = []
# score = 0
# question_num = 0
#
# for question in questions:
#     print("--------------------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#
#
#
#
#     guesses = input("Enter an option (A, B, C, D)").upper()
#     guesses.append(guesses)
#     if guesses == answers[question_num]:
#         print("Your answer is correct!")
#         score += 1
#     else:
#         print("The answer is incorrect!")
#     question_num += 1

