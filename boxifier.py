#!/usr/bin/env python


from matplotlib.image import imread
import numpy as np





#based off of the fact that we are dealing with discrete values, adjacency is just a specific type of intersection, so
#I will be making a function to find adjacency but all adjacency would also trip intersections. Furthermore contained is
#a type of intersection as well where all of it is in the other.

def intersection(box_one, box_two):
    intersect = 0
    for i in box_one:
        if i in box_two:
            intersect = 1
            break
    if intersect == 1:
        return "boxes do intersect"
    else:
        return "boxes do not intersect"

def contained(box_one, box_two):
    contained = 1
    for i in box_one:
        if i not in box_two:
            contained = 0
            break
    if contained == 1:
        return "box one is contained by box two"
    else:
        return "box one is not contained by box two"


#with adjecency I am also making the assumption that directly next to each other does not count as adjecent but that
#they actually share the same side.

def adjecent(box_one,box_two):
    if intersection(box_one,box_two) == "boxes do not intersect":
        return "are not adjacent"
    else:
        intersecting_values = []
        for i in box_one:
            if i in box_two:
                intersecting_values.append(i)
        if np.unique(np.array([item[0] for item in intersecting_values])).size <= 2 or np.unique(np.array([item[1] for item in intersecting_values])).size <= 2:
            return "the two boxes are adjacent"
        else:
            return "the two boxes are not adjacent"

def check_all_three(box_one,box_two):
    check_array = [0,0,0,0]
    if intersection(box_one,box_two) == "boxes do intersect":
        check_array[0] = 1

    if contained(box_one,box_two):
        check_array[1] = 1

    elif contained(box_two,box_one):
        check_array[2] = 1

    if adjecent(box_one,box_two):
        check_array[3] = 1
    return check_array

#parse out what is actually happening.
def response_for_checks(check_array,name_one,name_two):
    if check_array[0] == 1:
        if check_array[1] == 1:
            return name_one + " is contained by " + name_two
        elif check_array[2] == 1:
            return name_two + " is contained by " + name_one
        else:
            return "there is an intersection between" + name_one + " and " + name_two
    else:
        return "there is no interaction between " + name_one + " and " + name_two

#here is the final function
def check_all_boxes_boolean(image):
    box_list = all_boxify(image)
    string_list = []
    for idx, i in enumerate(box_list):
        for j in box_list[idx+1:]:
            name_one = "box" + str(idx)
            name_two = "box" + str(idx+1)
            string_list.append(response_for_checks(check_all_three(i,j),name_one, name_two))
    return string_list


#To run agains actual image please put the path to the image file that you wish to use
#in for img below:

img = imread('./intersection.jpg')

print ['box0 is contained by box1', 'there is no interaction between box0 and box1', 'there is no interaction between box0 and box1', 'there is no interaction between box1 and box2', 'there is no interaction between box1 and box2', 'there is no interaction between box2 and box3'] == check_all_boxes_boolean(img)