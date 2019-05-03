#parse out what is actually happening.
def ica_response_checker(array, name_one, name_two):
    if array[0] == 0:
        return "there is no interaction " + name_one + " and" + name_two
    else:
        if array[1] == 1:
            return name_one + " is contained by " + name_two
        elif array[2] == 1:
            return name_two + " is contained by " + name_one
        elif array[3] == 1:
            return name_two + " is adjacent to" + name_one
        else:
            return "there is an intersection between" + name_one + " and " + name_two


