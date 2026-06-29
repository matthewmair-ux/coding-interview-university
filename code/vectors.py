class Vector:
    def __init__(self, capacity=4):
        """
        Creates a new empty vector.

        capacity = Total amount of space available.
        size = Number of elements currently stored.
        data = Underlying array.
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        """
        Adds a new value to the end of the vector.
        Automatically resizes if the vector is full.
        """
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = value
        self.size += 1

    def resize(self):
        """
        Doubles the capacity of the vector.
        """
        self.capacity *= 2

        new_data = [None] * self.capacity

        # Copy old values into the new array
        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def get(self, index):
        """
        Returns the value at the given index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        return self.data[index]

    def set(self, index, value):
        """
        Changes the value at the given index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        self.data[index] = value

    def remove_last(self):
        """
        Removes the last element.
        """
        if self.size == 0:
            raise IndexError("Vector is empty")

        self.size -= 1
        self.data[self.size] = None

    def __len__(self):
        """
        Allows len(vector)
        """
        return self.size

    def __str__(self):
        """
        Allows print(vector)
        """
        return str(self.data[:self.size])