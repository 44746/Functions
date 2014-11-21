def input_number():
    number = int(input("Please enter an odd number: "))
    return number

def top(number):
    if number % 2 > 0:
        counter =1
        while counter <=number:
            list1=''
            for count in range(counter):
                list1= list1 + '*'
            counter = counter +2
            print("{0:^{1}}".format(list1,number))
def bottom(number):
    if number % 2 > 0:
        counter = number -2
    while counter >= 1:
        list1=''
        for count in range(counter):
                list1= list1 + '*'
        counter = counter -2
        print("{0:^{1}}".format(list1, number))
def display(number):
    top(number)
    bottom(number)
    

def diamond():
    number = input_number()
    display(number)

diamond()


