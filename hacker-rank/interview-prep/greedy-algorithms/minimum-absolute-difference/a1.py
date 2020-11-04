# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
  arr.sort()
  minVal = abs(arr[0] - arr[1])
  for i in range (len(arr)-1):
    diff = abs(arr[i] - arr[i+1])
    if diff < minVal:
      minVal = diff
  return minVal

if __name__ == '__main__':
  print('<<<')  
  print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))