# https://leetcode.com/contest/biweekly-contest-41/problems/count-the-number-of-consistent-strings/

def solve(allowed, words):  
  aDict = {}

  for x in allowed:
    aDict[x] = 1
  
  count = 0
  for word in words:
    ok = True
    for char in word:
      if char not in aDict:
        ok = False
        break
    if ok:
      count += 1
  return count
if __name__ == "__main__":
  # ans = solve('ab', ["ad","bd","aaab","baa","badab"])
  # ans = solve('abc', ["a","b","c","ab","ac","bc","abc"])
  ans = solve('cad', ["cc","acd","b","ba","bac","bad","ac","d"])
  print(ans)