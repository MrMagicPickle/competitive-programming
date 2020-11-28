# https://leetcode.com/contest/biweekly-contest-40/problems/maximum-repeating-substring/
def solve(sequence, word):
  # find patt occ index
  occIndex = []
  k = 0
  for i in range (len(sequence) - len(word) + 1):
    sub = sequence[i:i+len(word)]
    if sub == word:
      occIndex.append(i)
      k = 1
  if k < 1:
    return 0
  
  for i in occIndex:
    n = len(word)
    count = 1    
    
    while True:               
      subLength = n * count
      if i + subLength > len(sequence):
        break
      
      sub = sequence[i:i+subLength]
      if sub != (word * count):
        break
      k = max(k, count)   
      count += 1
  return k
      
  

if __name__ == "__main__":
  print(solve('ababc', 'ab'))
  print(solve('ababc', 'ac'))