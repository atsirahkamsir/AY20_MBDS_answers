import re
import math
import os
from pathlib import Path
# 2-dimension
# part a
L1 = 4 #length
L2 = 3 #height

## coordinates <-- index ( 2D) :
# index = x1 + ( x2 * length)
#
#
## Inverse:
## index<-- coordinates
# x1 = index % length
# x2 = index /length

## part b
def coordinates_to_index(x1,x2,L1,L2):

    return x1 + ( x2 * L1)

#[Input file1: input coordinates 7 1.txt (tab-seperated file: each column corresponds to a dimension)]
#[Output file1: output index 7 1.txt (write the calculated index values)]

def index_to_coordinates(I,L1,L2):

    x1 = I % L1
    x2 = math.floor(I / L1)

    return (x1,x2)



mat = []
l1= 50
l2 = 57

with open("input_coordinates_7_1.txt", "r") as f:
    next(f)
    for x in f.readlines():
        x = x.rstrip()
        array = []
        array = re.split(r'\t+',x)
        desired_array = [int(numeric_string) for numeric_string in array]
        mat.append(desired_array)
f.close()


if Path("output_index_7_1.txt").is_file(): # if file exist
    os.remove("output_index_7_1.txt")
f = open("output_index_7_1.txt","x")
f.write("index"+ "\n")
for row in mat:
    f.write(str(coordinates_to_index(row[0],row[1],l1,l2)))
    f.write("\n")
f.close()


index=[]

with open("input_index_7_1.txt", "r") as f:
    next(f)
    for x in f.readlines():
        x = x.rstrip()
        x=int(x)
        index.append(x)
f.close()

if Path("output_coordinate_7_1.txt").is_file(): # if file exist
    os.remove("output_coordinate_7_1.txt")
f = open("output_coordinate_7_1.txt","x")
f.write('x1'+ "\t" + 'x2'+ "\n")
for ind in index:
    (x1,x2) = index_to_coordinates(ind,l1,l2)
    f.write(str(x1)+ "\t" + str(x2))
    f.write("\n")
f.close()

    
