def solve(n):
  if n == 0 or n == 1:
    return n
  maxN = 1
  nums = [0] * (n+1)
  nums[0] = 0
  nums[1] = 1

  limit = n + 1
  index = 1
  while (2 * index) < limit and (2 * index+1) < limit:
    nums[2 * index] = nums[index]
    nums[(2 * index) + 1] = nums[index] + nums[index+1]
    maxN = max(maxN, nums[index] + nums[index+1])
    index += 1
  
  if (2 * index) < limit:
    nums[2 * index]=  nums[index]


  return maxN

if __name__ == "__main__":
  print(solve(7))
  print(solve(3))
  print(solve(2))