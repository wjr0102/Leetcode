class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("Get %d"%key)
        if self.cache.__contains__(key):
            self.stack.remove(key)
            self.stack.append(key)
            # print(self.stack)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print("Put %d"%key)
        if (len(self.cache) == self.capacity) and (not self.cache.__contains__(key)):
            delete_key = self.stack.pop(0)
            del(self.cache[delete_key])

        self.cache[key] = value
        if key not in self.stack:
            self.stack.append(key)
        else:
            self.stack.remove(key)
            self.stack.append(key)
        # print(self.stack)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)