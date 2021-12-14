def cafe_order_checker(take_out, dine_in, served):
    # 1. check the if the current index for both lists to see if 
    #    they match the current index for the served list
    # 2. if they do, make a recursive call removing the matching indicies

    # base case
    # if len(served) == 0:
    #     return True

    # if len(take_out) and take_out[0] == served[0]:
    #     cafe_order_checker(take_out[1:], dine_in, served[1:])
    # elif len(dine_in) and dine_in[0] == served[0]:
    #     cafe_order_checker(take_out, dine_in[1:], served[1:])
    # else:
    #     return False

    # end recursive solution

    take_out_index = 0
    dine_in_index = 0
    served_index = 0
    take_out_index_valid = take_out_index < len(take_out)
    # unnecessary to check this
    # dine_in_index_valid = dine_in_index < len(dine_in) 

    while served_index < len(served):
        if take_out_index_valid and take_out[take_out_index] == served[served_index]:
            take_out_index += 1
        else: # assumes input is valid
            dine_in_index += 1
        
        take_out_index_valid = take_out_index < len(take_out)
        served_index += 1

    return take_out_index == len(take_out) and dine_in_index == len(dine_in)

# take_out = [1, 3, 5]
# dine_in = [2, 4, 6]
# served = [1, 2, 4, 6, 5, 3]

take_out = [17, 8, 24]
dine_in =[12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

print(cafe_order_checker(take_out, dine_in, served))