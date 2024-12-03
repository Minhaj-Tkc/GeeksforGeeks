class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            # Swap elements at left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            # Move pointers closer to the center
            left += 1
            right -= 1

        return arr
        

arr = [3, 5, 0, 0, 4]
sol = Solution()
result = sol.reverseArray(arr)
print(result)  