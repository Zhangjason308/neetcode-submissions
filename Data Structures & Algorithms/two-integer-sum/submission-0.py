class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass solution

        sum_dict = {} # {value, index}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in sum_dict:
                return [sum_dict[complement], index]
            else:
                sum_dict[value] = index

                
            
        

        