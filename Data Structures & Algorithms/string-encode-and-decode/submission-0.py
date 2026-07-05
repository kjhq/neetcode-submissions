class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s):03d}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []

        while s != "":
            str_length = int(s[0:3])
            string = s[3:3+str_length]
            strs.append(string)
            s = s[3 + str_length:]
        
        return strs
