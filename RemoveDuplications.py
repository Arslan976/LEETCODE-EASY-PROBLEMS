def removeDuplicates(nums):
    i = 0
        
    while i < len(nums):
            
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            j = i + 1
            while j < len(nums):
                nums[j - 1] = nums[j]
                j += 1
            nums.pop()
        else:
            i += 1
    return(nums)

print(removeDuplicates([1,2,2,3,4,5,5,5]))