# https://leetcode.com/contest/biweekly-contest-38/ranking/
# 5539. Sort Array by Increasing Frequency

""" Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array. """
def solve(nums):
  aDict = {}
  for i in range (len(nums)):
    num = nums[i]
    aDict[num] = aDict.get(num, 0) + 1  

  sortedItems = {k: v for k, v in sorted(aDict.items(), key=lambda item: item[1])}
  
  firstSortKeys = list(sortedItems.keys())
  firstSort = []
  for i in range (len(firstSortKeys)):
    key = firstSortKeys[i]
    arr = [key] * aDict[key]
    firstSort += arr

  miniDict = {}
  isIdentical = False
  prevKey = None
  ans = []
  print(firstSort, firstSortKeys)
  for i in range (len(firstSortKeys)):
    key = firstSortKeys[i]
    freq = aDict[key]
    if prevKey is not None:
      # check if identical
      prevFreq = aDict[prevKey]
      if prevFreq == freq:
        if not isIdentical:
          ans.pop()
        isIdentical = True
        miniDict[prevKey] = prevFreq
        miniDict[key] = freq
      else:
        isIdentical = False        

    if not isIdentical:
      if len(list(miniDict.keys())) == 0:
        ans.append(key)
      else:        
        ans = ans + sorted(miniDict, reverse=True)
        miniDict = {}
        ans.append(key)
    print(ans, '<< ', i)
    prevKey = key

  
  if len(list(miniDict.keys())) > 0:
    ans = ans + sorted(miniDict, reverse=True)
    
  actual = []
  for i in range (len(ans)):
    anum = ans[i]
    freq = aDict[anum]
    arr = [anum] * freq
    actual += arr

  return actual


if __name__ == "__main__":
  #print(solve([2, 3, 1, 3, 2]))
  print(solve([-1,1,-6,4,5,-6,1,4,1]))