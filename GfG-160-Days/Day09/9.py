class Solution:
    def getMinDiff(self, arr, k):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)

        # Step 2: Initial difference between max and min without any changes
        result = arr[-1] - arr[0]

        # Step 3: Traverse the array to find minimum difference
        for i in range(1, n):
            # If subtracting K results in a negative height, skip the iteration
            if arr[i] - k < 0:
                continue
            
            # Calculate the minimum and maximum heights after modifications
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[-1] - k, arr[i - 1] + k)

            # Update the result with the smallest difference
            result = min(result, max_height - min_height)

        return result



sol = Solution()
output = sol.getMinDiff([1, 5, 8, 10], 2)
print(output)