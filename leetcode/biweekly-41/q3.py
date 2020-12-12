# https://leetcode.com/contest/biweekly-contest-41/problems/stone-game-vi/

def solve(aliceValues, bobValues):
  gapValues = []
  for i in range (len(aliceValues)):
    gapValues.append([aliceValues[i] + bobValues[i], i])
  gapValues = sorted(gapValues, reverse=True)
  
  aliceScore = 0
  bobScore = 0
  for i in range (len(gapValues)):
    val = gapValues[i][0]
    index = gapValues[i][1]
    if i % 2 == 0:
      # Alice Turn
      aliceScore += aliceValues[index]
    else:
      bobScore += bobValues[index]
  print(aliceScore, bobScore)

  if aliceScore > bobScore:
    return 1
  elif bobScore > aliceScore: 
    return -1
  else:
    return 0


if __name__ == "__main__":
  print(solve([1,3], [2,1]))
  print('<<')
  print(solve([1,2], [3,1]))
  print('<<')
  print(solve([2,4,3], [1,6,7]))