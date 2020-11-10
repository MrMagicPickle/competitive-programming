def solve(s):
  aDict = {}
  for x in s:
    aDict[x] = aDict.get(x, 0) + 1
  
  bDict = {}
  for k,v in aDict.items():
    if v in bDict:
      bDict[v].append(k)
    else:
      bDict[v] = [k]

  count = 0
  #  print(aDict)
  for key in sorted(bDict):
    chars = bDict[key]    
    #print(count, key, len(chars))
    while len(chars) > 1:
      char = chars.pop()
      val = key
      while True:
        count += 1
        val -= 1
        if not val in bDict or val == 0:
          bDict[val] = char
          break

  return count



if __name__ == "__main__":
  print(solve('aab'))
  print(solve('aaabbbcc'))
  print(solve('abcabc'))