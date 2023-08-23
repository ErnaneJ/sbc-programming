class Solution(object):
  def groupAnagrams(self, strs):
    words = [str(sorted(s)) for s in strs]
    table = {}
    for index, word in enumerate(words):
      if word in table:
        table[word].append(index)
      else:
        table[word] = [index]

    return [[strs[index] for index in values] for values in table.values()]