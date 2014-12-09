def GetInput():
    distance = float(input("Please input the distance: "))
    mpg = float(input("Please input the Miles per gallon of the vehicle: "))
    price = float(input("Please input the current price of fuel: "))
    return distance,mpg,price

def CalculateCost(distance,mpg,price):
    price_per_gallon = price*4.55
    gallons_needed = distance/mpg
    journey_fuel_cost = gallons_needed*price_per_gallon /100
    return journey_fuel_cost

def DisplayCost(journey_fuel_cost):
    print("The total fuel cost for the journey is £{0:.2f}".format(journey_fuel_cost))

def main():
    distance,mpg,price = GetInput()
    journey_fuel_cost = CalculateCost(distance,mpg,price)
    DisplayCost(journey_fuel_cost)

main()
