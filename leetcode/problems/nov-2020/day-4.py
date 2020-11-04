# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/
def solve(s):
  if len(s) == 1:
    return 1

  prevChar = s[0]
  count = 1
  maxCount = 1
  for i in range (1, len(s)):
    currChar = s[i]
    if prevChar == currChar:
      count += 1
      if count > maxCount:
        maxCount = count
    else:
      count = 1      
    prevChar = currChar
  return maxCount


  return 0

if __name__ == "__main__":
  print(solve('tourist'))