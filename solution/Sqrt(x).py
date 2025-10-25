"""
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest
integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the
nearest integer, 2 is returned.

Constraints:
0 <= x <= 231 - 1

25 – 1 = 24
24 – 3 = 21
21 – 5 = 16
16 – 7 = 9
9 – 9 = 0
"""
"""
This is first approach for solve this problem.
"""
x = 8
s = 1
a = 0
count = 0
for i in range(x):
  a = x - s
  s += 2
  count += 1
  x = a
  if x == 0 or x < s:
    print(count)
    break
  if x < 0:
    break

"""Second approach"""
if x == 0:
  print(x)
count = 0
s = 1
while x >= s:
  x = x - s
  s += 2
  count += 1
print(count)