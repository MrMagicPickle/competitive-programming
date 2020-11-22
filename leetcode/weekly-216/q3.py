def solve(nums):
  # prep arr
  even = [0] * len(nums)
  odd = [0] * len(nums)

  evenN = 0
  oddN = 0
  for i in range (len(nums)):
    if i % 2 == 0:
      evenN = nums[i]
      oddN = 0
    else:
      oddN = nums[i]
      evenN = 0
    if i == 0:
      even[i] = evenN
      odd[i] = oddN
      continue
    even[i] = evenN + even[i-1]
    odd[i] = oddN + odd[i-1]
  
  count = 0
  for i in range (len(nums)):
    # calc even
    if i == 0:
      preEven = 0
    else:
      preEven = even[i-1]
    postOdd = odd[len(nums)-1] - odd[i]
    evenSum = postOdd + preEven

    #calc odd
    if i == 0:
      preOdd = 0
    else:
      preOdd = odd[i-1]
    
    postEven = even[len(nums)-1] - even[i]
    oddSum = postEven + preOdd
    if oddSum == evenSum:
      # print('index fair at:', i)
      count += 1
  return count


if __name__ == "__main__"  :
  print(solve([1,2,3]))
