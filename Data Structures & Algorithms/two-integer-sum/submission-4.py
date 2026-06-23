class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i,j in enumerate(nums):
            d[j].append(i)
        print(d)

        for i,j in enumerate(nums):
            if len(d[target-j]) > 0:
                if i == d[target-j][0]:
                    if len(d[target-j]) > 1:
                        return [i, d[target-j][1]]
                    else:
                        continue
                return [i, d[target-j][0]]