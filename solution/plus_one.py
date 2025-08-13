"""
66. Plus One
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""
from typing import List

digits = [4,3,2,1]
length = len(digits)
int_digits = int(''.join(map(str, digits)))

for i in range(length):
  if 0 <= digits[i] <= 9:
    add = int_digits + 1
    plus_one = list(map(int, str(add)))

print(plus_one)

# print(length)
# if 0 in digits:
#   print("0")
# elif 1 <= len(digits) <= 100:
#   int_digits = int(''.join(map(str, digits)))
#   add = int_digits + 1
#   again_list = list(map(int, str(add)))
#   print(again_list)


class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    length = len(digits)
    int_digits = int(''.join(map(str, digits)))
    for i in range(length):
      if 0 <= digits[i] <= 9 and 1 <= len(digits) <= 100:
        add = int_digits + 1
    return list(map(int, str(add)))
