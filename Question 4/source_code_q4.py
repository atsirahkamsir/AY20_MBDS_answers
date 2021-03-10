# using 4 connectivity and depth-first search algorithm
from pathlib import Path
import os
import re

#store input image 
mat = []

f = open("input_question_4", "r")

for x in f.readlines():
    x = x.rstrip()
    array = []
    array = re.split(r'\t+', x)
    desired_array = [int(numeric_string) for numeric_string in array]
    mat.append(desired_array)
  


# fucntion to get number of connected components
# outputs matrix of labeled components

def connect_components(image):
    ## dimensions
    n = len(image)   
    m = len(image[0])

    # 4-connectivity
    dx=[-1,0,1,0]
    dy=[0,-1,0,1];

    # Initialize an array that's the same size as image that needs to be processed
    # data Input: bool
    visited = []
    # retrieve all the connected componenets
    B = []
    # connected component label
    ID_counter = 1

    # initialise all variables. B with zeros. Visited with n*m(False)
    for i in range(n):
        array =[]
        array2=[]
        for j in range(m):
           array.append(0)
           array2.append(False)
        visited.append(array2)
        B.append(array)
            
    # connected component counter
    count=0
    # loop through binary image
    for i in range(n):
        for j in range(m):
            # check if index of that pixel[i][j] has been visited
            # if pixel =1 and not yet visited
            if(image[i][j]==1 and visited[i][j]== False):
                #connected component found
                count = count+1
                visited[i][j] = True
                # create a queue , push that index into queue
                Q = []
                Q.append((i,j))
                ## take note of the connected component and label it in the same index in B
                B[i][j] = count
                # while queue is not empty
                while( len(Q)!=0):
                    # pop of the first index in the queue
                    (x,y)=Q[0]
                    del Q[0]
                    # check all 4 neighbours
                    for dir in range(4):
                        newx = x + dx[dir]
                        newy = y + dy[dir]
                        # if neighbours are connected to current index
                        if(newx >= 0 and newx<n and newy>=0 and newy<m and image[newx][newy]==1 and visited[newx][newy]== False):
                            visited[newx][newy] = True
                            B[newx][newy] = count
                            Q.append((newx,newy))
    return B
print(connect_components(mat))

if Path("output_question_4").is_file(): # if file exist
    os.remove("output_question_4")
                        
f = open("output_question_4", "x")

for row in connect_components(mat):
    for j in row:
        f.write(str(j))
        f.write("\t")
    f.write("\n")    

f.close()
