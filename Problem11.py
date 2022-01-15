#First, read in the grid from Problem11Grid.txt
#Then, take the data from the grid and create a 2d list of ints
#Then, write functions that calculate the product in all the required directions
#Finally, use those functions when iterating over the 2d list to search for the largest product
#As of now, this code can be drastically improved and should be refactored - the same lines are used with very slight modifications
#However, as is, this does provide the correct answer

#Get data from the relevant text file
grid = open('Problem11Grid.txt', 'r')
rows = grid.readlines()

#Initialize a list to store individual rows (each row is converted to a list of 2 digit strings and new line characters are removed before being appended)
gridAsList = []
for row in rows:
    gridAsList.append(row.strip().split(" "))

#Now, iterate over the entire grid and convert all values to ints

for i in range(len(gridAsList)):
    for j in range(len(gridAsList[i])):
        gridAsList[i][j] = int(gridAsList[i][j])

#With the grid now stored as a 2d list of ints, functions are needed to calculate the product going up/down, left/right, and diagonally

def upDown(twoDimensionalArr, y, x, searchSize = 4):
    """
    To search going up/down, start at (y, x) then increment y until at (y + (searchSize - 1), x)
    We don't have to worry about indexing out of bounds for now since we can only call this function for y values <= 16
    """
    product = twoDimensionalArr[y][x]
    for i in range(searchSize-1):
        y+=1
        product*=twoDimensionalArr[y][x]
    return product

def leftRight(twoDimensionalArr, y, x, searchSize = 4):
    """
    To search going left/right, start at (y, x) then increment x until at (y, x + (searchSize - 1))
    We don't have to worry about indexing out of bounds for now since we can only call this function for x values <= 16
    """
    product = twoDimensionalArr[y][x]
    for i in range(searchSize-1):
        x+=1
        product*=twoDimensionalArr[y][x]
    return product

def diagonal(twoDimensionalArr, y, x, downRight = True, searchSize = 4):
    """
    Returns the diagonal product of a two dimensional array, calculating the product for n numbers where n = searchSize
    If downRight, calculates the diagonal where you increment x and y
    Else, calculates the diagonal where you increment x and decrement y
    To avoid indexing out of bounds, will only calculate values for downRight = True when x <= 16 and y <=16
    and for downRight = False when x <=16 and 3 <= y <= 19
    """
    product = twoDimensionalArr[y][x]
    if downRight:
        for i in range(searchSize-1):
            y+=1
            x+=1
            product*=twoDimensionalArr[y][x]
        return product
    else:
        for i in range(searchSize-1):
            y-=1
            x+=1
            product*=twoDimensionalArr[y][x]
        return product

#Finally, we can iterate over our two dimensional array and call our functions as needed
#This can be drastically improved - parameters could be used to write all the functions as a single function with a parameter to determine direction
#Also, there must be a better way to handle indexing errors than the current method

max = 0
for y in range(17):
    for x in range(20):
        prod = upDown(gridAsList, y, x)
        if prod > max:
            max = prod

for y in range(20):
    for x in range(17):
        prod = leftRight(gridAsList, y, x)
        if prod > max:
            max = prod

for y in range(17):
    for x in range(17):
        prod = diagonal(gridAsList, y, x)
        if prod > max:
            max = prod

for y in range(3,20):
    for x in range(17):
        prod = diagonal(gridAsList, y, x, downRight = False)
        if prod > max:
            max = prod

print(max)