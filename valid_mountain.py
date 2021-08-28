def validMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        strict_increase = True
        index = 0
        point = None
        highest_peak = 0
        
        if len(arr) <= 2:
            strict_increase = False
        
        while strict_increase != False and len(arr) > 2 and index < len(arr) :
            print("in the loop")
            if point == None:
                point = arr[index]
            elif point < arr[index]:
                if index <= round(len(arr) / 2) - 1:     
                    point = arr[index]
                    highest_peak = index
                else:
                    strict_increase = False
                    break
            elif point == arr[index]:
                strict_increase = False
                break
            elif point > arr[index]:
                print(index)
                if index > round(len(arr) / 2) - 1:    
                    
                     point = arr[index]
                else:
                    strict_increase = False
                    break
            index += 1
            
        if highest_peak == len(arr) - 1:
            strict_increase = False
        print(strict_increase)
        return strict_increase
validMountainArray([1,3,2])