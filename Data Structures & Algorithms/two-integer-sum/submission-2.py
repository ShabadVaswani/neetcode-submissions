class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dict1 = {}
        k = 0;
        for i in nums:
            
            if target - i in dict1:
                return [dict1[target - i], k]
            else:
                dict1[i] = k;
                k+=1;


        return [j,k]
