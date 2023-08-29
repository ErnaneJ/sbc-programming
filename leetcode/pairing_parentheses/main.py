class Solution(object):
    def generateParenthesis(self, n):
        def generate(openN, closeN, ans):
            if len(ans) == n*2:
               return ans

            if openN < n:
               generate(openN+1, closeN, ans+"(")
            if closeN < openN:
               generate(openN , closeN+1, ans + ")")

            return ans
        vec = []
        generate(0, 0, vec)
        return vec