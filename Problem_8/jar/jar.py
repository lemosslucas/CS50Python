class Jar:
    def __init__(self, capacity=12):
        # initialize the variables
        if capacity < 0 :
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # return the cookies quant
        return  self.size * "🍪"

    def deposit(self, n):
        # Verify if is valid the quant for a jar capacity
        if n > self.capacity:
            raise ValueError("Exceeds jar capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity")
        # remove the cookies
        self._size += n

    def withdraw(self, n):
        # verify if has enough cookies
        if self.size < n:
            raise ValueError("Not enough cookies for remove")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(2)
jar.withdraw(1)
print(jar)
