class Solution(object):
    def reorderList(self, head):
        if not head:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while second:
            first_node = first.next
            second_node = second.next

            first.next = second
            second.next = first_node

            first = first_node
            second = second_node