class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # I see subset, I immediately think of a window
        # use a two-pointer/sliding window approach
        # Find the longest substring without duplicates
        # Have one pointer for left, right
        # Create a set called seen(), every time you add the window, at it to seen, unless its in the set
        # If in the set, the you should move the window left
        # Create a count variable so that you can compare the max lengths

        l, r, count = 0, 0, 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            count = max(count, r - l + 1)
        return count
            