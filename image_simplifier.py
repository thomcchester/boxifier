import numpy as np
## This file is just for simplifying the image into constiuent parts


#This is a function to flatten value to 0 or 1 for array. I also flipped the values since I wanted to use one as black
#and 0 as white, mainly as a preference but also because ones look like lines. The idea is simple, and a bit of an over
#simplification, but I am going to say that if the hue amplitude is over half way it is white, and if it is under half
#way it is black. I might come back to this to allow for differences in color and what not.
def flattenator(value_list):
    if value_list[1] < 128:
        return 1
    else:
        return 0

# asciiator is function used to turn the entirety of the array into ascii-art 0 and 1 of the image for later processing
def asciiator(image):
    image_list = []
    for i in image:
        row_list = []
        for m in i:
            row_list.append(flattenator(m))
        image_list.append(row_list)
    return np.array(image_list)

