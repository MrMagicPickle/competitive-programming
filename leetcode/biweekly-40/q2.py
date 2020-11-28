# https://leetcode.com/contest/biweekly-contest-40/problems/merge-in-between-linked-lists/
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def solve(list1, a, b, list2):
  # traverse list 1
  node = list1
  index = 0
  while node is not None:
    if index == a-1:
      startNode = node
    if index == b:
      endNode = node.next      
    node = node.next
    index += 1

  startNode.next = list2

  # traverse list 2
  node = list2  
  while node.next is not None:
    node = node.next
  node.next = endNode
  return list1

def printList(alist):
  node = alist
  while node is not None:
    print(node.val)
    node = node.next

if __name__ == "__main__":
  list1a = [0,1,2,3,4,5]
  # list1a = [0,1,2,3,4,5,6]
  list2a = [1000000,1000001,1000002]
  # list2a = [1000000,1000001,1000002,1000003,1000004]
  a = 3 
  b = 4 
  # a = 2
  # b = 5  
  list1 = ListNode(list1a[0])
  node = list1
  for i in range (1, len(list1a)):
    node.next = ListNode(list1a[i])
    node = node.next
  list2 = ListNode(list2a[0])
  node = list2
  for i in range (1, len(list2a)):
    node.next = ListNode(list2a[i])
    node = node.next
  
  # printList(list1)
  # printList(list2)
  printList(solve(list1, a, b, list2))