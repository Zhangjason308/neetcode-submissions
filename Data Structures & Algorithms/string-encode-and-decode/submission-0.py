class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for elem in strs:
            encoded += str(len(elem)) + "#" + elem
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            j = i # This is the index of the delimiter
            while s[j] != '#':
                j += 1
            s_length = int(s[i:j]) # length of the string
            decoded.append(s[j + 1 : j + 1 + s_length])
            i = j + 1 + s_length
        return decoded
            
        
