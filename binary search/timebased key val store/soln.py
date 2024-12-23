class TimeMap:

    def __init__(self):
        self.obj = {} # {key: [[timetamp val], [timestamp val]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key in self.obj):
            self.obj[key].append([timestamp, value])
        else:
            self.obj[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.obj): return ""
        # bin search
        l, r = 0, len(self.obj[key]) - 1
        maxSeen = -1
        while (l <= r):
            # try to find a timestamp in self.obj.key <= timestamp
            mid = l + (r - l) // 2
            if (self.obj[key][mid][0] == timestamp):
                return self.obj[key][mid][1]
            elif (self.obj[key][mid][0] < timestamp):
                maxSeen = max(maxSeen, mid)
                l = mid + 1
            else:
                r = mid - 1
        if (maxSeen == -1): return ""
        return self.obj[key][maxSeen][1]
