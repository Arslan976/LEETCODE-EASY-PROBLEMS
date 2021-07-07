class Solution(object):
    def duplicateZeros(self, arr):
        # DUPLICATING THE ARRAY
        duplicateArray = [i for i in arr]
        first_index = 0
        second_index = 0
        
        while first_index < len(arr):
            # CHECKING IF THE ARRAY VALUE IS ZERO
            if not duplicateArray[second_index]:
                arr[first_index] = 0
                first_index += 1
                if first_index < len(arr):
                # SETTING DUPLICATE ZERO WHEN FOUND ONE
                    arr[first_index] = 0
            else:
                arr[first_index] = duplicateArray[second_index]
            second_index += 1
            first_index += 1
            
        return arr

obj = Solution()
print(obj.duplicateZeros([1,0,2,3,0,4,5,0]))
            
    