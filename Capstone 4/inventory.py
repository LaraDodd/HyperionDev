import pandas
from tkinter import *
from tkinter import messagebox


# ========The beginning of the class==========
class Shoe:
    """Creates show object with various stock data

    Attributes:
        country - string denoting information about what country product is in
        code - string denoting SKUcode for product
        product - string denoting name of product
        cost - int denoting cost of product in GBP
        quantity - int denoting number of product in stock

    Methods:
        get_cost - returns cost of shoe
        get_quantity - returns quantity of shoes
        __str__ - returns string of class"""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self) -> int:
        """returns cost attribute"""
        return self.cost

    def get_quantity(self) -> int:
        """returns class quantity attribute"""
        return self.quantity

    def __str__(self):
        output = f"Country: {self.country}\n"
        output += f"Product code: {self.code}\n"
        output += f"Product: {self.product}\n"
        output += f"Product cost: {self.cost}\n"
        output += f"Product quantity: {self.quantity}\n"
        return output


# =============initial variables===========

shoe_list = []  # used to store a list of objects of shoes
shoes_df = pandas.read_csv("inventory.csv")  # stores csv data


# =============Functions outside the class==============

def read_shoes_data() -> dict:
    """This function will open the file inventory.csv in a pd dataframe
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list."""
    shoes_dict = shoes_df.to_dict(orient="records")
    for data in shoes_dict:
        shoe_object = Shoe(data["Country"], data["Code"], data["Product"], data["Cost (£)"], data["Quantity"])
        shoe_list.append(shoe_object)
    return shoes_dict


def capture_shoes():
    """
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list. Also adds shoe data to csv.
    """

    country = input("Please enter the country that the shoes are in: ")
    code = input("Please enter the product code: ")
    product = input("Please enter the name of the shoe: ")
    cost = int(input("Please enter the cost of the shoe: "))
    quantity = int(input("Please enter the stock quantity: "))

    data_dict_item = {'Country': country,
                      'Code': code,
                      'Product': product,
                      'Cost': cost,
                      'Quantity': quantity,
                      }

    shoes_dict_list = read_shoes_data()  # get shoes_dict_list by callind read shoes data method
    shoes_dict_list.append(data_dict_item)

    df = pandas.DataFrame(shoes_dict_list)
    df.to_csv("inventory.csv", index=False)

    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)


def view_all() -> pandas.DataFrame:
    """
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    """
    # read_shoes_data()
    # for shoe in shoe_list:
    #     print(shoe.__str__())

    # leaving above for marker but using pd df as cleaner:
    return shoes_df


def re_stock() -> str:
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    """

    min_qty_product = shoes_df[shoes_df.Quantity == shoes_df.Quantity.min()]
    print(f"The product/s with the lowest stock is/are:\n{min_qty_product}\n")

    sku_false = True
    while sku_false:

        try:
            quantity = int(input("Enter the number that you would like to restock product by "))
        except TypeError:
            print("This is not a number")

        else:
            new_quantity = shoes_df.Quantity.min() + quantity
            index = shoes_df.index[shoes_df.Quantity == shoes_df.Quantity.min()]
            shoes_df.loc[index, "Quantity"] = new_quantity
            sku_false = False

    # write to csv
    shoes_df.to_csv("inventory.csv", index=False)

    print(f"The new quantity of:\n {min_qty_product.Product.to_string(index=False)}\n is {new_quantity}")


def search_shoe() -> str:
    """
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    """

    sku_code = input("Please enter the SKUcode of the item you would like to find details about: ")

    # read_shoes_data()
    # for shoe_object in shoe_list:
    #     try:
    #         if sku_code == shoe_object.code:
    #             selected_shoe = shoe_object
    #             test = selected_shoe.__str__()
    #             print(test)
    #     except:
    #         print("sku not in sys")

    # cleaner using pd

    product = shoes_df[shoes_df.Code == sku_code]
    if len(product) == 0:
        print("This is not a valid SKU")
        search_shoe()

    else:
        print(product)


def value_per_item() -> pandas.DataFrame:
    """
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """
    print("\n")
    shoes_df["Value (£)"] = shoes_df["Cost (£)"] * shoes_df["Quantity"]
    return shoes_df


def highest_qty():
    """
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    """

    max_qty_product = shoes_df[shoes_df.Quantity == shoes_df.Quantity.max()]
    print(f"As we have {shoes_df.Quantity.max()} of the {max_qty_product.Product.to_string(index=False)}, "
          f"they are going on SALE!")


# ==========Main Code=============
def maincode():
    if radio_state.get() == "va":
        output_df = view_all()
        canvas1.itemconfig(display_text, text=str(output_df))
        return

    elif radio_state.get() == "a":
        canvas1.itemconfig(display_text, text="look at console")
        capture_shoes()
        canvas1.itemconfig(display_text, text="Shoe added to db!!!")
        return

    elif radio_state.get() == "rs":
        canvas1.itemconfig(display_text, text="look at console")
        re_stock()
        return

    elif radio_state.get() == "se":
        canvas1.itemconfig(display_text, text="look at console")
        search_shoe()
        return

    elif radio_state.get() == "sa":
        canvas1.itemconfig(display_text, text="look at console")
        highest_qty()
        return

    elif radio_state.get() == "£££":
        value_df = value_per_item()
        canvas1.itemconfig(display_text, text=str(value_df))
        return

    elif radio_state.get() == 'e':
        canvas1.itemconfig(display_text, text="Goodbye!!!", font=("arial", 30, "bold"))
        exit()


# ==========UI=============
# Create object
window = Tk()

# Adjust size
window.geometry("1000x600")

# Add image file
bg = PhotoImage(file="background2.png")

# Create Canvas
canvas1 = Canvas(window, width=1000, height=600)
canvas1.grid(row=0, column=0, rowspan=2)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Add Text
canvas1.create_text(200, 50, text="Welcome Menu", font=("courier", 30, "bold"), fill="pink")

# create radio buttons
radio_state = StringVar(value="r")  # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="View all products", value="va", variable=radio_state, command=maincode)
radiobutton2 = Radiobutton(text="Add product to database", value="a", variable=radio_state, command=maincode)
radiobutton3 = Radiobutton(text="re-stock lowest quantity items", value="rs", variable=radio_state, command=maincode)
radiobutton4 = Radiobutton(text="search for specific product details", value="se", variable=radio_state,
                           command=maincode)
radiobutton5 = Radiobutton(text="View sale product", value="sa", variable=radio_state, command=maincode)
radiobutton6 = Radiobutton(text="View value amount of each product", value="£££", variable=radio_state,
                           command=maincode)
radiobutton7 = Radiobutton(text="Exit", value="e", variable=radio_state, command=maincode)

# Display Buttons
button1_canvas = canvas1.create_window(100, 100, anchor="nw", window=radiobutton1)
button2_canvas = canvas1.create_window(100, 125, anchor="nw", window=radiobutton2)
button3_canvas = canvas1.create_window(100, 150, anchor="nw", window=radiobutton3)
button4_canvas = canvas1.create_window(100, 175, anchor="nw", window=radiobutton4)
button5_canvas = canvas1.create_window(100, 200, anchor="nw", window=radiobutton5)
button6_canvas = canvas1.create_window(100, 225, anchor="nw", window=radiobutton6)
button7_canvas = canvas1.create_window(100, 250, anchor="nw", window=radiobutton7)

display_text = canvas1.create_text(500, 300, text="", fill="black", font=("arial", 10, "italic"), anchor="w")


# Execute tkinter
window.mainloop()
