def removeElement(nums, val):
    main_index = 0
        
    while main_index < len(nums):
        if nums[main_index] == val:
            secondary_index = main_index + 1
            while secondary_index < len(nums):
                nums[secondary_index - 1] = nums[secondary_index]
                secondary_index += 1
            nums.pop()
        else:
            main_index += 1

removeElement([0,2,2,3,3,5,6], 3)