# Definition for singly-linked list node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to build a linked list from a Python list
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to convert a linked list back to a Python list for easy printing
def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # Store the next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev forward
            curr = next_temp       # Move curr forward
            
        return prev


# Test cases
solution = Solution()

# Test Case 1: Standard multi-node linked list [1, 2, 3, 4, 5]
head1 = build_linked_list([1, 2, 3, 4, 5])
reversed1 = solution.reverseList(head1)
print("Test Case 1:", print_linked_list(reversed1))  
# Expected output: [5, 4, 3, 2, 1]

# Test Case 2: Two elements [1, 2]
head2 = build_linked_list([1, 2])
reversed2 = solution.reverseList(head2)
print("Test Case 2:", print_linked_list(reversed2))  
# Expected output: [2, 1]

# Test Case 3: Empty list []
head3 = build_linked_list([])
reversed3 = solution.reverseList(head3)
print("Test Case 3:", print_linked_list(reversed3))  
# Expected output: []

# Test Case 4: Single element list [1]
head4 = build_linked_list([1])
reversed4 = solution.reverseList(head4)
print("Test Case 4:", print_linked_list(reversed4))  
# Expected output: [1]