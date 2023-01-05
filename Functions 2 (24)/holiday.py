#globals
HOTEL_COST_PER_NIGHT = 40
CAR_COST_PER_NIGHT = 10


def hotel_cost(nights):
    """calculates the cost of the hotel given the number of nights"""
    cost = nights * HOTEL_COST_PER_NIGHT
    return cost


def plane_cost(city):
    """calculates the cost of the flight given the city"""
    if city.lower() == "london":
        cost = 40
    elif city.lower() == "paris":
        cost = 90
    elif city.lower() == "new york":
        cost = 600
    elif city.lower() == "munich":
        cost = 70
    return cost


def car_rental(days):
    """calculates the cost of the car rental given the number of days"""
    cost = days * CAR_COST_PER_NIGHT
    return cost


def holiday_cost(nights, city, days):
    """calculates total cost of the holiday given the number of nights, days and the city"""
    total_cost = car_rental(days) + plane_cost(city) + hotel_cost(nights)
    return total_cost


# user inputs
nights = int(input("How many nights are you staying? "))
city = input("Which city are you flying to? ")
days = int(input("How many days are you renting the car for? "))

#print results
print(f"The hotel will cost £{hotel_cost(nights)}")
print(f"The flight will cost £{plane_cost(city)}")
print(f"The car will cost £{car_rental(days)}")
print(f"The whole holiday will cost £{holiday_cost(nights, city, days)}")
