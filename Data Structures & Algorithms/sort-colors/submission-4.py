class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for i in nums:
            colors[i] = colors[i] + 1
        
        starting = 0
        for i in range(0, len(colors)):
            j = starting + colors[i]
            nums[starting:j] = [i] * colors[i]
            starting = j
        
        return nums