def solve(word1, word2):
  s1 = ''
  s2 = ''
  for x in word1:
    s1 += x
  for x in word2:
    s2 += x
  return s1 == s2

if __name__ == "__main__":
  print(solve(["abc", "d", "defg"], ["abcddefg"]))
