# https://leetcode.com/contest/biweekly-contest-39/problems/defuse-the-bomb/

def solve(code, k):
  if k == 0:
    return [0] * len(code)

  ans = []    
  if k > 0:
    for i in range (len(code)):
      sum = 0
      if i + k < len(code):
        for j in range (i+1, i+k+1):
          sum += code[j]
      else:
        for j in range(i+1, len(code)):
          sum += code[j]
        remainder = k - (len(code) -1 - i)
        for j in range(remainder):
          sum += code[j]
      ans.append(sum)
  if k < 0: 
    for i in range(len(code)):
      sum = 0
      start = i + k
      if start >= 0:
        for j in range (start, start + abs(k)):
          sum += code[j]
      else:
        for j in range (start, 0):
          sum += code[j]
        remainder = abs(k) - (0 - (start))
        for j in range(remainder):
          sum += code[j]

      ans.append(sum)
  return ans

if __name__ == "__main__":
  print(solve([5,7,1,4], 3))
  print(solve([1,2,3,4], 0))  
  print(solve([2,4,9,3], -2))