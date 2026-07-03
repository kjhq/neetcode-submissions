class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped_nums = {}
        for i in nums:
            if i not in mapped_nums:
                mapped_nums[i] = 0
            
            mapped_nums[i] = mapped_nums[i] + 1
        
        output = []
        while len(output) < k:
            max_key = 0
            max_val = 0

            for i in mapped_nums.keys():
                if mapped_nums[i] > max_val:
                    max_key = i
                    max_val = mapped_nums[i]

            output.append(max_key)
            del mapped_nums[max_key]        
        return output