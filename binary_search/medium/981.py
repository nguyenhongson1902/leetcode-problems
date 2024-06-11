# Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/


class TimeMap:

    def __init__(self):
        self.d = {} # key: [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value, timestamp]]
        else:
            self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        else:
            # Binary search
            if timestamp < self.d[key][0][-1]:
                return ""

            # result = ["", 0]
            result = self.d[key][0]
            left, right = 0, len(self.d[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                timestamp_mid = self.d[key][mid][-1]

                if timestamp_mid == timestamp:
                    result = self.d[key][mid]
                    break
                elif timestamp_mid < timestamp:
                    result = self.d[key][mid]
                    left = mid + 1
                else:
                    right = mid - 1
            return result[0]
            # Time: O(logn), n=max(len(self.d[key]))


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)