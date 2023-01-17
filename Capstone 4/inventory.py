import pandas


#========The beginning of the class==========
class Shoe:
    """Creates show object with various stock data

    Attributes:
        country - where it is
        code -
        product -
        cost -
        quanitity -

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

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        output = f"Country: {self.country}"
        output += f"product code: {self.code}"
        output += f"product: {self.product}"
        output += f"product cost: {self.cost}"
        output += f"product quantity: {self.quantity}"
        return output


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    """This function will open the file inventory.csv in a pd dataframe
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list."""
    shoes_df = pandas.read_csv("inventory.csv")
    shoes_dict = shoes_df.to_dict()
    print(shoes_dict)



def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data()