class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[value],[timestamp]]
        else:
            self.dic[key][0].append(value)
            self.dic[key][1].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        values, times = self.dic[key]
        l, r = 0, len(times) - 1
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if times[m] <= timestamp:
                ans = m
                l = m + 1
            else:
                r = m - 1

        return "" if ans == -1 else values[ans]
        
