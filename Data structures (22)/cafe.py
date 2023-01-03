
# initialise lists and dictionaries containing relevant info
menu = ['spaghetti bolognese', 'chicken korma', 'lasagne', 'soup of the day']

stock_dict = {
    "spaghetti bolognese": 45,
    "chicken korma": 50,
    "lasagne": 35,
    "soup of the day": 25,
}

price_dict = {
    "spaghetti bolognese": 10.00,
    "chicken korma": 13.50,
    "lasagne": 9.99,
    "soup of the day": 6.00,
}

#  calculate the total stock worth in the cafe
total = 0
for meal in menu:
    total_value = stock_dict[meal] * price_dict[meal]  # use meal name as key, multiply cost of meal by stock no of meal
    total += total_value

print(f"The total stock worth is £{total}")
