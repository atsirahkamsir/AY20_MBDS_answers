import os
from pathlib import Path
## Main Logic: ( From geeksforgeeks.org)
#1) Draw a horizontal line to the right of each point and extend it to infinity

#2) Count the number of times the line intersects with polygon edges.
#       Two given line segments  (p1, q1) and (p2, q2) intersect if and only if ONE of the following 2 condition is verified:
#           1. General Case:
#               – (p1, q1, p2) and (p1, q1, q2) have different orientations and
#               – (p2, q2, p1) and (p2, q2, q1) have different orientations.
#           2. Special Case
#               – (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and
#               – the x-projections of (p1, q1) and (p2, q2) intersect
#               – the y-projections of (p1, q1) and (p2, q2) intersect

#3) A point is inside the polygon if either count of intersections is odd or
#   point lies on an edge of polygon.  If none of the conditions is true, then 
#   point lies outside.

import re

INT_MAX = 10000


# Given three colinear points p, q, r, onSegment() checks if  
# point q lies on line segment pr    
def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
        (q[1] >= min(p[1], r[1]))):
        return True
         
    return False
 
# To find orientation of ordered triplet (p, q, r). 
# The function returns following values 
# 0 --> p, q and r are colinear 
# 1 --> Clockwise 
# 2 --> Counterclockwise 
def orientation(p:tuple, q:tuple, r:tuple) -> int:
     
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))
            
    if val == 0:
        return 0
    if val > 0:
        return 1 # Collinear
    else:
        return 2 # Clock or counterclock
  
# function that returns true if  the line segment 'p1q1' and 'p2q2' intersect. 
def doIntersect(p1, q1, p2, q2):
     
    # Find the four orientations needed for  
    # general and special cases 
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if (o1 != o2) and (o3 != o4):
        return True
     
    # Special Cases 
    # p1, q1 and p2 are colinear and 
    # p2 lies on segment p1q1 
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True
 
    # p1, q1 and p2 are colinear and 
    # q2 lies on segment p1q1 
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True
 
    # p2, q2 and p1 are colinear and 
    # p1 lies on segment p2q2 
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True
 
    # p2, q2 and q1 are colinear and 
    # q1 lies on segment p2q2 
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True
 
    return False


# main function
# Returns true if the point p lies inside the polygon[] with n vertices 
def is_inside_polygon(points:list, p:tuple) -> bool:
     
    n = len(points)
     
    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False
         
    # Create a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
    count = i = 0
     
    while True:
        next = (i + 1) % n
         
        # Check if the line segment from 'p' to  
        # 'extreme' intersects with the line  
        # segment from 'polygon[i]' to 'polygon[next]' 
        if (doIntersect(points[i],
                        points[next], 
                        p, extreme)):
                             
            # If the point 'p' is colinear with line  
            # segment 'i-next', then check if it lies  
            # on segment. If it lies, return true, otherwise false 
            if orientation(points[i], p, 
                           points[next]) == 0:
                return onSegment(points[i], p, 
                                 points[next])
                                  
            count += 1
             
        i = next
         
        if (i == 0):
            break
         
    # Return true if count is odd, false otherwise 
    return (count % 2 == 1)

# Driver program to test above functions:
#store input points
mat = []

f = open("input_question_6_polygon", "r")

polygon = []
for x in f.readlines():
    x = x.rstrip()
    array = []
    array = re.split(' ', x)
    desired_array = [int(numeric_string) for numeric_string in array]
    polygon.append(tuple(desired_array))

f.close()
f = open("input_question_6_points", "r")

points = []
for x in f.readlines():
    x = x.rstrip()
    array = []
    array = re.split(' ', x)
    desired_array = [int(numeric_string) for numeric_string in array]
    points.append(tuple(desired_array))

f.close()

if Path("output_question_6").is_file(): # if file exist
    os.remove("output_question_6")
    
f = open("output_question_6", "x")    
for point in points:
    if (is_inside_polygon(points = polygon, p = point)):
      x,y= point
      f.write(str(x)+" "+str(y) +" inside\n"  )
      
    else:
      x,y= point  
      f.write(str(x)+" "+str(y) +" outside\n"  )
f.close()       
        
      
        
