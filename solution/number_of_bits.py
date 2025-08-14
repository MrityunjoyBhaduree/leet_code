"""
191. Number of 1 Bits
Given a positive integer n, write a function that returns the number of set bits in its
binary representation (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30

Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1
"""

num = 11
number = []
count = 0
check = 1
while num != 0:
  digit = num % 2
  num = int(num / 2)
  number.append(digit)


for i in range(len(number)):
  if number[i] == check:
    count += 1

print(count)


class Solution:
  def hammingWeight(self, n: int) -> int:
    check = 1
    number = []
    count = 0
    while n != 0:
      binary = n % 2
      n = n // 2
      number.append(binary)

    for i in range(len(number)):
      if number[i] == check:
        count += 1

    return count
