class MRUQueue:
    """
    A queue-like data structure that moves the most recently used element 
    to the end of the queue when accessed.

    Methods:
    - __init__(n): Initialises the queue with elements [1, 2, ..., n].
    - fetch(k): Moves the k-th (1-indexed) element to the end of the queue and returns it.
    """

    def __init__(self, n: int):
        """
        Initialises the MRUQueue with n elements [1, 2, ..., n].

        :param n: Number of elements in the queue.
        """
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        """
        Fetches the k-th element (1-indexed), moves it to the end of the queue, and returns it.

        :param k: The position (1-based index) of the element to fetch.
        :return: The fetched element.
        """
        value = self.queue.pop(k - 1)       # Remove the k-th element (adjusting for 0-indexing)
        self.queue.append(value)            # Move it to the end of the queue
        return value


def main():
    """
    Demonstrates the MRUQueue class with an example.
    """
    # Initialise the queue with n = 8
    mru_queue = MRUQueue(8)

    # Test fetch operations
    queries = [3, 5, 2, 8]
    results = [mru_queue.fetch(k) for k in queries]

    # Display results
    print("Fetch results:", results)


if __name__ == "__main__":
    main()
