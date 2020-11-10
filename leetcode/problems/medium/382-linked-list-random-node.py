# https://leetcode.com/problems/linked-list-random-node/
from random import randint

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:

  def __init__(self, head: ListNode):
    """
    @param head The linked list's head.
    Note that the head is guaranteed to be not null, so it contains at least one node.
    """
    self.head = head
    node = head
    count = 0
    while node is not None:
      count += 1
      node = node.next
    self.length = count
    

  def getRandom(self) -> int:
    """
    Returns a random node's value.
    """
    randomIndex = randint(0, self.length-1)
    node = self.head
    count = 0        
    while node is not None:
      if count == randomIndex:
        return node.val
      node = node.next      
      count += 1            

if __name__ == "__main__":
  alist = [1,2,3]
  root = ListNode(alist[0])
  xd = root
  for i in range (1, len(alist)):
    xd.next = ListNode(alist[i])
    xd = xd.next
  
  solution = Solution(root)
  print(solution.getRandom())