"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of
num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large
integers (such as BigInteger). You must also not convert the inputs to integers directly.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""

num1 = "11"
num2 = "123"
num = []
num3 = []
for n in num1:
  num.append(n)

for n1 in num2:
  num3.append(n1)

int_digits = int(''.join(map(str, num)))
int_digit = int(''.join(map(str, num3)))
x = int_digits + int_digit
result = str(x)


class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    sys.set_int_max_str_digits(0)
    num = []
    num3 = []
    for n in num1:
      num.append(n)
    for n1 in num2:
      num3.append(n1)

    int_digits = int(''.join(map(str, num)))
    int_digit = int(''.join(map(str, num3)))
    x = int_digits + int_digit
    return str(x)
