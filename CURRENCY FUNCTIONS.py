#GEORGE WEST
#28-11-14
#CURRENCY FUNCTIONS

def get_currency_details():
    print("1. GBP")
    print("2. Euro")
    print("3. US")
    currency_from = int(input("Which currency do you want to covert from: "))
    user_ans = int(input("which currency do you want to convert to: "))
    amount = float(input("How much would you like to convert: "))
    return currency_from, user_ans,amount                   



def GBP(user_ans,amount):
    if user_ans == 1:
        print("GBP to GBP??? {0}".format(amount))
    elif user_ans == 2:
        GBP_EURO(amount)
    elif user_ans == 3:
        GBP_US(amount)
    else:
        print("Invalid choice")

def GBP_EURO(amount):
    converted = amount*1.229
    print('{0:.2f}'.format(converted))

def GBP_US(amount):
    converted = amount*1.601
    print('{0:.2f}'.format(converted))




def EURO(user_ans,amount):
    if user_ans == 1:
        EURO_GBP(amount)
    elif user_ans == 2:
        print("Euro to Euro??? {0}".format(amount))
    elif user_ans == 3:
        EURO_US(amount)
    else:
        print("Invalid choice")

def EURO_GBP(amount):
    converted = amount*0.814
    print('{0:.2f}'.format(converted))

def EURO_US(amount):
    converted = amount*1.302
    print('{0:.2f}'.format(converted))




def US(user_ans,amount):
    if user_ans == 1:
        US_GBP(amount)
    elif user_ans == 2:
        US_EURO(amount)
    elif user_ans==3:
        print("Euro to Euro??? {0}".format(amount))
    else:
        print("Invalid choice")

def US_GBP(amount):
    converted = amount*0.625
    print('{0:.2f}'.format(converted))

def US_GBP(amount):
    converted = amount*0.768
    print('{0:.2f}'.format(converted))




def calculator(currency_from,user_ans,amount):
    if currency_from == 1:
        GBP(user_ans,amount)
    elif currency_from == 2:
        EURO(user_ans,amount)
    elif currency_from == 3:
        US(user_ans,amount)
    else:
        print("Invalid choice")

def main():
    currency_from, user_ans,amount = get_currecny_details()
    calculator(currency_from,user_ans, amount)

main()

