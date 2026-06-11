class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        diff = [g-c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            print(sum(diff))
            return -1
        total = 0
        start = 0
        for index, value in enumerate(diff):
            total += value
            if total < 0:
                total = 0
                start = index+1
        
        return start
