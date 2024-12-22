class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []
    def backtrack(curr, currLeft, currRight):
      if (len(curr) == n * 2):
        result.append(curr)
        return
      if (currLeft < n):
        backtrack(curr + "(", currLeft + 1, currRight)
      if (currRight < currLeft):
        backtrack(curr + ")", currLeft, currRight + 1)
    backtrack("", 0, 0)
    return result
