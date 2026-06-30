# 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_length = len(nums) * 2
        for i in nums:
            if len(nums) == ans_length:
                break
            nums.append(i)
        
        return nums