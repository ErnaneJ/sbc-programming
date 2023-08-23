class Solution(object):
  def addTwoNumbers(self, list1, list2):
    return list(map(int, list(str(int(''.join(map(str, list1[::-1]))) + int(''.join(map(str, list2[::-1]))))[::-1])))