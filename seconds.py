
def input_time():
    hours=int(input("Please enter the number of hours: "))
    minutes = int(input("Please enter the number of minutes: "))
    seconds=int(input("Please enter the number of seconds: "))
    return hours,minutes,seconds

def calculation(hours,minutes,seconds):
    seconds_calculation = (hours*60*60)+(minutes*60)+seconds
    return seconds_calculation
def display(seconds_calculation):
    print(seconds_calculation)

def calculate_seconds():
    hours,seconds,minutes = input_time()
    seconds_calculation = calculation(hours,minutes,seconds)
    display(seconds_calculation)
    

calculate_seconds()
