# https://leetcode.com/contest/weekly-contest-217/problems/find-the-most-competitive-subsequence/

def solve(nums, k):
  out = []
  mins = [10000000000] * k
  
  def gen(seq, arr):
    nonlocal mins
    if (len(seq)) == k:
      out.append(seq)
      smaller = False
      for j in range (len(mins)):
        if seq[j] < mins[j]:
          smaller = True          
        elif seq[j] > mins[j]:
          break
      if smaller:        
        mins = seq
      return
    if len(arr) == 0:
      return

    for i in range(len(arr)):
      n = arr[i]      
      if i+1 < len(arr):
        gen(seq + [n], arr[i+1:])
      else:
        gen(seq + [n], [])

  gen([], nums)
  # print(out)
  return mins

def solve2(nums, k):
  alist = []  
  if k == len(nums):  
    return nums    
  
  minIndex = -1
  startIndex = 0  
  while k > 0:
    minN = 10000000000    
    endIndex = len(nums) - k + 1
    for i in range (startIndex, endIndex):
      if nums[i] < minN:
        minIndex = i
        minN = nums[i]    
    alist.append(minN)
    startIndex = minIndex + 1
    k -= 1
  return alist

if __name__ == "__main__":
  print(solve2([3,5,2,6], 2))
  print(solve2([2,4,3,3,5,4,9,6], 4))

  alist = [0] * 50000
  k = 50000
  print(solve2(alist, k))

