'''
time-based key-value d.s. that supports
    storing multiple values for same key at specific time stamps
    retrieving the key's value at a specified timestamp

implement TimeMap class

set -> stores key "key" with "value" at given "timestamp"
{"alice": {1:"happy", 3: "sad"}}

get -> returns most recent value of key if set previously called on it and the most recent ts


'''

class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = {}
        self.storage[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        timestamps = sorted(self.storage[key].keys())
        l = 0
        r = len(timestamps) - 1
        res = ""
        print(self.storage[key])
        print(r)
        while l <= r:
            m = (l + r) // 2
            if timestamps[m] == timestamp and timestamps[m] in self.storage[key]:
                return self.storage[key][timestamps[m]]
            elif timestamps[m] < timestamp:
                if timestamps[m] in self.storage[key]:
                    res = self.storage[key][timestamps[m]]
                l = m + 1
            else:
                r = m - 1
        return res
    
