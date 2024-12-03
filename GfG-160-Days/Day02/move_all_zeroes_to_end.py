class Solution:
    def pushZerosToEnd(self,arr):
         n = len(arr)
         non_zero_index = 0

        # Traverse the array
         for i in range(n):
            if arr[i] != 0:
                # Swap the current element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1

         return arr
    
arr = [3, 5, 0, 0, 4]
sol = Solution()
result = sol.pushZerosToEnd(arr)
print(result)  # Output: 15