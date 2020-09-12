def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = left + ( right - left ) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1 
            else: 
                right = mid - 1
        
        return nums[left]

if __name__ == "__main__":
    print(findMin([3,1,2]))