class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[nums[i]] = i
        
        for i in hash_map.keys():            
            if target - i in hash_map:
                return [hash_map[i], hash_map[target - i]]
        
        return [0, 1]
