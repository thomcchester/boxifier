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
