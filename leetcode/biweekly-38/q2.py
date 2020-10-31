# 5540. Widest Vertical Area Between Two Points Containing No Points

""" Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area. """

def solve(points):
  xList = []
  for i in range (len(points)):
    xList.append(points[i][0])

  xList.sort()  
  maxGap = 0
  prevCurr = xList[0]
  for i in range (1, len(xList)):
    currX = xList[i]
    gap = currX - prevCurr
    if gap > maxGap:
      maxGap = gap
    prevCurr = currX
    
  return maxGap

if __name__ == "__main__":
  print(solve([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))