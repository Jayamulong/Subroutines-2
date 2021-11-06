#Create a program that will ask how many apples and oranges you want to buy.
#Display the amount you need to pay if apple price is 20 pesos and orange is 25.

from abc import ABC

def Fruit_Price():
    Apple_Func = int(20)
    Orange_Func = int(25)
    print(f"The price for an apple is {Apple_Func}, and the price for an orange is {Orange_Func}.")
    return Apple_Func, Orange_Func

def Buying_Fruit_Amount():
    Apple_Number = int(input("How many apples you want to buy?: "))
    Orange_Number = int(input("How many oranges you want to buy?: "))
    print(f"The amount of apples bought is {Apple_Number} and the amount of oranges bought is {Orange_Number}.")
    return Apple_Number, Orange_Number

def Calculate_Fruit_Price():
    Apples_Prices = 20*Apple
    print(f"The total price of apples is {Apples_Prices}")
    Oranges_Prices = 25*Orange
    print(f"The total price of oranges is {Oranges_Prices}")
    return Apples_Prices, Oranges_Prices

def Total_Amount():
    Total = Apple_Total + Orange_Total
    print(f"The total amount is {Total}")
    
# Steps:
# # 1. Present the apple and the orange price
Prices = Fruit_Price()
# 2. Ask how many apples and orange will buy
Apple, Orange = Buying_Fruit_Amount()
#Calculate the amount and price of apples and oranges
Apple_Total, Orange_Total = Calculate_Fruit_Price()
#Give the total amount of apples and oranges combined
Total_Amount()