def mergeSort(nums):
    '''
    This is a divide and conquer algorithm where the array 
    is divide into two parts left and right and the merge will happen
    from the leaves level in the recursion
    '''
    if len(nums) == 1:
        return
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    mergeSort(left)
    mergeSort(right)

    i = 0 
    j = 0
    k = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else: 
            nums[k] = right[j]
            j += 1
        k += 1 

    while i < len(left):
        nums[k] = left[i] 
        k += 1
        i += 1
    
    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1
    return nums

if __name__ == '__main__':
    print(mergeSort([3, 4, 2, 5, 1]))







