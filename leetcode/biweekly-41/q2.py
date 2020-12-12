# https://leetcode.com/contest/biweekly-contest-41/problems/sum-of-absolute-differences-in-a-sorted-array/

def solve(nums):
  post = 0
  for i in range (len(nums)):
    post += nums[i]

  pre = 0 
  res = []
  for i in range (len(nums)):
    n = nums[i]
    post -= n
    back = (n * i) - pre
    front = post - (n * (len(nums) - i - 1))
    res.append(back+front)    
    pre += n
    
  return res

if __name__ == "__main__":
  # ans = solve([2,3,5])
  ans = solve([1,4,6,8,10])
  print(ans)