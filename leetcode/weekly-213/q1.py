# https://leetcode.com/contest/weekly-contest-213/problems/check-array-formation-through-concatenation/

def solve2(arr, pieces):
  pieceDict = {}
  for i in range (len(pieces)):
    piece = pieces[i]
    pieceDict[piece[0]] = piece

  i = 0 
  while i < len(arr):    
    currNum = arr[i]
    if currNum not in pieceDict:
      return False
    
    pieceArr = pieceDict[currNum]
    for k in range (len(pieceArr)):
      if pieceArr[k] != arr[i+k]:
        return False
    i += len(pieceArr)
  return True


def solve(arr, pieces):
  pieceDict = {}
  for i in range (len(pieces)):
    piece = pieces[i]
    pieceDict[piece[0]] = piece
  isSearch = False
  currPieceArr = None
  counter = 0
  for i in range (len(arr)):
    key = arr[i]
    if isSearch:
      if counter < len(currPieceArr):
        if key != currPieceArr[counter]:
          return False
        counter += 1
      else:
        counter = 1
        isSearch = False
      continue

    if key not in pieceDict:
      return False
    else:
      currPieceArr = pieceDict[key]
      if len(currPieceArr) > 1:
        isSearch = True
        counter = 1
      
  return True

if __name__ == "__main__":
  print(solve2([49,18,16], [[16,18,49]]))
  print(solve2([91,4,64,78], [[78],[4,64],[91]]))
  print(solve2([97,80,56,85,60,33,26,23,99,98,19,34,30,66],[[98,19],[23,99],[97,80,56,85,60],[33,26],[34],[30,66]]))