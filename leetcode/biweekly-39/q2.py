# https://leetcode.com/contest/biweekly-contest-39/problems/minimum-deletions-to-make-string-balanced/

def solve(s):
  # count(s)
  aCount = 0
  bCount = 0
  n = 0
  if s == 1: 
    return 0

  prev = s[0]  
  seenFirstB = False
  for i in range (1, len(s)):
    # print(aCount, bCount, prev, s[i])
    if s[i] == 'b':
      if not seenFirstB:
        seenFirstB = True
        bCount += 1
        continue
      if prev == 'a':
        n += min(bCount, aCount)
        bCount = 0
        aCount = 0

      bCount += 1
    if s[i] == 'a':
      if seenFirstB:
        aCount += 1

    prev = s[i]

  return n

def count(s):
  aDict = {}
  for x in s:    
    aDict[x] = aDict.get(x, 0) + 1
  print(aDict)

if __name__ == "__main__":
  print(solve('aababbab'))
  print(solve('bbaaaaabb'))
  # print(solve("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"))
  # print(solve("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbabab"))