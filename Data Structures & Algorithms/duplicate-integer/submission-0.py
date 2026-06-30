class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        for i in nums:
            if not i in appeared:
                appeared[i] = 1
            else:
                return True
        
        return False