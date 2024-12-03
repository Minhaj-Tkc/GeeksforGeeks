#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        largest = second = float('-inf')

        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif largest > num > second:
                second = num

        return second if second != float('-inf') else -1


# Example usage:
arr = [15, 14, 15, 19]
sol = Solution()
result = sol.getSecondLargest(arr)
print(result)  

