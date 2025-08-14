"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

# First convert input binary value into decimal number
# Then added those decimal number
# And finally convert decimal to binary
# (11)2 = (1 * 2 **1) + (1 * 2 ** 0)

# a = "11"
# b = "1"
# number = 0
# b_number = 0
#
# for i in range(len(a)):
#   number += int(a[len(a) - 1 - i]) * (2 ** i)
# print(number)
#
# for i in range(len(b)):
#   b_number += int(b[len(b) - 1 - i]) * (2 ** i)
#
# final  = number + b_number
# print(final)
# output = []
# while final != 0:
#   digit = final % 2
#   final = int(final / 2)
#   output.append(digit)
#
# final_output = []
# for i in range(len(output) - 1, -1, -1):
#   final_output.append(output[i])
#
# print(str(final_output))


class Solution:
  def addBinary(self, a: str, b: str) -> str:
    num1 = 0
    num2 = 0
    for i in range(len(a)):
      num1 += int(a[len(a) - 1 - i]) * (2 ** i)
    print(num1)
    for i in range(len(b)):
      num2 += int(b[len(b) - 1 - i]) * (2 ** i)
    print(num2)
    add_binary = num1 + num2
    print(add_binary)
    if add_binary == 0:
      return "0"
    else:
      result = []
      # Extract bits directly MSB → LSB
      while add_binary != 0:
        digit = add_binary % 2
        add_binary = add_binary // 2
        result.append(digit)
        # result.insert(0, digit)    # insert at the front

      final_output = []
      for i in range(len(result) - 1, -1, -1):
        final_output.append(result[i])
      final = ''.join(map(str, final_output))
      return final

a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
x =Solution()
print(x.addBinary(a, b))