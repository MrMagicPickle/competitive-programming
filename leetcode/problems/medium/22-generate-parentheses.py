# https://leetcode.com/problems/generate-parentheses/

def solve(n):
  ans = []  
  def backtrack(myStr, left, right):
    if len(myStr) == 2 * n:
      ans.append(myStr)
      return
    if left < n:
      backtrack(myStr + '(', left+1, right)
    if right < left:
      backtrack(myStr + ')', left, right+1)
  backtrack('', 0, 0)
  return ans

if __name__ == "__main__":
  print(solve(3))