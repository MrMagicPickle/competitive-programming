# https://www.hackerrank.com/contests/projecteuler/challenges/euler230/problem
def solve(a, b, n):  
  if len(a) >= n:
    return a[n-1]
  if len(b) >= n:
    return b[n-1]

  valDict = {}
  valDict['a'] = a
  valDict['b'] = b
  occ = [1, 1]
  prevOcc = [0, 1]
  accString = solve_aux('ab', 'b', n, occ, prevOcc, len(a), len(b))

  count = 0  
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

def calcLen(occDict, aLen, bLen):
  return (occDict[0] * aLen) + (occDict[0] * bLen) 

def solve_aux(acc, curr, n, occDict, prevOcc, aLen, bLen):  
  while True:
    if calcLen(occDict, aLen, bLen) >= n:
      return acc

    tmpAcc = acc
    print(acc)
    acc = curr+acc
    
    curr = tmpAcc

    tmp = [occDict[0], occDict[1]]
    occDict =  [occDict[0] + prevOcc[0], occDict[1] + prevOcc[1]]
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
