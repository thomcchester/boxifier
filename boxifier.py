#!/usr/bin/env python

import sys

from matplotlib.image import imread
import square_builder as squab
import box_interaction as bxin
import response_checker as resch


#here is the final function
def check_all_boxes(image):
    box_list = squab.all_boxify(image)
    string_list = []
    for idx, i in enumerate(box_list):
        for j in box_list[idx+1:]:
            name_one = "box " + str(idx)
            name_two = "box " + str(idx+1)
            response_check = resch.ica_response_checker(bxin.intersect_contain_adjacent(i, j), name_one, name_two)
            string_list.append(response_check)
    return string_list

def outputter(image):
    print("NOTE: Boxes are zero indexed and ordered from top-down then left-right, by upper left most pixel of said box.")
    print(check_all_boxes(img))