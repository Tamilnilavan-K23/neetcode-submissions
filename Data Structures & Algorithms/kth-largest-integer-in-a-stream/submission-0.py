import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.K=k
        self.arr=nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()

        return self.arr[len(self.arr)-self.K]