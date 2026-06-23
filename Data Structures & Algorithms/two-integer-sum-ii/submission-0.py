class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Looks like a 2-sum problem except we want to use O(1) space
        # Use a two-pointer solution
        # while l < r
        # If sum is greater than the target, decrease the right pointer
        # If the sum is less than the target, increase the left pointer
        # If sum = target, return index of l + 1 and index of r + 1

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1