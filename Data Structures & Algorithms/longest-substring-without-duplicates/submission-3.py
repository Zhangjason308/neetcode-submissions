class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        unique = set()

        l, r = 0, 0

    
        while r < len(s):
            # Move right pointer
            if s[r] not in unique:
                unique.add(s[r])
                max_count = max(max_count, r - l + 1)

                r += 1
            # Move left pointer
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
        return max_count          
            
       