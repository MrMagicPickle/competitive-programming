# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def solve(s):
  aDict = {}
  maxCount = 0
  count = 0
  for i in range (len(s)):
    char = s[i]
    if char in aDict:
      aDict = {}
      aDict[char] = i
      count -= 1
    else:
      aDict[char] = i
      count += 1
    
    if count > maxCount:
      maxCount = count
    print(maxCount, char)
  return maxCount

if __name__ == "__main__":
  print(solve('dvdf'))