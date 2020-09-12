from heapq import heapify, heappop, nlargest, nsmallest, _heapify_max

if __name__ == '__main__':
    nums = [1, 5, 3, 2, 4]
    nums1 = [1, 5, 3, 2, 4]
    # Code for min heap
    heapify(nums)
    # Code for max heap
    _heapify_max(nums1)
    print(nums, nums1)
    #Get the nth largest element in min heap
    print(nlargest(3, nums)[-1])
    #Get the nth smallest element in min heap
    print(nsmallest(1, nums)[-1])
    #Get the nth largest element in max heap
    print(nlargest(3,nums1)[-1])
    #Get the nth smallest element in max heap
    print(nsmallest(1,nums1)[-1])