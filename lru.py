
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.least_freq = 0
        self.key_cache_count = dict()
        self.lfu_count = dict()
    
    def _update(self, key, value):
        _, freq = self.key_cache_count[key]
        self.lfu_count[freq].remove(key)
        if len(self.lfu_count[self.least_freq]) == 0:
             self.least_freq += 1
        if freq+1 in self.lfu_count:         
            self.lfu_count[freq+1].append(key)
        else:
            self.lfu_count[freq+1] = [key]
        self.key_cache_count[key] = (value, freq+1)    

    def get(self, key: int) -> int:
        if key in self.key_cache_count:
            value, _ = self.key_cache_count[key]
            self._update(key, value)
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_cache_count:
            self._update(key, value)
        else:
            self.key_cache_count[key] = (value, 1)
            self.least_freq = 1 
            if self.least_freq in self.lfu_count:
                self.lfu_count[self.least_freq].append(key) 
            else:
                self.lfu_count[self.least_freq] = [key]
            if self.capacity == 0:
                removed = self.lfu_count[self.least_freq]
                self.key_cache_count.pop(removed[0])
            else:
                self.capacity -= 1
                
    def show(self):
        print( self.key_cache_count, self.least_freq, self.lfu_count,  self.capacity)
               
               
obj= LFUCache(2)
obj.put(1,4)
obj.show()
obj.put(2,5)
obj.show()
print(obj.get(1))
obj.put(3, 6)
obj.show()


