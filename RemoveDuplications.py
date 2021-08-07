def removeDuplicates(nums):
        if len(nums) == 0 or len(nums) == 1:
            print("Stopped! The Length of the Array is 1 or 0")
        else:
            temporay_array = []
            index = 0;
            while index < len(nums) and index + 1 < len(nums):
                if nums[index] != nums[index+1]:
                    temporay_array.append(nums[index])
                index += 1
            temporay_array.append(nums[len(nums) - 1])
            index = 0
            while index < len(nums):
                if index < len(temporay_array):
                    nums[index] = temporay_array[index]
                    index += 1
                else:
                    nums.pop()
        return(nums)
                    
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))