def solve2(n, k):
  
  if k == n:
    return 'a' * n

  s = ''
  base = 97
  remainder = k - n
  nZs = remainder // 25
  lastCharOrd = remainder % 25
  count = 0  

  s = 'z' * nZs
  
  s = chr(base + lastCharOrd) + s
  remainderAs = n - nZs - 1
  if remainderAs > 0:
    s = ('a' * remainderAs) + s  

  # print(nZs, lastCharOrd, chr(base + lastCharOrd))
  return s

def solve(n, k):
  s = 'a' * n
  if k == len(s):
    return s

  base = 97
  remainder = k - len(s)
  nZs = remainder // 25
  lastCharOrd = remainder % 25
  count = 0
  pointer = len(s) - 1
  while count < nZs:
    if pointer < len(s) - 1:
      s = s[:pointer] + 'z' + s[pointer+1:]
    else:
      s = s[:pointer] + 'z'
    
    pointer -= 1
    count += 1
  if pointer < len(s) - 1:
    s = s[:pointer] + chr(base + lastCharOrd) + s[pointer+1:]
  else:
    s = s[:pointer] + chr(base + lastCharOrd)

  # print(nZs, lastCharOrd, chr(base + lastCharOrd))
  return s

if __name__ == "__main__":
  print(solve2(3, 27))
  print(solve2(5, 73))