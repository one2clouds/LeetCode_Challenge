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

# Definition of singly linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




if __name__=="__main__":
    head = ListNode(1)
    current = head
    for val in [2,3,4,7]:
        current.next = ListNode(val)
        current = current.next

    middle_node = middle_of_link_list(head)


    result = []
    while middle_node:
        result.append(middle_node.val)
        middle_node = middle_node.next
    print(result)


