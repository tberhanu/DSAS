# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        def get_mid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        left_node = head
        mid = get_mid(head)
        right_node = mid.next
        mid.next = None # separating

        lefts = self.sortList(left_node)
        rights = self.sortList(right_node)

        # merging
        merged = root = ListNode()
        while lefts and rights:
            if lefts.val < rights.val:
                root.next = lefts
                root = root.next
                lefts = lefts.next
            else:
                root.next = rights
                root = root.next
                rights = rights.next
        if lefts:
            root.next = lefts
        if rights:
            root.next = rights
        return merged.next

