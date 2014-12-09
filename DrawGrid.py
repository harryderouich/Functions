# define functions

def get_grid_size():
    valid_grid = False
    while valid_grid == False:
        this_grid_size = int(input("Please enter the size of the grid (max 20): "))
        if this_grid_size <= 20 and this_grid_size > 0:
            valid_grid = True
        else:
            valid_grid = False
            print("Please enter a number between 1 and 20 inclusive")
            print()
    return this_grid_size


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

# main program

size = get_grid_size()
rowToDraw = GetGridRow(size)
DisplayGrid(size, rowToDraw)
