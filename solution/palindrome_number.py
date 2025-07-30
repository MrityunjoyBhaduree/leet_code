"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?
"""


# num = 0
# if num >= 0:
#   print("Enter")
#   reversed_number = str(num)[::-1]
#   reversed_number = int(reversed_number)
#   if reversed_number == num:
#     print("Enter")
#     print(reversed_number)
#   else:
#     print(0)
#
# else:
#   print(0)

# x = -121
# original = x
# reversed_num = 0
#
# while x > 0:
#   print("Enter here")
#   digit = x % 10
#   reversed_num = reversed_num * 10 + digit
#   x = x // 10
#
# if reversed_num == original:
#     print(reversed_num)
# if x < 0:
#   print(0)
# else:
#     print(0)


class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x >= 0:
      reversed_number = str(x)[::-1]
      reversed_number = int(reversed_number)
      if reversed_number == x:
        return True
      else:
        return False
    else:
      return False

class Solution:
  def isPalindrome(self, x: int) -> bool:
    original = x
    reversed_num = 0

    while x > 0:
      digit = x % 10
      reversed_num = reversed_num * 10 + digit
      x = x // 10

    if reversed_num == original:
      return True
    if original < 0:
      return False
    else:
      return False

