class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for i in nums:
            st.add(i);
        if len(st) != len(nums):
            return True
        return False
            