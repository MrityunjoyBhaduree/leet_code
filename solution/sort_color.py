"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in
the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""



from typing import List


class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low, mid, high = 0, 1, 2
    l = []
    m = []
    h = []
    sort_list = []

    for i in nums:
      if low == i:
        l.append(i)
      elif mid == i:
        m.append(i)
      elif high == i:
        h.append(i)
    # Combine and update nums in-place
    sorted_list = l + m + h
    for i in range(len(nums)):
      nums[i] = sorted_list[i]