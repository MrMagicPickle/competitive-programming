# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
  modded = d % len(a)
  start = modded
  ans = []
  for i in range (len(a)):
    ans.append(a[start])
    start += 1
    if start == len(a):
      start = 0
  return ans

if __name__ == "__main__":
  a = [1,2,3,4,5]
  d = 4
  print('<<<')
  print(rotLeft(a, d))