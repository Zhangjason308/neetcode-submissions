class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for char in s:
            if char not in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] = s_hash[char] + 1
        
        for char in t:
            if char not in t_hash:
                t_hash[char] = 1
            else:
                t_hash[char] = t_hash[char] + 1
        
        if s_hash == t_hash:
            return True
        return False


        