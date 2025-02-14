class ProductOfNumbers:
    """
    A class that maintains a stream of integers and allows retrieving the product 
    of the last k elements in the stream efficiently.
    """

    def __init__(self):
        """
        Initialises an empty stream with a prefix product list.
        The list starts with 1 to handle multiplication logic seamlessly.
        """
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        """
        Appends an integer to the stream.
        
        If the number is 0, the entire prefix product list is reset, 
        as multiplication with 0 invalidates previous values.

        Args:
            num (int): The number to be added to the stream.
        """
        if num == 0:
            # Reset on zero since it invalidates all previous products.
            self.prefix_product = [1]
            self.size = 0
        else:
            # Append the cumulative product of the current number with the last product.
            self.prefix_product.append(self.prefix_product[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        """
        Retrieves the product of the last k numbers in the current list.

        Args:
            k (int): The number of last elements to consider for the product.

        Returns:
            int: The product of the last k elements or 0 if k exceeds the list size.
        """
        if k > self.size:
            return 0  # If k is greater than available numbers, return 0.

        # Compute product efficiently using division of prefix products.
        return self.prefix_product[-1] // self.prefix_product[-k - 1]


def main():
    """Example usage of the ProductOfNumbers class."""
    product_of_numbers = ProductOfNumbers()

    # Example sequence of operations
    product_of_numbers.add(3)
    product_of_numbers.add(2)
    product_of_numbers.add(0)
    product_of_numbers.add(5)
    product_of_numbers.add(4)
    
    print(product_of_numbers.getProduct(2))         # Expected output: 20
    print(product_of_numbers.getProduct(3))         # Expected output: 40
    print(product_of_numbers.getProduct(4))         # Expected output: 0
    
    product_of_numbers.add(8)
    print(product_of_numbers.getProduct(2))  # Expected output: 32


if __name__ == "__main__":
    main()
