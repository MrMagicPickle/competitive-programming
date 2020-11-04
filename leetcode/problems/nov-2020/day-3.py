# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3517/

class PrevNode:
  def __init__(self, node, prev):
    self.node = node
    self.prev = prev

class Node:
  def __init__(self, val, next):
    self.val = val
    self.next = next

def printList(root, count):
  node = root
  while node is not None:
    print(node.val, count)
    node = node.next

def solve(head):
  node = head      
  currPrevNode = None
  count = 0
  innerCount = 0
  
  while node is not None:    
    newPrevNode = PrevNode(node, currPrevNode)
    currPrevNode = newPrevNode
    val = node.val    
    nextNode = node.next
    aNode = currPrevNode
    printList(head, count)          
    while aNode.prev is not None:
      if aNode.prev.node.val <= val:
        if aNode.prev.node.next != node:
          oriNext = aNode.prev.node.next
          aNode.prev.node.next = node
          node.next = oriNext
      aNode = aNode.prev  
    count += 1
    node = nextNode
  
  """ iterNode = head
  while iterNode is not None:
    print(iterNode.val)
    iterNode = iterNode.next """

if __name__ == "__main__":
  a = [1,3,4,2]
  node = Node(a[0], None)
  currNode = node
  for i in range (1, len(a)):
    print(a[i])
    currNode.next = Node(a[i], None)
    currNode = currNode.next
  
  aNode = node
  print('<<')
  while aNode is not None:
    print(aNode.val)
    aNode = aNode.next
  solve(node)