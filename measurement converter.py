#CM
def CM_F(amount):
    converted = amount/30.48
    print('{0:.2f}'.format(converted))
def CM_I(amount):
    converted = amount*0.397
    print('{0:.2f}'.format(converted))
def CM_M(amount):
    converted = amount/100
    print('{0:.2f}'.format(converted))

#M
def M_F(amount):
    converted  = amount*100/30.48
    print('{0:.2f}'.format(converted))

def M_I(amount):
    converted = amount*39.37
    print('{0:.2f}'.format(converted))

def M_CM(amount):
    converted = amount*100
    print('{0:.2f}'.format(converted))

#I
def I_CM(amount):
    converted =  amount*2.54
    print('{0:.2f}'.format(converted))

def I_M(amount):
    converted= amount*2.54/100
    print('{0:.2f}'.format(converted))

def I_F(amount):
    converted= amount/12
    print('{0:.2f}'.format(converted))

#F
def F_CM(amount):
    converted = amount*12*2.54
    print('{0:.2f}'.format(converted))

def F_M(amount):
    converted = amount*12*2.54*100
    print('{0:.2f}'.format(converted))

def F_I(amount):
    converted = amount*12
    print('{0:.2f}'.format(converted))

    
def FEET(to,amount):
    if to == 1:
        print(amount)
    elif to == 2:
        F_I(amount)
    elif to == 3:
        F_CM(amount)
    elif to == 4:
        F_M(amount)
    else:
        print("Invalid choice")

def INCHES(to,amount):
    if to == 1:
        I_F(amount)
    elif to == 2:
        print(amount)
    elif to == 3:
        I_CM(amount)    
    elif to == 4:
        I_M(amount)
        
    else:
        print("Invalid choice")

def CENTI(to,amount):
    if to == 1:
        CM_F(amount)
    elif to == 2:
        CM_I(amount)
    elif to == 3:
        print(amount)   
    elif to == 4:
        CM_M(amount)

def METRE(to,amount):
    if to == 1:
        M_F(amount)
    elif to == 2:
        M_I(amount)
    elif to == 3:
        M_CM(amount)    
    elif to == 4:
        print(amount)


def converting(to,from1,amount):
    
    if from1 == 1:
        FEET(to,amount)
    elif from1 == 2:
        INCHES(to,amount)
    elif from1 == 3:
        CENTI(to,amount)
    elif from1 == 4:
        METRE(to,amount)
    else:
        print("Invalid choice")

def input_details():
    print("1. Feet")
    print("2. Inches")
    print("3. Centimetres")
    print("4. Metres")
    from1 = int(input("Please input the unit you wish to convert from: ")) 
    to = int(input("Please input the unit you wish to convert to: "))
    amount = float(input("How much would you like to convert: "))
    return from1,to,amount

def main():
    from1,to,amount = input_details()
    converting(to,from1,amount)

main()
                
                


                
