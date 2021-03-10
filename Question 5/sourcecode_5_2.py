# perform task using greedy algorithm
from pathlib import Path
import os

beads= [['R',139],['B',1451],['Y',457],['W',1072],['G',977]]
# sort the beads, with largest colour first
beads.sort(key=lambda l: l[1], reverse=True)
mat = []
L= 64

# pop the first 2 largest colour from the stack of tuples
sequence = beads[:2]
beads=beads[2:5]


for row in range(L):
    new = []
    for col in range(L):
        j = col % 2 # determine if row is even or odd to determine sequence of placing each bead of diff colour
        if len(sequence) == 1: # if left with only 1 colour
            new.append(sequence[0][0])
            sequence[0][1] = sequence[0][1]-1
            continue
        else:
            #based on if row is even/odd, place beads according to colour in sequence array
            new.append(sequence[j][0])
            sequence[j][1] = sequence[j][1] -1 # minus off
            # if beads of that colour has run out, replace with a new colour, in that same position in sequence
            if sequence[j][1] ==0 and len(beads)!=0:
                sequence[j] = beads[0]
                del beads[0]
    mat.append(new)
    tmp = sequence[0]
    sequence[0]= sequence[1]
    sequence[1]=tmp

## check penalty
# penalty should be 0
pen = 0
    
for row in range(L):
    for col in range(L):
        if col < L-1:
            if mat[row][col] == mat[row][col+1]:
                pen = pen+1
                
        if row < L-1:
            if mat[row][col] == mat[row+1][col]:
                pen = pen + 1
                
print(pen)
if Path("output_question_5_2").is_file(): # if file exist
    os.remove("output_question_5_2")

f = open("output_question_5_2", "x")
for row in range(L):
    for col in range(L):
        
        f.write(mat[row][col])
        f.write(' ')
        
    f.write("\n")

f.close()
