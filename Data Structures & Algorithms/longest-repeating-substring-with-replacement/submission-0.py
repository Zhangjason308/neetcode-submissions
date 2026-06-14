class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We're looking at a substring -> sliding window
        # it is not a fixed size
        """
        1. Create a left pointer for a starting letter
        2. While the right pointer is less than size of string
            a) while k > 0, move the right pointer, get the max of the current substring and the max substring
                - if the character at the right != left, then k -= 1
                - else just move the pointer right
            b) Once k = 0,continue if left = right, otherwise make left move right until its not equal to left anymore
        """
        count = {}
        l, res, maxf = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

