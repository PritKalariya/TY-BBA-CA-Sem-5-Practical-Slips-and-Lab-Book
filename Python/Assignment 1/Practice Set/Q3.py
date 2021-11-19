"""
Write python script to accept the x and y coordinate of a point and find the quadrant in which the point lies.

2. (-+)  |  1. (++)
3. (--)  |  4. (+-)

"""

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "First Quadrant"
    elif x < 0 and y > 0:
        return "Second Quadrant"
    elif x < 0 and y < 0:
        return "Third Quadrant"
    elif x > 0 and y < 0:
        return "Fourth Quadrant"
    else:
        return "At Origin"

point_x = int(input("Enter the value of point X: "))
point_y = int(input("Enter the value of point Y: "))

quadrant = find_quadrant(point_x, point_y)
print(quadrant)