# https://www.hackerrank.com/certificates/17f5da938c57

#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(freq):
    # Write your code here
    remainder = 0
    total = 0
    for i in range (len(freq)):
      curr = freq[i]
      count = (curr + remainder) // 2
      nextRemainder = (curr + remainder) % 2
      if nextRemainder == 0:
        remainder = remainder
      else:
        if curr != 0:
          remainder = remainder
      total += count            
    return total

if __name__ == "__main__":
  
  ans = taskOfPairing([3, 5, 7])
  print('<<<')
  print(ans)