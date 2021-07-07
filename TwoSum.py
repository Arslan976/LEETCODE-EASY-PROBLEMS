def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answerArray = []
        index = 0
        while index < len(nums):   
            if index + 1 < len(nums) and nums[index] + nums[index + 1] == target:
                answerArray = [index, index + 1]
            index += 1
        return answerArray

print(twoSum([2,7,11,15],9))