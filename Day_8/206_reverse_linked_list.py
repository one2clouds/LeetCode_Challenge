
def reverse_linked_list(head):

    prev_P = None 
    current_P = head

    # if 1->2->3->4->7 is our LL then, 
    # in 1st iteration next_P = 2, current_P.next=None, prev_P = 1, current_P = 2, 
    # in 2nd iteration, next_P = 3, current_P.next=1, prev_P = 2, current_P = 3, 
    # in 3rd, next_P = 4, current_P.next=2, prev_P = 3, current_P = 4
    # in 4th , next_P = 7, current_P.next=3, prev_P = 4, current_P = 7
    # in 4th , next_P = 7, current_P.next=3, prev_P = 4, current_P = 7
    # in 5th, next_P = None, current_P.next=4, prev_P = 7, current_P = None, and then loop stops, then head = prev_P = 7

    while current_P != None:
        next_P = current_P.next

        current_P.next = prev_P

        prev_P = current_P

        current_P = next_P

    
    head = prev_P

    return head 



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
            
    reversed_LL = reverse_linked_list(head)


    result = []
    while reversed_LL!=None:
        result.append(reversed_LL.val)
        reversed_LL=reversed_LL.next

    print(result)






