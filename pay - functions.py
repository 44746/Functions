#George West
#18-11-14
#calculate pay
def calculate_basic_pay(hours,pay):
    total = hours*pay
    return total
    
def calculate_overtime_pay(hours,pay):
    overtime_hours = hours-40
    overtime_pay = pay*1.5
    total_overtime_pay = overtime_hours*overtime_pay
    basic = pay*40
    total = basic+total_overtime_pay
    return total

def calculate_total_pay(hours,pay):
    if hours<= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours  = int(input("Please input the amount of hours worked: "))
    pay = float(input("Please enter your pay rate: "))
    return hours,pay
def display_total(total):
    print(total)
        
def calculate_pay():
    hours,pay = work_details()
    total = calculate_total_pay(hours,pay)
    display_total(total)


calculate_pay()
