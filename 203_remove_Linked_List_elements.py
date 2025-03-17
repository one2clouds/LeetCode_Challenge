# Time : O(N) as we have to iterate to whole linked list until end
# Space : O(1) as only pointers dummy head & current node is needed...
# edge cases : empty linked list, multiple nodes in row need deleting, head node needs deleting, final node needs deleting, all nodes need deleting.....

def remove_linked_list_elements(head, val):

    dummy_head = ListNode(-1)
    dummy_head.next = head 

     # a dummy head for edge case, if we want to remove 1st element, then current_node.next will remove first element too, if we hadn't have dummy, then we can just delete current_node.next only....and not 1st node...

    current_node = dummy_head

    while current_node.next != None:
        # checks if current_nude + 1 is equal to val, and if it is then shift the pointer to node after that. 
        # even works for last pointer as checking for last node is dene in l-1 step already with this code : (if current_node.next.val):
        if current_node.next.val == val:
            current_node.next = current_node.next.next 
        else:
            current_node = current_node.next

    return dummy_head.next


# Definition of singly linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



if __name__=="__main__":
    head = ListNode(1)
    current = head

    for val in [4, 2,3,4,7, 4, 2, 6, 4]:
        current.next = ListNode(val)
        current = current.next
            
    removed_elements_list = remove_linked_list_elements(head, val=4)

    result = []
    while removed_elements_list != None:
        result.append(removed_elements_list.val)
        removed_elements_list = removed_elements_list.next

    print(result)








