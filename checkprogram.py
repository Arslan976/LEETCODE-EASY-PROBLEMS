def removeDuplicates(nums):
        if len(nums) == 0 or len(nums) == 1:
            print("Stopped!")
        else:
            temp = list(range(len(nums)))
            j = 0;
            for i in range(0, len(nums)-1):
 
                if nums[i] != nums[i+1]:
                    temp[j] = nums[i]
                    j += 1
 
            temp[j] = nums[len(nums)-1]
            j += 1
    
            for i in range(0, j):
                nums[i] = temp[i]
            while j <= len(nums) + 1:
                nums.pop()
                j += 1
        return nums

print("result")
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))