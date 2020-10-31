# 5541. Count Substrings That Differ by One Character
# https://leetcode.com/contest/biweekly-contest-38/problems/count-substrings-that-differ-by-one-character/

""" Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string. """
""" 
Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.
​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t. """

def countDiff(t, s):
  count = 0
  print(len(t), len(s))
  for i in range (len(t)):
    if t[i] != s[i]:
      count += 1
  return count

def solve(s, t):
  count = 0
  aDict = {}  
  for i in range (1, len(s)):
    gap = i
    for j in range(len(s)):
      if j + gap < len(s):
        subS = s[j:j+gap]
        for k in range (len(t)):
          if k + gap < len(t):
            subT = t[k:k+gap]
            if subT != subS:
              print(subT, subS, j, k, gap)
              diff = countDiff(subT, subS)
              if diff == 1:
                count += 1
  return count
if __name__ == "__main__":
  print(solve('abe', 'bbc'))