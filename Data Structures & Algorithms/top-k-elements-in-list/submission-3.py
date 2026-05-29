class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        freq_list = []

        for i in nums:
            freq_dict[i] = freq_dict.get(i, 0) + 1

        #{1: 1, 2: 2, 3: 3}
        
        count_list = []
        for num, count in freq_dict.items():
            count_list.append([count, num])
        count_list.sort()

        while k > 0:
            freq_list.append(count_list.pop(-1)[1])
            k -= 1
        return freq_list

        
