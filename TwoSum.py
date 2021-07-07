
def twoSum(self, nums, target):
        indiceArray = []
        first_index = 0
        flag = True
        
        while(flag == True and first_index < len(nums)):
            second_index = 1    
            while (flag == True and first_index != second_index and second_index < len(nums)):
                if (nums[first_index] + nums[second_index] == target):
                    indiceArray = [first_index, second_index]
                    flag = False
                second_index += 1
            first_index += 1
            print(indiceArray)
        return indiceArray 

twoSum("self", [3,3], 6 )