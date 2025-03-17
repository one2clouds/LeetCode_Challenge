def alternating_groups(colors, k):
    left = 0
    output = 0

    # start from first element to check 0th and 1st elements are same. Then, 
    for right in range(1, len(colors)+k-1):
        # because if right's previous term and current term are same, then even though 
        # other are alternating, because of these two values, overall subarray would never be alternating....
        if colors[right % len(colors)] == colors[(right-1)% len(colors)]:     # mod by len(colors) because of circular array for valid node indexing
            left = right     

        # if the subarray if greater than k, remove 1st element and add new element as with 1st element has already been checked
        if right - left + 1 > k:
            left += 1
        
        # checking for upto Kth element, and as already alternating[verified by if condition : as if not indexing left=right], increase output by 1
        if right-left +1 == k:
            output += 1

    return output


if __name__=="__main__":
    colors = [0,1,0,1,0]
    k = 3
    print(alternating_groups(colors, k))