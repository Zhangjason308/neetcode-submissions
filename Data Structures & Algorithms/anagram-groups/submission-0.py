class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}

        for ana in strs:
            ana_tuple = tuple(sorted(ana))
            if ana_tuple not in ana_dict.keys():
                ana_dict[ana_tuple] = [ana] # ana_dict = {"act": ["act"]}
            else:
                ana_dict[ana_tuple].append(ana) # ana_dict = {"act": ["act", "cat"]}
        
        return list(ana_dict.values())
            



        