products = input("Please enter three products, each product separated by a comma ")

products_list = products.split(",")  # splits string into a list with ',' as separator
price_list = []  # initialises list

for item in products_list:
    price = input(f"Please enter the price (in pounds) for {item} ")
    price_stripped = int(price.strip("£"))
    price_list.append(price_stripped)

total_cost = sum(price_list)
average_cost = total_cost/len(price_list)

print(f"The Total of {products_list[0]},{products_list[1]} and{products_list[2]} is £{total_cost} "
      f"and the average price of the items is £{round(average_cost,3)}")




