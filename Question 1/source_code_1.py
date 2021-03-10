# Given a m x n matrix, we want to connect from top left corner (starting point, first row, first column) to
# bottom right corner (ending point, mth row, nth column). Only 2 operations are allowed: Right (R) or Down (D).
# Numbers that are passed through will be summed up. Given any summed number, you are required to find out the
# operations needed to get the number

# if m= 4. n=4
# 1   1   1   1
# 2   2   2   2
# 3   3   3   3
# 4   4   4   4
import os
from pathlib import Path

def hasPathSum(pos,s,path,mat):

    (rowpos,colpos) = pos
    ## get end point coordinates
    endrow = len(mat)-1
    endcol = len(mat[0])-1
    
    # Return true if we reach end of path and remaining sum = 0
    if pos == (endrow,endcol):
        subSum = s - mat[endrow][endcol]
        if (subSum == 0):
            return path
        else:
            # sum of that path is not equivalent to sum we need
            return 0
 
    else:
        ans = 0
 
        subSum = s - mat[rowpos][colpos]
 
        # Check both path possibilities 
        if rowpos < endrow:
            ans = ans or hasPathSum((rowpos+1,colpos),subSum,path + "D",mat)
        if colpos < endcol:
            ans = ans or hasPathSum((rowpos,colpos+1),subSum,path + "R",mat)
 
        return ans


m = 9 # row
n = 9 # col

mat =[]
## forming the data structure
rows, cols = (m,n)
for row in range(rows):
    new = []
    for col in range(cols):
        new.append(row+1)

    mat.append(new)


path = ""
requiredsum = 65
if Path("output_question_1").is_file(): # if file exist
    os.remove("output_question_1")

f = open("output_question_1", "x")
f.write(str(requiredsum) + " " + str(hasPathSum((0,0),requiredsum,path,mat)))
f.write("\n")
requiredsum = 72
f.write("\n" + str(requiredsum) + " " + str(hasPathSum((0,0),requiredsum,path,mat)))
requiredsum = 90
f.write("\n" + str(requiredsum) + " " + str(hasPathSum((0,0),requiredsum,path,mat)))
requiredsum = 110
f.write("\n" + str(requiredsum) + " " + str(hasPathSum((0,0),requiredsum,path,mat)))

f.close()


