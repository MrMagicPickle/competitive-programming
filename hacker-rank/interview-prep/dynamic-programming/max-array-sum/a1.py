# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
  table = [] 
  maxSum = arr[0]
  for i in range (len(arr)):
    row = [0] * len(arr)
    table.append(row)
  
  for i in range (len(arr)):
    num = arr[i]
    table[i][i] = num
    badIndex = i-1
    if i == 0:      
      continue
    for j in range (i):
      if j == badIndex:
        table[j][i] = table[j][i-1]
      else:
        table[j][i] = table[j][i-2] + num
      if table[j][i] > maxSum:
        maxSum = table[j][i]
  for i in range (len(table)):
    print(table[i])
  return maxSum

if __name__ == "__main__":
  arr = [3, 7, 4, 6, 5]
  print('<<<')
  print(maxSubsetSum(arr))