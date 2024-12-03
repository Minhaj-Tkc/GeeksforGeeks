class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        # Step 1: Find the first decreasing element
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
    
        if i >= 0:  # Only perform the next steps if i is valid
            # Step 2: Find the smallest larger element on the right of arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # Step 3: Swap arr[i] and arr[j]
            print("0", arr[i],"1" ,arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    
        # Step 4: Reverse the suffix starting at i + 1
        arr[i + 1:] = reversed(arr[i + 1:])
        return arr
    

sol = Solution()
output = sol.nextPermutation([2, 4, 1, 7, 5, 0])
print(output)