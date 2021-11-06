#Create a prgram which you will enter the amount of money you have, it will also ask for te price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.

from abc import ABC

def Money_Apple_Amount():
    money = float(input("Enter amount of money: "))
    apple = float(input("Enter the price of an apple: "))
    return money, apple

def Sum_And_Change():
    Apple_Amount = Money // Apple
    Price = Apple_Amount*Apple
    Change = Money - Price
    return Apple_Amount, Change

def Display_Output(ApplesA, ChangeM):
    print(f"You can buy {ApplesA} apples and your change is {ChangeM:.2f} pesos.")

#Steps
#1. Ask how much money it have and a price for an apple
Money, Apple = Money_Apple_Amount()
#2. Calculate how many apples you can buy in money an the change for it
Apples, Change = Sum_And_Change()
#5. Report how many apples you can buy and your change
Display_Output(Apples, Change)