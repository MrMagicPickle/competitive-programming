def solve(tasks):
  tasks.sort()
    
  aDict = {}
  dups = {}
  for i in range (len(tasks)):
    task = tasks[i]
    actual = task[0]
    if actual in aDict:
      aDict[actual].append(i)
    else:
      aDict[actual] = [i]
  # print(aDict)
  energy = 0
  remainder = 0
  prevRemainder = 0
  i = 0 
  # print(tasks)
  while i < len(tasks):
      
    x = tasks[i]
    actual = x[0]
    minEnergy = x[1]

    arrs = aDict[actual]        
    if len(arrs) <= 1:
      remainder = minEnergy - actual
      if i == 0:
        energy = minEnergy        
      else:        
        energy += minEnergy - prevRemainder
      i += 1
      prevRemainder = remainder
      # print(energy,remainder, actual, minEnergy)
    else:
      # print('In j <<<<')
      j = i + len(arrs) - 1
      
      while j >= i:
        x = tasks[j]        
        actual = x[0]
        minEnergy = x[1]
        remainder = minEnergy - actual        
        if j == 0:
          energy = minEnergy
        else:
          energy += minEnergy - prevRemainder                  
        prevRemainder = remainder

        # print(energy, remainder)
        j -= 1
      i += len(arrs)
      # print('>>>')
  return energy


if __name__ == "__main__"  :
  # print(solve([[1,2],[2,4],[4,8]]))
  # print('<<<')
  print(solve([[1,2],[2,4],[4,8]]))
  # print('<<<')
  # print(solve([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))