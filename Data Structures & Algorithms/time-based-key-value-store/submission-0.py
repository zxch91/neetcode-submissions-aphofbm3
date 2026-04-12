class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        arr = self.dic[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
