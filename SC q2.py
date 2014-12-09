def GetGridSize():

    thisGridSize = 8
    validGrid = False
    while validGrid == False:
        thisGridSize= int(input("Please enter the size of the grid(max 20): "))
        if thisGridSize <= 20 and thisGridSize > 0:
            validGrid = True

    return thisGridSize



def GetGridRow(aRowLength):
    # draws a single row using |_ for each square
    thisRow = '|_' * (aRowLength)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow

def DisplayGrid(aGridSize, aRow):
    # display top of grid using _ as top of each square
    print(' _' * aGridSize)
    # display rows of |_| for each row
    for rowCount in range(aGridSize):
        print(aRow)


thisGridSize = GetGridSize()
rowToDraw = GetGridRow(thisGridSize)
DisplayGrid(thisGridSize, rowToDraw)
