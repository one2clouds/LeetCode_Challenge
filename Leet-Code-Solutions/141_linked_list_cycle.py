# at worst case, where end pointer points to 1st location, 
# algorithm executes for n steps at that time
# hence, time complexity of slow & fast pointer meet will be O(N). 
# SPace COmplexity = O(1) as we only need to save fast and slow pointers


def has_cycle(head):

    slow = fast = head 

    while fast and fast.next :
        slow = slow.next 
        fast = fast.next.next 

        # if the linked_list didn't have cycle, fast and fast.next 
        # would be none at one time, and it breaks out of loop and 
        # returns False.

        if slow == fast:
            # print(slow.val)
            # print(fast.val)
            return True 
        
    return False 



# Definition of singly linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



if __name__=="__main__":
    head = ListNode(1)
    current = head
    cycle_node = None
    for val in [2,3,4,7]:
        current.next = ListNode(val)
        current = current.next

        if val == 2:
            cycle_node = current
    
    current.next = cycle_node
            
    print(has_cycle(head))






