from typing import Optional

# Definition for singly-linked list.
class ListNode:
    """
    Definition for a singly linked list node.
    Each node contains an integer value and a reference to the next node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    This class provides an implementation to find the middle of a singly linked list
    using the two-pointer technique.
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle of a singly linked list using the two-pointer technique.

        :param head: The head node of the linked list
        :return: The middle node of the linked list
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


def main():
    """
    Demonstrates finding the middle node of a linked list.
    """
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solver = Solution()
    middle = solver.middleNode(head)

    # Print the middle node value
    print(f"Middle Node Value: {middle.val}")


if __name__ == "__main__":
    main()