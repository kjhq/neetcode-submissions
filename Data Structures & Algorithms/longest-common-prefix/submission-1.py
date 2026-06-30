class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = len(strs[0])
        shortest_str_id = strs[0]

        for i in strs:
            if len(i) < shortest_str:
                shortest_str = len(i)
                shortest_str_id = i
        
        prefix_length = 0
        for i in range(0, shortest_str):
            for n in strs:
                if n[i] != shortest_str_id[i]:
                    return shortest_str_id[0:prefix_length]
                
            prefix_length = prefix_length + 1
        
        return shortest_str_id[0:prefix_length]
