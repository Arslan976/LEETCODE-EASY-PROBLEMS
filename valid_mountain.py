class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        index = 1    
        while(index < len(arr) and arr[index] > arr[index - 1]):
            index += 1
        if index == 1 or index == len(arr):
            return False
        
        while(index < len(arr) and arr[index] < arr[index - 1]):
            index += 1
        return index == len(arr)

obj = Solution()
print(obj.validMountainArray([0,3,2,1]))