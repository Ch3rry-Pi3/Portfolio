class ListNode:
    """
    Definition for a singly linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into one sorted linked list.

        Args:
            l1 (ListNode): The head of the first sorted linked list.
            l2 (ListNode): The head of the second sorted linked list.

        Returns:
            ListNode: The head of the merged sorted linked list.
        """

        # Dummy node to serve as a placeholder for the new linked list
        prehead = ListNode(-1)

        # Pointer to construct the new linked list
        prev = prehead

        # Traverse both lists and merge nodes in sorted order
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next        # Move to the next node in l1
            else:
                prev.next = l2
                l2 = l2.next        # Move to the next node in l2
            prev = prev.next        # Move the pointer forward

        # Attach the remaining nodes from the non-empty list (if any)
        prev.next = l1 if l1 is not None else l2

        # The merged list starts from the next node of the dummy node
        return prehead.next


# Helper function to create a linked list from a list
def create_linked_list(lst):
    """
    Creates a linked list from a given list of values.

    Args:
        lst (List[int]): A list of integers.

    Returns:
        ListNode: The head of the linked list.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print a linked list
def print_linked_list(head):
    """
    Prints a linked list in a readable format.

    Args:
        head (ListNode): The head of the linked list.
    """
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))


def main():
    # Example test cases
    solution = Solution()

    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    merged_head = solution.mergeTwoLists(list1, list2)
    print("Merged Linked List:")
    print_linked_list(merged_head)


if __name__ == "__main__":
    main()
