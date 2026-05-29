class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        frequency -> Hash Map -> Dictionary
        - Create a list of tuples [(1: __),(2: __),(3: __),...]
        """
        count_dict = {}
        count_list = []
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] = count_dict[i] + 1
        
        # Now convert the dictionary to a list thats reversed

        for num, count in count_dict.items():
            count_list.append([count, num])
        count_list.sort()

        new_list = []
        while k > 0:
            new_list.append(count_list.pop()[1])
            k -= 1
        return new_list

        
