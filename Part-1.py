#Create a program that will ask for name, age and address.
#Display those details in the following format.
#Hi, my name is ________. I am ______ years old and I live in ______.

from abc import ABC

def Your_Input():
    User_Name = input("What is your name?: ")
    User_Age = int(input("What is your age?: "))
    User_Address = input("Where do you live?: ")
    return User_Name, User_Age, User_Address

def Display_Output(my_name, my_age, my_address):
    print(f"Hi, my name is {my_name}. I am {my_age} years old and I live in {my_address}.")

#Step
#1. Ask for users name, age, and address
Name, Age, Address = Your_Input()
#4. Present the output
Display_Output(Name, Age, Address)