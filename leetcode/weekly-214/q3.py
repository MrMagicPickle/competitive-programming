# https://leetcode.com/contest/weekly-contest-214
# https://leetcode.com/contest/weekly-contest-214/problems/sell-diminishing-valued-colored-balls/

def findNext(maxN, aDict):
  while True:
    if maxN in aDict:
      break
    elif maxN == 0:
      break
    maxN -= 1     
    
  return maxN

def solve2(inventory, orders):
  inventory.sort(reverse=True)
  count = 0
  index = 0  
  if len(inventory) == 1:
    n = len(inventory)
    ans = n * orders
    neg = ((orders) * (orders + 1)) // 2
    count = ans - neg
    return count % 1000000007

  while orders > 0:
    val = inventory[index]
    
    count += val
    inventory[index] -= 1
    # print(inventory, index)
    if index == len(inventory) - 1:
      index = 0      
    elif inventory[index + 1] > inventory[index]:      
      index = index+1      
    else:
      index = 0
    orders -= 1
  return count % 1000000007


def solve(inventory, orders):
  aDict = {}
  maxN = 0
  for i in range (len(inventory)):
    x = inventory[i]
    maxN = max(x, maxN)
    aDict[x] = aDict.get(x, 0) + 1

  # print(aDict)
  count = 0
  while orders > 0:
    
    vals = aDict[maxN]
    # print(maxN, vals, aDict)
    vals -= 1
    aDict[maxN] = vals
    count += maxN
    aDict[maxN-1] = aDict.get(maxN-1, 0) + 1

    if vals == 0:
      maxN -= 1
      #maxN = findNext(maxN-1, aDict)

    orders -= 1
  if count > 1000000007:
    return count % 1000000007
  return count


if __name__ == "__main__":
  print(solve2([2,5], 4))
  print('<<')
  print(solve2([3,5], 6))
  print('<<')
  print(solve2([2,8,4,10,6], 20))
  print('<<')  