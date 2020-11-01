# https://leetcode.com/contest/weekly-contest-213/problems/count-sorted-vowel-strings/

def solve(n):
  if n == 1:
    return 5 
  a = [1, 1, 1, 1, 1]

  for i in range (2, n+1):
    for k in range (len(a)):
      sum = 0
      for j in range (k, len(a)):
        sum += a[j]
      a[k] = sum
  count = 0

  for i in range (len(a)):
    count += a[i]

  return count
if __name__ == "__main__":
  print(solve(2))
  print(solve(33))