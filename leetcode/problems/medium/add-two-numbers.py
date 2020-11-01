# https://leetcode.com/problems/add-two-numbers/

def solve(l1, l2):
  node1 = l1
  str1 = ''
  while node1 is not None:
    val = str(node1.val)
    node1 = node1.next
    str1 = val + str1
  num1 = int(str1)

  node2 = l2
  str2 = ''
  while node2 is not None:
    val = str(node2.val)
    node2 = node2.next
    str2 = val + str2
  num2 = int(str2)
  
  ans = num1 + num2  

  ansStr = str(ans)
  rootNode = ListNode(ansStr[-1])
  currNode = rootNode
  for i in range (len(ansStr)-2, -1, -1):
    char = ansStr[i]
    charNode = ListNode(char)
    currNode.next = charNode
    currNode = currNode.next
  return rootNode


if __name__ == "__main__":
