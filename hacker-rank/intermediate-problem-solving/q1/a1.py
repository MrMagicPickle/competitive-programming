# https://www.hackerrank.com/certificates/17f5da938c57

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#
def findNewLargeIndex(arr):
  largestIndex = 0
  for i in range (len(arr)):
    val = arr[i]
    if val > arr[largestIndex]:
      largestIndex = i
  return largestIndex

def getMaxArea(w, h, isVertical, distance):
  # Write your code here
  nLines = len(isVertical)  

  heightArr = [h]  
  widthArr = [w]
  answer = []
  
  wlargestIndex = 0
  hlargestIndex = 0
  for i in range(len(isVertical)):
    if isVertical[i] == 1:
      # Vertical -- affects width
      newWidthArr = []
      vDistance = distance[i]    
      totalDistance = 0
      for j in range (len(widthArr)):
        currDistance = widthArr[j]
        
        if (vDistance - totalDistance) <=  currDistance:
          # This is the location to update
          splitVal1 = vDistance - totalDistance
          splitVal2 = currDistance - (vDistance - totalDistance)
          newWidthArr.append(splitVal1)
          newWidthArr.append(splitVal2)

          if j < len(widthArr)-1:
            newWidthArr += widthArr[j+1:]

          if j == wlargestIndex:
            wlargestIndex = findNewLargeIndex(newWidthArr)            
          break        
        totalDistance += currDistance
        newWidthArr.append(currDistance)
      widthArr = newWidthArr
      answer.append(widthArr[wlargestIndex] * heightArr[hlargestIndex])
    else:
      # Horizontal
      hDistance = distance[i]
      # Vertical -- affects width
      newHeightArr = []
      hDistance = distance[i]    
      totalDistance = 0
      for j in range (len(heightArr)):
        currDistance = heightArr[j]
        
        if (hDistance - totalDistance) <=  currDistance:
          # This is the location to update
          splitVal1 = hDistance - totalDistance
          splitVal2 = currDistance - (hDistance - totalDistance)
          newHeightArr.append(splitVal1)
          newHeightArr.append(splitVal2)
          
          if j < len(heightArr)-1:
            newHeightArr += heightArr[j+1:]

          if j == hlargestIndex:
            hlargestIndex = findNewLargeIndex(newHeightArr)            
          break        
        totalDistance += currDistance
        newHeightArr.append(currDistance)
      heightArr = newHeightArr
      answer.append(widthArr[wlargestIndex] * heightArr[hlargestIndex])
  return answer

if __name__ == '__main__':
  pass