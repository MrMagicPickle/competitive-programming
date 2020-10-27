# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def makeAnagram(a, b):
  
  aDict = {}
  for i in range (len(a)):
    aDict[a[i]] = aDict.get(a[i], 0) + 1

  bDict = {}  
  for i in range (len(b)):    
    key = b[i]
    bDict[key] = bDict.get(key, 0) + 1

  
  count = 0 
  for key in aDict:
    if key not in bDict:
      count += aDict[key]
    else:
      if aDict[key] > bDict[key]:
        count += aDict[key] - bDict[key]
      
  for key in bDict:
    if key not in aDict:
      count += bDict[key]
    else:
      if bDict[key] > aDict[key]:
        count += bDict[key] - aDict[key]
  
  return count

  
if __name__ == "__main__":
  print('<<<')
  print(makeAnagram('cde', 'abc'))