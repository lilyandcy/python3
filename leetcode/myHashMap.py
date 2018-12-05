class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = []
        self.hashKey = {}


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashKey:
            index = self.hashKey[key]
            self.table[index] = (key, value)
        else:
            self.table.append((key, value))
            self.hashKey[key] = len(self.table) - 1


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key not in self.hashKey:
            return -1
        else:
            index = self.hashKey[key]
            return self.table[index][1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.hashKey:
            index = self.hashKey[key]
            for i in range(index+1, len(self.table)):
                self.hashKey[self.table[i][0]] -= 1
            del self.hashKey[key]
            self.table.pop(index)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)