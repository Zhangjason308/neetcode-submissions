class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search problem again...
        # We have a target instead of finding lowest num
        # Create a binary search to find the lowest num
        # Create another binary search with the lowest point as the middle

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        lowest = left
        left, right = 0, len(nums) - 1

        
        if target >= nums[lowest] and target <= nums[right]:
            left = lowest
        else:
            right = lowest - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

            

