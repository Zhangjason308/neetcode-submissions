class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        l, r, max_c, res = 0,0, 0, 0

        while r < len(s):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_c = max(max_c, char_count[s[r]])
            while (r - l + 1) - max_c > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


