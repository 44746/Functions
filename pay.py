#George West
#14-11-14
#pay
basic_hours= float(input("Please enter your basic hours: "))
overtime_hours= float(input("Please enter your overtime hours: "))
basic_rate= float(input("Please enter your basic rate: "))
overtime_rate= float(input("Please enter your overtime rate: "))
basic_pay = basic_hours*basic_rate
overtime_pay = overtime_rate*overtime_rate
total_pay = overtime_pay+basic_pay
print("You got paid £{0}".format(total_pay))
