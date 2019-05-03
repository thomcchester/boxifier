#!/usr/bin/env python

import sys

from matplotlib.image import imread
import square_builder as squab
import box_interaction as bxin
import response_checker as resch

img = imread(sys.argv[1])

#here is the final function
def check_all_boxes(image):
    box_list = squab.all_boxify(image)
    string_list = []
    for idx, i in enumerate(box_list):
        for j in box_list[idx+1:]:
            name_one = "box " + str(idx)
            name_two = "box " + str(idx+1)
            string_list.append(resch.response_for_checks(bxin.check_all_three(i,j),name_one, name_two))
    return string_list

print check_all_boxes(img)