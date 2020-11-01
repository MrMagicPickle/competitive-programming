# https://leetcode.com/contest/weekly-contest-213/problems/furthest-building-you-can-reach/

def solve(heights, bricks, ladders):
  if bricks == 0 and ladders == 0:
    if len(heights) >= 2:
      if heights[1] < heights[0]:
        return 1
      return 0
  ladderDict = {}
  ladderCount = 0
  prevHeight = heights[0]
  diffArr = []
  for i in range (1, len(heights)):
    height = heights[i]
    diffArr.append(prevHeight - height)
    prevHeight = heights[i]
  
  end = 0
  nextHighest = 0  
  ladderList = []
  for i in range (len(diffArr)):
    
    diff = diffArr[i]
    if diff < 0:
      absDiff = abs(diff)
      if ladderCount < ladders:
        ladderList.append([absDiff, i])
        ladderList.sort(reverse=True)
        nextHighest = ladderList[len(ladderList)-1][0]
        ladderCount += 1
      else:        

        if absDiff > nextHighest and len(ladderList) > 0:
          dec = ladderList.pop()
          ladderList.append([absDiff, i])
          ladderList.sort(reverse=True)
          nextHighest = ladderList[len(ladderList)-1][0]
          bricks -= dec[0]
          if bricks < 0:
            break
        else:
          bricks -= absDiff
          if bricks < 0:
            break
    end = i
    

  return end + 1

if __name__ == "__main__":
  print(solve([4,2,7,6,9,14,12], 5, 1))
  print(solve([4,12,2,7,3,18,20,3,19], 10, 2))
  print(solve([14,3,19,3], 17, 0))
  print(solve([1, 2], 0, 0))