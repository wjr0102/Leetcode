class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.frequency = {}

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.cache:
            self.change_freq(key)
            return self.cache[key]
        else:
            return -1
    
    def change_freq(self,key:int) -> None:
        freq = self.frequency[key]+1
        del self.frequency[key]
        self.frequency[key] = freq
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache:
            if self.size<self.capacity:
                self.size += 1
            else:
                feq = 1000
                k = None
                for item in self.frequency:
                    if self.frequency[item] < feq:
                        feq = self.frequency[item]
                        k = item
                if k:
                    del self.frequency[k]
                    del self.cache[k]
            self.frequency[key] = 0
        self.change_freq(key)
        self.cache[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)