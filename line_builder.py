import image_simplifier as i_s
import numpy as np


#determine the location where ones are
def map_ones(image):
    rows=[]
    for idx, i in enumerate(i_s.asciiator(image)):
        for idn, j in enumerate(i):
            if j == 1:
                rows.append(np.array([idx,idn]))
    return np.array(rows)

#this is function used to find based off of one axis the possible crosses with non-zero values
def find_axis_info(image):
    last_val = -1
    temp_array = []
    for i in map_ones(image):
        if i[0] != last_val:
            last_val = i[0]
            temp_array.append([i[0],i[1]])
        else:
            temp_array[-1].append(i[1])
    return temp_array


#This looks for sections longer than one unit long given a row or column
def continous_ranges(list):
    start = -1
    end_at = -1
    temp_array = []
    for i in list:
        if start == -1:
            start = i
            end_at = i
        elif i == end_at + 1:
            end_at = i
        else:
            if end_at != -1 and end_at != start:
                temp_array.append([start,end_at])
            start = i
            end_at = start
    if end_at != start:
        temp_array.append([start,end_at])
    return temp_array


#this determines every line using continous_ranges
def find_lines(image):
    axis_info = find_axis_info(image)
    out_put_array = []
    for i in axis_info:
        ranges = continous_ranges(i[1:])
        if np.array(ranges).size > 0:
            out_put_array.append([i[0], ranges])
    return out_put_array

#this is used to fix and append and remove values that are warped on corner
def line_maker(image):
    potential_lines = find_lines(image)
    true_lines = []
    for i in potential_lines:
        for j in i[1]:
            if (j[-1] - j[0]) > 1:
                true_lines.append([i[0], j[0], j[-1]])
    return true_lines

#this is to handle the bad corners in the following function
def fuzzy_finder(a,b):
    if abs(a - b) < 2:
        return 1
    else:
        return 0
