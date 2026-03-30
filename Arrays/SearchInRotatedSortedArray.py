class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is binary search
        # do the two binary searches if I want to practise...
        n = len (nums)

        left = 0
        right = n-1

        while left <= right: # put equals because we have the value in the array
            mid = left + (right-left) // 2 # to compute mid in binary search

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # left side is sorted
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right side is sorted
                if target <= nums[right]  and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
