# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

  if len(arr) == 1:
    return arr[0]
  if len(arr) == 2:
    return max(arr[0], arr[1])

  maxArr = [0] * len(arr)
  maxArr[0] = arr[0]
  maxArr[1] = max(arr[0], arr[1])
  maxSum = max(arr[0], arr[1])
  for i in range (2, len(arr)):
    maxSum = max(arr[i], maxSum)
    maxSum = max(maxSum, maxArr[i-2] + arr[i])
    maxArr[i] = maxSum
    
  return maxSum

if __name__ == "__main__":
  arr = [3, 7, 4, 6, 5]
  print('<<<')
  print(maxSubsetSum(arr))