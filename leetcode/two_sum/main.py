class Solution(object):
  def twoSum(self, nums, target):
    th = {}
    for i, num in enumerate(nums):
      comp = target - num
      if comp in th:
        return [nums.index(comp), i]
      th[num] = comp
    
    return []
