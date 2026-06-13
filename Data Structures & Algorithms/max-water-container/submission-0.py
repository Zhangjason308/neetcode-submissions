class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Brute force solution would be to use a double for loop
        # Could use a two pointer approach to save time complexity
        # What if we ordered the height array, and had its index along with it

        # height = [1,7,2,5,4,7,3,6] -> take the min of left and right
        # width = [0,1,2,3,4,5,6,7] -> take the difference between left and right
        
        water = 0
        left  = 0
        right = len(heights) - 1

        while left < right:
            temp = (right - left) * min(heights[right], heights[left])
            if temp > water:
                water = temp
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return water