class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We know the matrix is sorted -> use a binary search to get O(log(n))
        # Brute force solution would be to iterate through the entire list O(n)
        # Create a left and right pointer for each array
        # We need a middle point to guage if we move left or right pointer
        # We can use the arrays first to find the mid point, and then use pointer within the array once identified its in that range
        
        l_matrix, r_matrix = 0, len(matrix) - 1

        while l_matrix <= r_matrix:
            mid_matrix = l_matrix + (r_matrix - l_matrix) // 2

            if matrix[mid_matrix][0] <= target <= matrix[mid_matrix][-1]:
                l, r = 0, len(matrix[mid_matrix]) - 1

                while l <= r:
                    mid = l + (r - l) // 2

                    if matrix[mid_matrix][mid] == target:
                        return True
                    elif matrix[mid_matrix][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
            elif target < matrix[mid_matrix][0]:
                r_matrix = mid_matrix - 1
            else:
                l_matrix = mid_matrix + 1
        return False
