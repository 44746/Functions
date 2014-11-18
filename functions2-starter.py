#as computing/python/functions/functions2 starter
#31-10-12

def GetHoursAndRate():
    Hours = -1
    Rate = -1
    while Hours < 0 or Hours >60:
        Hours = input('Please enter the number of hours worked (max. 60 hours): ')
        Hours = int(Hours)
    while Rate < 0:
        Rate = input('Please enter your hourly rate of pay: ')
        Rate = float(Rate)
    return Hours, Rate

def CalculateBasicPay(Hours, Rate):
    BasicPay = 0
    if Hours > 40:
        Hours = 40
        BasicPay = Hours * Rate
    return BasicPay

def CalculateOvertimePay(Hours, Rate):
    OvertimePay =0
    if Hours > 40:
        Hours = Hours % 40
        OvertimePay = Hours * Rate * 1.5

def DisplayTotalPay(TotalPay):
    TotalPay = round(TotalPay,2)
    print('Your pay this week is: £{0}'.format(TotalPay))    

# main program
print('Pay Calculator')
print('')
BasicPay = 0
OvertimePay = 0
Hours, Rate = GetHoursAndRate()     
BasicPay = CalculateBasicPay(Hours, Rate)
CalculateOvertimePay(Hours, Rate)
TotalPay = BasicPay + OvertimePay
DisplayTotalPay(TotalPay)
