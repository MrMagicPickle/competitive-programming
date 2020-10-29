# https://www.hackerrank.com/contests/projecteuler/challenges/euler230/problem

valDict = {}

def solve(a, b, n):  
  valDict['a'] = a
  valDict['b'] = b

  if len(a) >= n:
    return a[n-1]
  if len(b) >= n:
    return b[n-1]

  occList = [[1, 0], [0, 1]]  
  occ = [1, 1]
  occList.append(occ)
  prevOcc = [0, 1]
  fibIteration = solve_aux(occList, n, occ, prevOcc, len(a), len(b))  

  # Fib(fibIteration) = Fib(fibIteration - 2) + Fib(fibIteration - 1)
  # n - len(Fib(fibIteration - 2)) <= len(Fib(fibIteratoin -1))

  bstTraverse(n - calcLen(occList[fibIteration-2], len(a), len(b)), occList, fibIteration - 1, len(a), len(b))
"""   count = 0  
  for i in range (len(accString)):
    char = accString[i]
    if char == 'a':
      val = len(a)
    else:
      val = len(b)    

    if count + val >= n:
      remainder = n - count
      expandedTarget = valDict[char]
      target = expandedTarget[remainder-1]
      print(target)
      break
    count += val  
 """

def bstTraverse(n, occList, currIndex, aLen, bLen):
  
  if currIndex == 1:
    print(currIndex, '<< index')
    myStr = valDict['b']
    print(myStr[n])
    return 
  elif currIndex == 2:
    print(currIndex, '<< index')
    myStr = valDict['a']
    print(n)
    print(myStr)
    print(myStr[n])
    return 

  if n < calcLen(occList[currIndex-2], aLen, bLen):
    bstTraverse(n, occList, currIndex-2, aLen, bLen)
  else:
    bstTraverse(n - calcLen(occList[currIndex-2], aLen, bLen), occList, currIndex-1, aLen, bLen)

def calcLen(occDict, aLen, bLen):
  return (occDict[0] * aLen) + (occDict[0] * bLen) 

def solve_aux(occList, n, occDict, prevOcc, aLen, bLen):  
  count = 2
  while True:
    if calcLen(occDict, aLen, bLen) >= n:
      return count

    count += 1
    tmp = [occDict[0], occDict[1]]
    occDict =  [occDict[0] + prevOcc[0], occDict[1] + prevOcc[1]]   
    occList.append(occDict) 
    prevOcc = tmp  

if __name__ == "__main__":
  questions = []
  nLines = int(input())
  for i in range(nLines):
    q = input()
    q = q.split()
    questions.append(q)
  
  for x in range(len(questions)):
    q = questions[x]
    solve(q[0], q[1], int(q[2]))
