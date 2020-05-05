"""
import pprint

# SOLUTION: https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python

hot_drinks = {
    'Dalgona Coffee (Original - Hot)': [2.75, 15],
    'Dalgona Coffee (Strawberry - Hot)': [3.00, 7],
    'Dalgona Coffee (Chocolate - Hot)': [3.00, 8],
    'Dalgona Coffee (Matcha - Hot)': [3.00, 9],
    'Americano (Hot)': [3.50, 8],
    'Coffee (Hot)': [2.25, 9],
    'Latte (Rose)': [4.75, 8], 
    'Latte (Sakura)': [4.75, 8], 
    'Latte (Caramel)': [4.25, 9], 
    'Latte (Matcha)': [4.75, 15], 
    'Latte (Regular)': [4.00, 9], 
    'Tea (Earl Grey)': [1.75, 6],
    'Tea (Green Tea)': [1.75, 6],
    'Tea (Rose)': [2.00, 7],
    'Tea (Sakura)': [2.00, 7],
    'Tea (Lavender)': [2.00, 8],
}

cold_drinks = {
    'Dalgona Coffee (Original - Cold)': [3.00, 15],
    'Dalgona Coffee (Strawberry - Cold)': [3.25, 7],
    'Dalgona Coffee (Chocolate - Cold)': [3.25, 8],
    'Dalgona Coffee (Matcha - Cold)': [3.25, 9],
    'Mango Yakult Refresher': [4.75, 15],  
    'Green Tea Yakult Refresher': [5.00, 7], 
    'Peach Yakult Refresher': [4.75, 8],
    'Americano (Iced)': [3.50, 9],
    'Coffee (Iced)': [2.50, 9],
}

single_serving_sweets = {
    'Red Bean Bun': [2.75, 8],
    'Green Tea Bun': [2.75, 12],
    'Donut (Red Bean)': [2.50, 10],
    'Donut (Ube)': [2.50, 8], 
    'Donut (Matcha)':[2.50, 15],
    'Japanese Rolled Cake (Slice - Original)': [4.00, 8],
    'Japanese Rolled Cake (Slice - Strawberry Cream)': [4.00, 8],
    'Japanese Rolled Cake (Slice - Matcha)': [4.00, 12],
    'Japanese Rolled Cake (Slice - Chocolate)': [4.00, 8],
    'Japanese Rolled Cake (Slice - Ube)': [4.00, 8],
    'Portguese Tart Egg Tarts (Single)': [2.00, 7],
    'Green Tea Banana Bread (Slice)': [1.75, 9],
    'Mini Cheese Tart (Orginal)': [3.75, 6], 
    'Mini Cheese Tart (Matcha)': [3.75, 6], 
    'Mini Cheese Tart (Chocolate)': [3.75, 5], 
    'Macaroon (Vanilla)': [2.75, 7],
    'Macaroon (Chocolate)': [2.75, 7],
    'Macaroon (Strawberry)': [2.75, 7],
    'Macaroon (Matcha)': [3.00, 8],
    'Macaroon (Earl Grey)':[3.00, 6],
    'Macaroon (Mango)': [3.00, 8],
    'Macaroon (Black Seasame)': [3.00, 8],
    'Macaroon (Lavender)': [3.00, 7],
    'Macaroon (Green Tea)': [3.00, 6],
    'Macaroon (Pandan Coconut)': [3.00, 8],
    'Macaroon (Vietnamese Coffee)': [3.00, 7],
    'Macaroon (Pistachio)': [3.00, 15],
    'Japanese Cheesecake (Slice - Original)': [3.75, 9],
    'Japanese Cheesecake (Slice - Matcha)': [4.00, 8],
}

bulk_sweets = {
    'Japanese Rolled Cake (Roll - Original)': [12.00, 12],
    'Japanese Rolled Cake (Roll - Strawberry Cream)': [12.00, 15],
    'Japanese Rolled Cake (Roll - Matcha)': [12.00, 9],
    'Japanese Rolled Cake (Roll - Chocolate)': [12.00, 8],
    'Japanese Rolled Cake (Roll - Ube)': [12.00, 8],
    'Japanese Cheesecake (Full - Original)': [11.75, 15],
    'Japanese Cheesecake (Full - Matcha)': [12.00, 8],
    'Green Tea Banana Bread (Loaf)': [4.75, 7],
    'Milk Bread (Loaf)': [4.50, 7],
    'Portguese Tart Egg Tarts (6)': [11.00, 8],
    'Macaroon Set (6)': [15.00, 5],
}

savory_meals = {
    'Bulgogi Bun': [2.75, 8],
    'Original Croquette': [3.00, 15], 
    'Special Vegetarian Curry Set': [15.00, 7],
    'Special Bulgogi Set': [12.50, 8],
    'Special Japanese Pork Cutlet Set': [12.00, 9],
    'Tamago Sando (Japanese Egg Sandwich)': [4.50, 7],
    'Fruit Sando (Japanese Fruit Sando)': [4.50, 6],
    'Katsu Sando (Cripsy Chicken Katsu Sandwich)': [7.50, 9]
} 
"""
import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid
import pprint

def determine_order_amount(month):
    if month == 12:
        order_amount = int(numpy.random.normal(loc=14000, scale=3000))
    elif month in range(7, 9):
        order_amount = int(numpy.random.normal(loc=20000, scale=3000))
    elif month in range(1, 4):
        order_amount = int(numpy.random.normal(loc=9000, scale=3000))
    else:
        order_amount = int(numpy.random.normal(loc=12000, scale=4000))
    return order_amount

print(determine_order_amount(12))