class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First convert the string to strip spaces and covert to lower cases
        # Thinking of splitting the string in half and reversing one string, if it matches then its a valid palindrome
        filtered_char = []
        for char in s:
            if char.isalnum():
                filtered_char.append(char.lower())
        s_filtered = "".join(filtered_char)

        s_reversed = s_filtered[::-1]

        if s_reversed == s_filtered:
            return True
        return False
        
        