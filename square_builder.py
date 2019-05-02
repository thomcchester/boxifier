import line_builder as lb

#one of the nice things about looking at rectangles is that that I only need to find two parallel
#lines that have the start and end points and that can completely define the box.
def find_parallel_lines_of_same_length(image):
    line_finder = lb.line_maker(image)
    out_put_array = []
    for idx, i in enumerate(line_finder):
        for j in line_finder[idx+1:]:
            if lb.fuzzy_finder(i[1], j[1]) and lb.fuzzy_finder(i[2], j[2]):
                out_put_array.append([i,j])
    return out_put_array


#since the corner issue only makes the lines smaller I grabing the largest line it could be
def boxify(single_box):
    min_val = min([single_box[0][1], single_box[1][1]])
    max_val = max([single_box[0][2], single_box[1][2]])
    out_put_array = []
    for i in range(single_box[0][0], single_box[1][0]+1):
        for j in range(min_val, max_val):
            out_put_array.append([i,j])
    return out_put_array

def all_boxify(image):
    lines = find_parallel_lines_of_same_length(image)
    out_put_array = []
    for i in lines:
        out_put_array.append(boxify(i))
    return out_put_array
