class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0, len(numbers) - 1
        sum = numbers[i] + numbers[j]
        while sum != target:
            sum = numbers[i] + numbers[j]
            if sum == target:
                print('dnon',i,j)
                return [i+1,j+1]
            elif sum > target:
                j-=1
                print('no',i,j)
            elif sum < target:
                i +=1
                print('on',i,j)
        return [i+1,j+1]
        print('grbd')