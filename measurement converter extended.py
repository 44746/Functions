def menu():
    print("1. Metric")
    print("2. Imperial")
    
def menu_choice():
    from1 = int(input("Please input the unit you wish to convert from: "))
    return from1
def measurements(from1):
    M=0
    CM=0
    F=0
    I=0
    if from1 == 1:
           M = float(input("Please input the number of metres: "))
           CM = float(input("And the number of centimetres: "))
           
    elif from1 == 2:
            F= float(input("Please input the number of feet: "))
            I = float(input("And the number of inches: "))
            
    else:
        print("Invalid choice")
    return M,CM,F,I

def M_I(M,CM):
    CM = CM + (M*100)
    I = CM/2.54
    F = I//12
    I = I%12
    
    print("{0} Feet and {1:.2f} Inches".format(F,I))

def I_M(F,I):
    I = I+ F*12
    CM= I*2.54
    M = CM//100
    CM = CM%100
    print("{0} Metres and {1:.2f} Centimetres".format(M,CM))

def choice(from1,M,CM,F,I):
    if from1 == 1:
        M_I(M,CM)
    elif from1==2:
        I_M(F,I)
    
def main():
    menu()
    from1=menu_choice()
    M,CM,F,I= measurements(from1)
    choice(from1,M,CM,F,I)

main()
