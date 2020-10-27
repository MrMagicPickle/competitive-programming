# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def checkMagazine(magazine, note):
  magDict = dict()
  magazineArr = magazine
  for i in range (len(magazineArr)):
    key = magazineArr[i]
    if key in magDict:
      magDict[key] += 1
    else:
      magDict[key] = 1
  
  noteArr = note  
  isNo = False
  for i in range (len(noteArr)):
    key = noteArr[i]
    if key not in magDict:
      print('No')
      isNo = True
      break
    else:
      if magDict[key] <= 0:
        print('No')
        isNo = True
        break
      else:
        magDict[key] -= 1        
  if not isNo:
    print('Yes')

if __name__ == "__main__":
  print('<<<')
  print(checkMagazine('ive got a lovely bunch of coconuts', 'ive got some coconuts'))
