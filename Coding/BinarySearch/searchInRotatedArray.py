#Intuition: Check the target in the array by checking whether the array is right rotated or left rotated 
def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1 
        while left <= right: 
            mid = left + ( right - left ) // 2
            if nums[mid] == target:    
                return mid
            #Check if the array is left rotated 
            if nums[mid] >= nums[left]:
                #Find the range in which the target lies 
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1
        return -1 

if __name__ == "__main__":

    print(search([4,5,6,7,0,1,2], 0))