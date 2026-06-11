class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Should sort the array
        # Then iterate through the array, return the highest count

        nums_set = set(nums)
        count_array = []

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                start = num
                while start + 1 in nums_set:
                    count += 1
                    start += 1
                count_array.append(count)
            else:
                pass

        count_array.sort()
        if len(count_array) == 0:
            return 0
        return count_array.pop(-1)
                