import collections
from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        """
        Initializes the number container system.
        """
        # Map from number to a sorted set of indices
        self.number_to_indices = collections.defaultdict(SortedSet)
        # Map from index to number
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        """
        Inserts or replaces the number at the given index.
        """
        # If the index already has a number, remove it from its previous mapping
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]
            self.number_to_indices[previous_number].remove(index)
            if not self.number_to_indices[previous_number]:
                del self.number_to_indices[previous_number]
        
        # Update the mappings
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        """
        Returns the smallest index associated with the given number, or -1 if not found.
        """
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1

def main():
    """
    Demonstrates the functionality of the NumberContainers class.
    """
    obj = NumberContainers()
    print(obj.find(10))         # Output: -1 (no index filled with 10)
    obj.change(2, 10)
    obj.change(1, 10)
    obj.change(3, 10)
    obj.change(5, 10)
    print(obj.find(10))         # Output: 1 (smallest index filled with 10)
    obj.change(1, 20)
    print(obj.find(10))         # Output: 2 (smallest index filled with 10 after change)

if __name__ == "__main__":
    main()
