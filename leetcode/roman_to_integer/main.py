class Solution(object):
  def romanToInt(self, s):
    table = {
      "I": 1, "V": 5, "X": 10, "L": 50,
      "C": 100, "D": 500, "M": 1000
    }

    summ = 0
    last = 0

    size = len(s)-1

    while size >= 0:
      current_value = table[s[size]]
      if current_value >= last:
        summ += current_value
      else:
        summ -= current_value

      last = current_value
      size -=1

    return summ