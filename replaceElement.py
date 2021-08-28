def replaceElements(arr):
        
        index_i = 0
        index_j = 0
        largest_on_right = 0
        largest_item_index = 0
        
        while index_i < len(arr) - 1:
            index_j = index_i + 1
            if largest_item_index == index_i:
                largest_on_right = 0
                while index_j < len(arr):
                    if largest_on_right < arr[index_j]:
                        largest_on_right = arr[index_j]
                        largest_item_index = index_j
                    index_j += 1
            arr[index_i] = largest_on_right
       
            index_i += 1
        arr[len(arr) - 1] = -1
        return arr
    
print(replaceElements([17,18,5,4,6,1]))