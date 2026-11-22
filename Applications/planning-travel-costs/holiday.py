#Get the flight option
flight_option = input("Choose between: Economy, first class or business class:").lower()
#Get the city option
city_flight = input("Which city are you flying to?:").lower()
#Get the number of nights at the hotel
num_nights = int(input("How many nights are you staying at the hotel?:"))
#Get the rental fee of the car
rental_days = int(input("How many days are you renting the car?:"))
#Get the cost of the flight
def cost_of_flight(city_flight, flight_option): 
    """
    Docstring for cost_of_flight
    
    :param city_flight: Name of the city
    :param flight_option: Type of flight class
    """
    if city_flight == "cape town" and flight_option == "economy":
        total_flight_cost = 3000

    elif city_flight == "cape town" and flight_option == "first class":
        total_flight_cost = 3500

    elif city_flight == "cape town" and flight_option == "business class":
        total_flight_cost = 4000

    elif city_flight in ["johannesburg", "kwazulu natal"] and flight_option == "economy":
        total_flight_cost = 1500

    elif city_flight in ["johannesburg", "kwazulu natal"] and flight_option == "first class":
        total_flight_cost = 2000

    elif city_flight in ["johannesburg", "kwazulu natal"] and flight_option == "business class":
        total_flight_cost = 2500
        """_summary_

        Returns:
            total_flight_cost: Total flight costs
        """
    return total_flight_cost
#Get the cost of the hotel
def cost_of_hotel(num_nights,price=500):
    """
    Docstring for cost_of_hotel
    
    :param num_nights: Number of nights at the hotel
    :param price: Price per night
    """
    hotel_costs = num_nights*price
    """_summary_

    Returns:
        hotel_cost: Total price of hotel
    """
    return hotel_costs
#Get the cost of the car rental fee 
def cost_of_rental(rental_days,hire_price=200):
    """
    Docstring for cost_of_rental
    
    :param rental_days: number of days renting the car
    :param hire_price: price of car per day
    """
    rent_costs = rental_days*hire_price
    """_summary_

    Returns:
        cost of rental: total cost of car rental 
    """
    return rent_costs
#Total cost of the holiday
flight_total_cost = cost_of_flight(city_flight,flight_option)
hotel_total_cost = cost_of_hotel(num_nights)
rental_total_cost = cost_of_rental(rental_days)

total = flight_total_cost + hotel_total_cost + rental_total_cost
print(f"Your total cost is: {total}")
