def merge(self, nums1, m, nums2, n):
    index_num2 = 0
    index_num1 = 0
    if m == 0:
        iterator = 0
        while iterator < n:
            nums1[iterator] = nums2[iterator]
            iterator += 1
    else:
        while (index_num2 < n and index_num1 < len(nums1)):
            iterator = len(nums1) - 1
            print(iterator)
            if nums1[index_num1] > nums2[index_num2]:
                while(iterator > index_num1):
                    nums1[iterator] = nums1[iterator - 1]
                    iterator -= 1
                nums1[index_num1] = nums2[index_num2]
                index_num2 += 1
            elif index_num1 > m and nums1[index_num1] == 0:
                nums1[index_num1] = nums2[index_num2]
                index_num2 += 1
            elif index_num1 + 1 > m and nums1[index_num1] == 0:
                nums1[index_num1] = nums2[index_num2]
                index_num2 += 1
            index_num1 += 1
        
    return nums1

print(merge("self",  [-1,0,0,0,3,0,0,0,0,0,0], 5, [-1,-1,0,0,1,2] , 6 ))