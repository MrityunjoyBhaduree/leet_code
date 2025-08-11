"""
202. Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
"""
def add(n, seen=None):

  if seen is None:
    seen = []
  x = str(n)
  print(x)
  res = 0
  for i in range(len(x)):
    res += int(x[i]) ** 2

  if res == 1:
    return True
  if res in seen:
    return False

  seen.append(res)
  return add(res, seen)

n = 2
a = add(n)
print(a)


class Solution:
  def isHappy(self, n: int, seen=None) -> bool:
    if seen is None:
      seen = []

    x = str(n)
    res = 0
    for i in range(len(x)):
      res += int(x[i]) ** 2
    if res == 1:
      return True
    if res in seen:
      return False

    seen.append(res)
    return self.isHappy(res, seen)
