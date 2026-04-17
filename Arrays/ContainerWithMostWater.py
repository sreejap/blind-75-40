# https://leetcode.com/problems/container-with-most-water/
class Solution:
    # we start with max width which is the extreme ends
    # then we check left and right bounds to find the tallest height to maximize the area
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len (height) - 1

        while left < right:
            area = (right - left) * min (height[left], height[right])

            max_area = max (area, max_area)
            if height [left] <= height[right] :
                left += 1 # we try to find the taller height to maximize area
            else:
                right -= 1
        return max_area
