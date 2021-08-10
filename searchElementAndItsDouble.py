def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        x_index = 0
        result = False
        while x_index < len(arr) - 1:
            y_index = 0
            while y_index < len(arr):
                if x_index != y_index:
                    if arr[x_index] == arr[y_index] * 2 or arr[y_index] == arr[x_index] * 2:
                        result = True
                y_index += 1
            x_index += 1
        return result

print(checkIfExist([-20,8,-6,-14,0,-19,14,4]))