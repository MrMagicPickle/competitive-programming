# https://leetcode.com/problems/zigzag-conversion/

def solve(s, numRows):
  if numRows == 1:
    return s
  mat = [''] * numRows

  pointer = 0  
  back = False
  for i in range (len(s)):
    char = s[i]    
    mat[pointer] += char
    if pointer == numRows - 1:
      back = True
      
    if pointer == 0:
      back = False
    if back:
      pointer -= 1      
    else:
      pointer += 1

  endStr = ''
  for i in range (len(mat)):    
    endStr += mat[i]
  return endStr

if __name__ == "__main__":
  print(solve('PAYPALISHIRING', 4))