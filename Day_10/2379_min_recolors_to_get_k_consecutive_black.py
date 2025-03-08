# trivial and bruteforce solution
# TIme COmplexity : O(N*k), O(N) for the N strings on while loop, O(k) for k substrings 
def minimum_recolors_for_black(my_string, k):
    left, right = 0, 0
    min_num_color_change = k 

    # basically we increment left=0 from start until we are at end of string
    # we also substract k because, if string is of length 5 and we are at length 4 and k is 3 then, we won't get 3 strings from (4 to 5)
    while left <= len(my_string)-k:
        num_color_change = 0 

        # as we progress from start to end of string, we see at each window from (left to left +k) in that if we 
        # see letter W then change it, then we take min of  number of change required to each sliding window 
        for right in range(left, left+k):
            if my_string[right] == "W":
                num_color_change +=1 

        min_num_color_change = min(min_num_color_change, num_color_change)
        left += 1
    
    return min_num_color_change


if __name__=="__main__":
    my_string = "WBBWWBBWBW"
    k = 7
    print(minimum_recolors_for_black(my_string, k))

    my_string = "WBWBBBW"
    k = 2
    print(minimum_recolors_for_black(my_string, k))