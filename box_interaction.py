import numpy as np

#based off of the fact that we are dealing with discrete values, adjacency is just a specific type of intersection, so
#I will be making a function to find adjacency but all adjacency would also trip intersections. Furthermore contained is
#a type of intersection as well where all of it is in the other.


def intersect_contain_adjacent(box_one, box_two):
    intersect = 0
    contained = 1
    second_contained = 1
    continue_checking_intersect = 1
    continue_checking_contained = 1
    for i in box_one:
        if continue_checking_intersect == 1 and i in box_two:
            intersect = 1
            continue_checking_intersect = 0
        elif continue_checking_contained == 1 and i not in box_two:
            contained = 0
        elif continue_checking_contained == continue_checking_intersect == 0:
            break
    if intersect == 0:
        adjacent = 0
    else:
        intersecting_values = []
        for i in box_one:
            if i in box_two:
                intersecting_values.append(i)
        if np.unique(np.array([item[0] for item in intersecting_values])).size <= 2 or np.unique(np.array([item[1] for item in intersecting_values])).size <= 2:
            adjacent = 1
        else:
            adjacent = 0
    for i in box_two:
        if i not in box_one:
            second_contained = 0
            break

    return [intersect, contained, second_contained, adjacent]

