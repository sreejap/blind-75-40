# remember - All the timestamps timestamp of set are strictly increasing.
# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        self.time_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        if len(self.time_map [key]) == 0:
            return ""

        if timestamp < self.time_map[key][0][0]:
            return ""
        
        left = 0
        right = len(self.time_map[key]) - 1

        while left <= right:
            mid = left + (right-left)//2
            if self.time_map[key][mid][0] <= timestamp:
                result = mid
                left = mid+1
            else:
                right = mid-1
        
        if result  == -1:
            return ""
        else:
            return self.time_map [key][result][1]        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
