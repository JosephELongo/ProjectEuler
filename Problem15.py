#Until you are at an edge, you can make two more paths at every point: you can go down or you can go right
#Therefore, we can make a Node class that stores where we currently are in terms of x and y: the starting point will be (0,0) and the ending point will be (20,20)
#If x or y is equal to 20, we increment a counter and remove the node from a list to check -> it is a unique path since any remaining moves will only be incrementing
#the coordinate that is not already equal to 20
#If x or y is not equal to 20, we need to make two new nodes with coords of (x+1, y) and (x, y+1)
#The previously mentioned list to check will have these two nodes added and this process will repeat until the list to check is empty
#These steps are done below in the while loop with the first node in the list being checked to see if it is on a right or bottom edge
#However, while this brute force method works for small grids, it does not work for larger grids
#Therefore, let's see what the solutions are for some smaller sized grids
#With n = 1, there are 2 paths, with n = 2, there are 6 paths, with n = 3, there are 20 paths, with n = 4, there are 70 paths
#With n = 5, there are 252 paths, with n = 6, there are 924 paths and so on
#Using the name of the problem (Lattice Paths) and looking at these numbers, it turns out all of these numbers appear in the middle of the rows of Pascal's triangle
#For example, 2 appears on the second row in the first column (if you start counting from 0)
#Then, 6 appears on the fourth row in the second column
#20 appears on the sixth row in the third column and so on
#Therefore, the pattern seems to be that the answer to the Lattice Paths question with grid n*n is the number on Pascal's triangle at row n*2 and column n
#Using the forumlua for a location on Pascal's triangle of r!/c!*(r-c)! where r is the row number and c is the column number (aka n choose k but with r's and c's),
#We can substitue in n*2!/n!*(n*2-n)! = 40!/20!*(40-20)! = 40!/20!**2
#This turns out to be the solution! However, we never proved that this method works -> a more programming oriented approach could have used memoization and a 
#more rigorous solution could have shown how we end up with a problem of combinatorics - perhaps a challenge for a future problem!

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def atEdge(self, n):
        """Determines whether or not you are at the right or bottom edge of the grid with size n * n"""
        if self.x == n or self.y == n:
            return True
        else:
            return False


if __name__ == "__main__":
    listOfNodes = [Node(0,0)]
    counter = 0
    n = 2
    while len(listOfNodes) > 0:
        currentNode = listOfNodes[0]
        if currentNode.atEdge(n):
            counter+=1
            listOfNodes.pop(0)
        else:
            listOfNodes.append(Node(currentNode.x+1, currentNode.y))
            listOfNodes.append(Node(currentNode.x, currentNode.y+1))
            listOfNodes.pop(0)
    print(counter)
    fortyFactorial = 1
    twentyFactorial = 1
    for i in range(1,41):
        fortyFactorial*= i
    for i in range(1, 21):
        twentyFactorial*= i
    print(fortyFactorial/(twentyFactorial)**2)

