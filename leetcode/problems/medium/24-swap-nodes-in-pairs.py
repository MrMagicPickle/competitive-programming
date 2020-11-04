# https://leetcode.com/problems/swap-nodes-in-pairs/

class Node: 
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def solve_aux(head):
  if head is None or head.next is None:
    return head
  tmp = head.next
  head.next = solve_aux(head.next.next)
  tmp.next = head
  return tmp

def solve(head):
  if head is None:
    return head
  if head.next is None:
    return head
  return solve_aux(head)

def printList(root):
  node = root
  while node is not None:
    print(node.val)
    node = node.next    
   
if __name__ == "__main__"   :
  a = [1,2,3,4,5,6,7]
  root = Node(a[0])      
  node = root
  for i in range (1, len(a)):
    new = Node(a[i])
    node.next = new
    node = node.next
    i += 1
  #printList(root)
  a = solve(root)
  printList(a)


