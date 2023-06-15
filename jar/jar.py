class Jar:
    # initializing capacity as default value of 12
    def __init__(self, capacity=12):
        #checking the capacity for a negative number
        if capacity > 0:
            self.capacity = capacity
        else:
            raise ValueError("Capacity of cookies can't be negative number")
        # defining size variable
        self.size = 0

    def __str__(self):
        # returning the amount of our cookies after operation with a cookie emoji
        return self.size*"🍪"

    def deposit(self, n):
        # deposit functio, checking for above capacity avaliable cookies
        if self.capacity < n:
            raise ValueError("You are trying to deposit cookies above capacity")
        if self.size + n > self.capacity:
            raise ValueError("You are trying to deposit cookies above capacity")
        else:
            self.size += n
            return self.size

    def withdraw(self, n):
        # Withdraw function, checking for exteended cookies in the jar, returning and updating size value
        if self.size < n:
            raise ValueError("There are not that many cookies in the jar")
        else:
            self.size -= n
            return self.size

# getter and setter functions defined below for capacity
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        self._capacity = capacity

# getter and setter functions defined below for size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        self._size = size