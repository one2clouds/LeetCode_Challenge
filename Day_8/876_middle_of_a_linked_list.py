# Loop runs O(N/2) ≈ O(N) , N is node of linked list, 
# As only two pointers are used, space complexity O(1)
def middle_of_link_list(head):
    fast = slow = head 

    # works on linkedlist of odd and even size. 
    # if odd size, after reaching last node, fast.next doesn't exist and it returns middle node. 
    # if even size, fast doesn't exist and function returns second node from two middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow










if __name__=="__main__":
    nums = [1,2,3, 4, 5]
    print(middle_of_link_list(nums))


