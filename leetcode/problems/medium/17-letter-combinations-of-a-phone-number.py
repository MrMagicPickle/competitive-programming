# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def solve(digits):
  if len(digits) == 0:
    return []
  aDict = {}
  aDict['2'] = ['a', 'b', 'c']
  aDict['3'] = ['d', 'e', 'f']
  aDict['4'] = ['g', 'h', 'i']
  aDict['5'] = ['j', 'k', 'l']
  aDict['6'] = ['m', 'n', 'o']
  aDict['7'] = ['p', 'q', 'r', 's']
  aDict['8'] = ['t', 'u', 'v']
  aDict['9'] = ['w', 'x', 'y', 'z']
  output = []
  
  def recursive_find(combination, nextDigits):
    if len(nextDigits) == 0:
      output.append(combination)
      return 
    currDigit = nextDigits[0]
    for letter in aDict[currDigit]:
      recursive_find(combination + letter, nextDigits[1:])

  recursive_find('', digits)
  return output

if __name__ == "__main__":
  print(solve('234'), len(solve('234')))
  