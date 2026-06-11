class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. If length is 3, see if the sum is equal to 0, if so, return the array
        # 2. If not equal to 0, return empty
        # 3. 

        nums.sort()

        # [-4, -1, -1, 0 , 1, 2]
        # Check for each elem in the array, index after it should have left and right pointer
        # if the sum of the 3 is less than 0, move the left pointer
        # if the sum of the 3 is greater than 0, move the right pointer
        
        three_sum_arr = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        three_sum_arr.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
            
        return three_sum_arr



        