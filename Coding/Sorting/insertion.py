def insertion_sort(nums):
    ''' Returns the sorted array which is done 
    inplace and the algorithm is stable. 
    Intuition is that the left part of the array
    is always sorted'''
    for i in range(len(nums)):
        j = i 
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


if __name__ == "__main__":
    
    nums = [5, 2, 4, 3, 1]

    print(insertion_sort(nums))