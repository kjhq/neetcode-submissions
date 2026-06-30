class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0

        for i in nums:
            if votes == 0:
                candidate = i
            
            if i == candidate:
                votes = votes + 1
            else:
                votes = votes - 1
    
        votes = 0
        length = len(nums)
        for i in nums:
            if i == candidate:
                votes = votes +1
        
        if length / 2 > votes:
            return -1
        
        return candidate