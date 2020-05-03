import pandas as pd
import numpy 
import random
import calendar 
import datetime 

# dictionary with product and price 
products = {
    'Milk Bread (Slice)': [1.25, 12],
    'Milk Bread (Loaf)': [4.50, 7],
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
    'Japanese Rolled Cake (Roll - Original)': [12.00, 12],
    'Japanese Rolled Cake (Roll - Strawberry Cream)': [12.00, 15],
    'Japanese Rolled Cake (Roll - Matcha)': [12.00, 9],
    'Japanese Rolled Cake (Roll - Chocolate)': [12.00, 8],
    'Japanese Rolled Cake (Roll - Ube)': [12.00, 8],
    'Portguese Tart Egg Tarts (Single)': [2.00, 7],
    'Portguese Tart Egg Tarts (6)': [11.00, 8],
    'Green Tea Banana Bread (Slice)': [1.75, 9],
    'Green Tea Banana Bread (Loaf)': [4.75, 7],
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
    'Dalgona Coffee (Original - Hot)': [2.75, 15],
    'Dalgona Coffee (Original - Cold)': [3.00, 15],
    'Dalgona Coffee (Strawberry - Hot)': [3.00, 7],
    'Dalgona Coffee (Strawberry - Cold)': [3.25, 7],
    'Dalgona Coffee (Chocolate - Hot)': [3.00, 8],
    'Dalgona Coffee (Chocolate - Cold)': [3.25, 8],
    'Dalgona Coffee (Matcha - Hot)': [3.00, 9],
    'Dalgona Coffee (Matcha - Cold)': [3.25, 9],
    'Mango Yakult Refresher': [4.75, 15],  
    'Green Tea Yakult Refresher': [5.00, 7], 
    'Peach Yakult Refresher': [4.75, 8],
    'Americano (Hot)': [3.50, 8],
    'Americano (Iced)': [3.50, 9],
    'Coffee (Hot)': [2.25, 9],
    'Coffee (Iced)': [2.50, 9],
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
    'Bulgogi Bun': [2.75, 8],
    'Original Croquette': [3.00, 15], 
    'Special Vegetarian Curry Lunch Set': [15.00, 7],
    'Special Bulgogi Lunch Set': [12.50, 8],
    'Special Japanese Pork Cutlet Lunch Set': [12.00, 9],
    'Tamago Sando (Japanese Egg Sandwich)': [4.50, 7],
    'Fruit Sando (Japanese Fruit Sando)': [4.50, 6],
    'Katsu Sando (Cripsy Chicken Katsu Sandwich)': [7.50, 9], 
    'Japanese Cheesecake (Slice - Original)': [3.75, 9],
    'Japanese Cheesecake (Slice - Matcha)': [4.00, 8],
    'Japanese Cheesecake (Full - Original)': [11.75, 15],
    'Japanese Cheesecake (Full - Matcha)': [12.00, 8],
}

drinks = {
    'Dalgona Coffee (Original - Hot)': [2.75, 15],
    'Dalgona Coffee (Original - Cold)': [3.00, 15],
    'Dalgona Coffee (Strawberry - Hot)': [3.00, 7],
    'Dalgona Coffee (Strawberry - Cold)': [3.25, 7],
    'Dalgona Coffee (Chocolate - Hot)': [3.00, 8],
    'Dalgona Coffee (Chocolate - Cold)': [3.25, 8],
    'Dalgona Coffee (Matcha - Hot)': [3.00, 9],
    'Dalgona Coffee (Matcha - Cold)': [3.25, 9],
    'Mango Yakult Refresher': [4.75, 15],  
    'Green Tea Yakult Refresher': [5.00, 7], 
    'Peach Yakult Refresher': [4.75, 8],
    'Americano (Hot)': [3.50, 8],
    'Americano (Iced)': [3.50, 9],
    'Coffee (Hot)': [2.25, 9],
    'Coffee (Iced)': [2.50, 9],
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

sweets = {
    'Milk Bread (Slice)': [1.25, 12],
    'Milk Bread (Loaf)': [4.50, 7],
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
    'Japanese Rolled Cake (Roll - Original)': [12.00, 12],
    'Japanese Rolled Cake (Roll - Strawberry Cream)': [12.00, 15],
    'Japanese Rolled Cake (Roll - Matcha)': [12.00, 9],
    'Japanese Rolled Cake (Roll - Chocolate)': [12.00, 8],
    'Japanese Rolled Cake (Roll - Ube)': [12.00, 8],
    'Portguese Tart Egg Tarts (Single)': [2.00, 7],
    'Portguese Tart Egg Tarts (6)': [11.00, 8],
    'Green Tea Banana Bread (Slice)': [1.75, 9],
    'Green Tea Banana Bread (Loaf)': [4.75, 7],
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
}

product_list = [product for product in products]
weights = [products[product][1] for product in products]

columns = ['Reciept ID', 'Product', 'Quantity Ordered', 'Price Each', 'Date']
order_id = 11000

df = pd.DataFrame(columns=columns)

def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2019, month, day,7,00)
  else:
    date = datetime.datetime(2019, month, day,11,00)
  time_offset = numpy.random.normal(loc=0.0, scale=120)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date.strftime("%m/%d/%y %H:%M")

def generate_random_day(month):
  day_range = calendar.monthrange(2019,month)[1]
  return random.randint(1,day_range)

def write_row(order_number, product, order_date):
  product_price = products[product][0]
  quantity = numpy.random.geometric(p=1.0-(1.0/product_price), size=1)[0]
  output = [order_number, product, quantity, product_price, order_date]
  return output

for month_value in range(1, 13):
    df = pd.DataFrame(columns=columns)

    if month_value == 12:
        orders_amount = int(numpy.random.normal(loc=14000, scale=3000)) 

    elif month_value in range(7,9):
        orders_amount = int(numpy.random.normal(loc=20000, scale=3000)) 

    elif month_value in range(1,4):
        orders_amount = int(numpy.random.normal(loc=9000, scale=3000)) 
    
    else: 
        orders_amount = int(numpy.random.normal(loc=12000, scale=4000)) 

    for i in range(orders_amount):
        date = generate_random_time(month_value)

        product = random.choices(product_list, weights=weights)[0]
        price = products[product][0]
        quantity_ordered = numpy.random.geometric(p=1.0-(1.0/price), size=1)[0]
        df.loc[i] = [order_id, product, quantity_ordered, price, date]

        if product in sweets.keys():
            if random.random() <  0.30:
                df.loc[i] =  write_row(order_id, random.choice(list(drinks)), date)

        order_id += 1

    month_name = calendar.month_name[month_value]
    df.to_csv(f"{month_name}_data.csv")
    break

