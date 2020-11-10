# https://leetcode.com/problems/jump-game/

def solve(nums):
  if len(nums) == 1:
    return True
  if len(nums) == 2:
    if nums[0] >= 1:
      return True
    else:
      return False
  target = len(nums)-1  
  count = 1
  for i in range (len(nums)-2, -1 ,-1):
    n = nums[i]
    ok = False
    if n >= count:
      target = i
      count = 0
      ok = True
    count += 1    

  return ok

if __name__ == "__main__":
  print(solve([2,3,1,1,4]))
  print('<<')
  print(solve([3,2,1,0,4]))
