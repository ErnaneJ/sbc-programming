class Solution(object):
  def isPalindrome(self, x):
    if x < 0:
      return False

    target = x
    r_x = 0

    while x > 0:
      r_x = 10*r_x + (x%10)
      x = x // 10
    
    return target == r_x