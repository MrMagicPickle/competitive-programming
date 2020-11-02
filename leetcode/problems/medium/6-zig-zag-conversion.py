# https://leetcode.com/problems/zigzag-conversion/

def solve(s, numRows):
  if numRows == 1:
    return s
  mat = []
  for i in range(numRows):
    mat.append([0] * len(s))

  pointer = 0
  rowPointer = 0 
  back = False
  for i in range (len(s)):
    char = s[i]    
    mat[pointer][rowPointer] = char
    if pointer == numRows - 1:
      back = True
      
    if pointer == 0:
      back = False
    if back:
      pointer -= 1
      rowPointer += 1
    else:
      pointer += 1

  endStr = ''
  for i in range (len(mat)):    
    for j in range (len(mat[i])):
      if mat[i][j] != 0:
        endStr += mat[i][j]
  return endStr

if __name__ == "__main__":
  print(solve('AB', 1))