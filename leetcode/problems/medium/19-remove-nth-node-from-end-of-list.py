# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next  

def printList(root):
  node = root
  while node is not None:
    print(node.val)
    node = node.next

def solve(head, n):  
  node = head
  nodeList = []
  length = 0
  while node is not None:
    nodeList.append(node)
    node = node.next    
    length += 1
  
  if length == 1:
    if n == 1:
      head = None
      return head

  remove = length - n  
  if remove == 0:
    head = head.next
  else:
    prev = nodeList[remove-1]
    
    if (remove+1) < length:
      next = nodeList[remove+1]
    else:
      next = None
    prev.next = next
  
  return head

if __name__ == "__main__":
  a = [1]
  root = ListNode(a[0])
  node = root
  for i in range (1, len(a)):
    new = ListNode(a[i])
    node.next = new
    node = node.next

  head = solve(root, 2)
  printList(head)  
  