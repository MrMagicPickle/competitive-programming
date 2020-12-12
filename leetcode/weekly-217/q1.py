def solve(accounts):  
  maxWealth = 0
  for i in range (len(accounts)):
    acc = accounts[i]
    wealth = 0
    for j in range (len(acc)):
      wealth += accounts[i][j]
    if wealth > maxWealth:
      maxWealth = wealth
  return maxWealth

if __name__ == "__main__":
  print(solve([[2,8,7], [7,1,3], [1,9,5]]))