
class LFUCache:

    def __init__(self, capacity: int):
        self.data = dict()
        self.capacity = capacity
        self.new_coming = 0

    def get(self, key: int) -> int:
        try:
            v = self.data[str(key)]
            v[1] = v[1]+1
            self.data[str(key)] = v
            ret = self.data[str(key)][0]
            return ret
        except:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.data.__len__() >= self.capacity:
            useless_v = [0,-1e100,1e100]
            useless_k = None
            for k,v in self.data.items():
                if v[1] > useless_v[1]:
                    useless_k = k
                    useless_v = v
                elif v[1] == useless_v[1]:
                    if v[2] < useless_v[2]:
                        useless_k = k
                        useless_v = v
            self.data.pop(useless_k)
            self.new_coming += 1
            self.data[str(key)] = [value, 1, self.new_coming]
        else:
            self.new_coming += 1
            self.data[str(key)] = [value, 1, self.new_coming]

if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      
    cache.put(3, 3)    
    cache.get(2)    
    cache.get(3)   
    cache.put(4, 4)    
    cache.get(1)      
    cache.get(3)       
    cache.get(4)


