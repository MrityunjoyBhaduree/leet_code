"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""


# number = 1563847412
# a = 2 ** 31
# print(a)
# b = 2 ** -31
# if number > 0 != a:
#   reversed_number = str(number)[::-1]
#   reversed_number = int(reversed_number)
#   if reversed_number > a:
#     print(0)
#   else:
#     print(reversed_number)
#
# elif number < 0 != a:
#   num = abs(number)
#   reversed_number = str(num)[::-1]
#   reversed_number = int(reversed_number)
#   if reversed_number > a:
#     print(0)
#   else:
#     print(-reversed_number)
#
# else:
#   print(0)

# x = -123
# a = 2 ** 31 - 1
# b = -2 ** 31
#
# reversed_number = 0
# num = abs(x)
#
# while num != 0:
#     digit = num % 10
#     reversed_number = reversed_number * 10 + digit
#     num = num // 10
#
# # Apply the sign correctly
# if x < 0:
#     reversed_number = -reversed_number
#
# # Check 32-bit signed integer range
# if reversed_number < b or reversed_number > a:
#     print(0)
# else:
#     print(reversed_number)

class Solution:
  def reverse(self, x: int) -> int:
    a = 2 ** 31
    b = 2 ** -31
    if x > 0 != a:
      reversed_number = str(x)[::-1]
      reversed_number = int(reversed_number)
      if reversed_number > a:
        return 0
      else:
        return reversed_number

    elif x < 0 != b:
      num = abs(x)
      reversed_number = str(num)[::-1]
      reversed_number = int(reversed_number)
      if reversed_number > a:
        return 0
      else:
        return -reversed_number
    else:
      return 0


class Solution:
  def reverse(self, x: int) -> int:
    a = 2 ** 31 - 1
    b = -2 ** 31
    reversed_number = 0
    num = abs(x)

    while num != 0:
      digit = num % 10
      reversed_number = reversed_number * 10 + digit
      num = num // 10

    if x < 0:
      reversed_number = -reversed_number

    if reversed_number < b or reversed_number > a:
      return 0
    else:
      return reversed_number
