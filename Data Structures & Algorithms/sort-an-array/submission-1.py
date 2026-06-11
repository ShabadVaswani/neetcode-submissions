class Solution:
    def merge(self, nums1, nums2):
        if len(nums1)>1:
            nums1 = self.merge(nums1[:len(nums1)//2], nums1[len(nums1)//2:])

        if len(nums2)>1:
            nums2 = self.merge(nums2[:len(nums2)//2], nums2[len(nums2)//2:])

        res = []
        while len(nums1) > 0 and len(nums2)>0:
            if nums1[0]>nums2[0]:
                res.append(nums2[0])
                nums2 = nums2[1:]
            else:
                res.append(nums1[0])
                nums1 = nums1[1:]
            
        while len(nums1) > 0 :
            
                res.append(nums1[0])
                nums1 = nums1[1:] 

        while  len(nums2)>0:
                res.append(nums2[0])
                nums2 = nums2[1:]
        return res


        
    def sortArray(self, nums: List[int]) -> List[int]:

        return self.merge(nums[:len(nums)//2], nums[len(nums)//2:])
        