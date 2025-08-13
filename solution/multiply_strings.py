"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the
product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer
directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


num1 = "123"
num2 = "456"
num = []
num3 = []
for n in num1:
  num.append(n)

for n1 in num2:
  num3.append(n1)

int_digits = int(''.join(map(str, num)))
int_digit = int(''.join(map(str, num3)))
x = int_digits * int_digit
result = str(x)
print(result)


class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    num = []
    num3 = []
    for n in num1:
      num.append(n)
    for n1 in num2:
      num3.append(n1)

    int_digits = int(''.join(map(str, num)))
    int_digit = int(''.join(map(str, num3)))
    x = int_digits * int_digit
    return str(x)