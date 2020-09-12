def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1 
        
        while left < right: 
            mid = left + (right - left) // 2 
            if nums[mid] < nums[mid + 1]:
                left = mid + 1 
            else: 
                right = mid 
            
        return left

if __name__ == "__main__":
    print(findPeakElement([1, 2, 3, 1]))


'''''''''''''''''
left = 0, right = 3, mid = 1
nums[1] = 2, nums[2] = 3
Now 3 > 2 so the peak should be checked from 3 so the left key is changed to 3
If the above is false then the right should be changed
'''''''''''''''''