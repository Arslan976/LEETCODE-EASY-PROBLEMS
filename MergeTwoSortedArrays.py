def merge(nums1, m, nums2, n):
    resultArray = [None] * (m + n)
    i = 0
    j = 0
    k = 0
    while i < m and j < n:
            
        if nums1[i] < nums2[j]:
            resultArray[k] = nums1[i]
            i += 1
            k += 1
        else:
            resultArray[k] = nums2[j] 
            j += 1
            k += 1
        
    while i < m:
        resultArray[k] = nums1[i]
        i += 1
        k += 1
        
    while j < n:
        resultArray[k] = nums2[j]
        j += 1
        k += 1
        
    print(resultArray)
    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)
