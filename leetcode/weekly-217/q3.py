# https://leetcode.com/contest/weekly-contest-217/problems/minimum-moves-to-make-array-complementary/
def solve(nums, limit):
  # occ = {}
  highest = 0
  comps = []
  
  minCount = 99999999
  for i in range (len(nums) // 2):
    comp = len(nums) - 1 - i
    summed = nums[comp] + nums[i]
    count = 0
    traversed = False
    for j in range (len(nums) // 2):
      subcomp = len(nums) - 1 - j
      subsummed = nums[subcomp] + nums[j]
      traversed = True
      # print(summed, subsummed, nums[subcomp], nums[j])
      if subsummed == summed:
        continue
      if limit + nums[j] >= summed or limit + nums[subcomp] >= summed:
        count += 1
      else:
        count += 2
    if traversed:
      if count < minCount:
        minCount = count
  return minCount
  # count = 0
  # for i in range (len(nums) // 2):
  #   comp = len(nums) - 1 - i
  #   summed = nums[comp] + nums[i]
  #   if summed == highest:
  #     continue
  #   if limit >= highest:
  #     count += 1
  #   else:
  #     count += 2
  # return count

if __name__ == "__main__":
  # print(solve([1,2,4,3], 4))
  print(solve([1,2,2,1], 2))
  # print(solve([1,2,1,2], 2))