class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = sorted(list(s))
        t_arr = sorted(list(t))
        s_hash = {}
        t_hash = {}
        for i in s_arr:
            if i not in s_hash.keys():
                s_hash[i] = 1
            else: 
                s_hash[i] = s_hash[i] + 1
        for i in t_arr:
            if i not in t_hash.keys():
                t_hash[i] = 1
            else: 
                t_hash[i] = t_hash[i] + 1
        if t_hash != s_hash:
            return False
        return True