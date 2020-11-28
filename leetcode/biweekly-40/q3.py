class FrontMiddleBackQueue:
  def __init__(self):
    self.arr = [None] * 10000
    self.frontStart = 0
    self.front = 0
    self.middleStart = 4000
    self.middle = 4000
    self.endStart = 7500
    self.end = 7500
    self.count = 0
    self.frontCount = 0 
    self.endCount = 0

  def pushFront(self, val: int) -> None:
    self.arr[self.front] = val
    self.front += 1

    self.frontCount += 1
    self.count += 1

  def pushMiddle(self, val: int) -> None:
    middle = self.count // 2
    if middle <= self.front:      
      # Shift all to the right
      currVal = self.arr[middle]
      for i in range (middle, self.front):
        nextVal = self.arr[i + 1]
        self.arr[i+1] = currVal
        currVal = nextVal                
      self.arr[middle] = val
      self.front += 1
      
    else:
      index = middle - self.front
      target = self.endStart + index
      # Shift all to the right
      currVal = self.arr[target]
      for i in range (target, self.end):
        nextVal = self.arr[i + 1]
        self.arr[i+1] = currVal
        currVal = nextVal                

      self.arr[target] = val
      self.end += 1      
    self.count += 1

  def pushBack(self, val: int) -> None:
    self.arr[self.end] = val
    self.end += 1

    self.count += 1
    self.endCount += 1

  def popFront(self) -> int:
    x = self.arr[self.frontStart]
    if x is not None:
      self.frontStart += 1
      return x
    # x = self.arr[self.middleStart]
    # if x is not None:
    #   self.middleStart += 1
    #   return x
    x = self.arr[self.endStart]
    if x is not None:
      self.endStart += 1
      return x
    return -1

  def popMiddle(self) -> int:
    middle = self.count // 2
    if middle <= self.front: 
      x = self.arr[middle]     

      # Shift all to the left      
      for i in range (middle, self.front):
        self.arr[i] = self.arr[i+1]
      
      self.front -= 1            
    else:
      index = middle - self.front
      target = self.endStart + index
      x = self.arr[target]
      # Shift all to the left      
      for i in range (target, self.end):
        self.arr[i] = self.arr[i+1]                        
      self.end -= 1      
    self.count -= 1    
    if x is None:
      return -1
    return x

  def popBack(self) -> int:
    x = self.arr[self.end]
    if x is not None:
      self.end -= 1
      return x
    # x = self.arr[self.middle]
    # if x is not None:
    #   self.middle -= 1
    #   return x
    x = self.arr[self.front-1]
    if x is not None:
      self.front -= 1
      return x
    return -1

  def getList(self):
    alist = []
    for i in range(self.front):
      alist.append(self.arr[i])

    for i in range(self.endStart, self.end):
      alist.append(self.arr[i])
    return alist
if __name__ == "__main__":    
  pass
  # Your FrontMiddleBackQueue object will be instantiated and called as such:
  obj = FrontMiddleBackQueue()
  
  obj.pushFront(1)
  obj.pushBack(2)  
  obj.pushMiddle(3)
  obj.pushMiddle(4)
  xd = obj.getList()
  print(xd)
  print(obj.popFront())
  print(obj.popMiddle())
  print(obj.popMiddle())
  print(obj.popBack())
  print(obj.popFront())  
  # for i in range (3):
  #   print(obj.popMiddle())
  