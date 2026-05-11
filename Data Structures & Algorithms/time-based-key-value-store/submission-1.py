
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, {})[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""

        res = ""

        keys = list(self.store[key].keys())                                                                 
        low, high = 0, len(keys) - 1                                                                     
                                                                                                            
        while low <= high:                                                                                  
            mid = (low + high) // 2                                                                         
            if keys[mid] == timestamp:                                                                      
                return self.store[key][keys[mid]]                                                           
            elif keys[mid] < timestamp:                                                                     
                res = self.store[key][keys[mid]]                                                            
                low = mid + 1                                                                               
            else:                                                                                           
                high = mid - 1                                                                              
                                                                                                            
        return res


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))
