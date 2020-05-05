import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid
import pprint

columns = ['Order ID', 'Product',
           'Quantity Ordered', 'Price Each', 'Order Date']

# Each dictionary below represents a category. The key is the product name. In the list, the first value represents the price
# and the second value represents the "weight", which is how much someone is likely to buy a product. The higher the number, the more likely they are to buy.
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
    'Donut (Matcha)': [2.50, 15],
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
    'Macaroon (Earl Grey)': [3.00, 6],
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


# SOLUTION: https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python
drinks = {**hot_drinks, **cold_drinks}

# inventory of all products
products = {**hot_drinks, **cold_drinks, **
            single_serving_sweets, **bulk_sweets, **savory_meals}

"""
Generates a random day (represented as a number) of a particular month. This is a helper function for generate_random_time.

input: month, an interger b/w 1 (January) to 12 (december)
output: a random number between the range and the month

sources:
https://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python
https://docs.python.org/3/library/calendar.html#calendar.monthrange
"""


def generate_random_day(month):
    # I had to play around with this and didn't know about this since we only need the month, we just index the second param
    day_range = calendar.monthrange(2020, month)[1]
    return random.randint(1, day_range)


"""
Generates a random date based on the month

input: month (interger)
output: date in format mm/dd/year hh:mm

sources:
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.normal.html
https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
"""


def generate_random_time(month):
    day = generate_random_day(month)

    # peak times are around 7am +/- 2 hours and 11am +/2 hours
    if random.random() < 0.5:
        date = datetime.datetime(2020, month, day, 7, 00)
    else:
        date = datetime.datetime(2020, month, day, 11, 00)

    time_offset = numpy.random.normal(loc=0.0, scale=120)
    final_date = date + datetime.timedelta(minutes=time_offset)

    return final_date.strftime("%m/%d/%y %H:%M")


"""
Purpose: Creates a new row with a given order number, product, and order_date.
Known Uses:

input: order_number (integer), product (String), order_date (date in format mm/dd/year H:mm)
output: returns a list containing data values for the correct columns
"""


def write_row(order_number, product, order_date):
    product_price = products[product][0]
    quantity = numpy.random.geometric(p=1.0-(1.0/product_price), size=1)[0]
    output = [order_number, product, quantity, product_price, order_date]
    return output

if __name__ == '__main__':
  order_number = 11000
  product_list = [product for product in products]
  weights = [products[product][1] for product in products]

  for month in range(1,13):
    if month == 12:
        order_amount = int(numpy.random.normal(loc=14000, scale=3000)) 

    elif month in range(7,9):
        order_amount = int(numpy.random.normal(loc=20000, scale=3000)) 

    elif month in range(1,4):
        order_amount = int(numpy.random.normal(loc=9000, scale=3000)) 
    
    else: 
        order_amount = int(numpy.random.normal(loc=12000, scale=4000)) 

    df = pd.DataFrame(columns=columns)

    i = 0
    while order_amount > 0:
      order_date = generate_random_time(month)

      product_choice = random.choices(product_list, weights)[0]
      df.loc[i] = write_row(order_number, product_choice, order_date)
      i += 1
      
      if product_choice in single_serving_sweets.keys():
          if random.random() <  0.30:
              df.loc[i] =  write_row(order_number, random.choice(list(drinks)), order_date)
              i += 1

      order_number += 1
      order_amount -= 1

    month_name = calendar.month_name[month]
    df.to_csv(f"Sales_{month_name}_2020.csv", index=False)
    print(f"{month_name} Complete")