class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        # Calculate the number of elements to be rotated
        n = len(arr)
        d = d % n

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the first d elements
        reverse(0, d - 1)
        print(arr)
        # Step 2: Reverse the remaining elements
        reverse(d, n - 1)
        # Step 3: Reverse the entire array
        reverse(0, n - 1)
        
        return arr
            


sol = Solution()
output = sol.rotateArr([1, 4, 3, 2, 6, 5], 5)
print(output)