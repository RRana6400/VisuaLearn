import time
import winsound
def merge_Sort(data, draw_initial, time_speed):
  mergeSortAlgo(data, 0, len(data)-1, draw_initial, time_speed)
  for i in range(2):
    winsound.Beep(2500,300)
    time.sleep(0.05)

def mergeSortAlgo(data, left, right, draw_initial, time_speed):
  if(left < right):
    mid= (left+right)//2
    mergeSortAlgo(data, left, mid, draw_initial, time_speed )
    mergeSortAlgo(data, mid+1, right, draw_initial, time_speed )
    merge(data, left, mid, right, draw_initial, time_speed)

def merge(data, left, mid, right, draw_initial, time_speed):
  draw_initial(data, colour_bar(len(data), left, mid, right))
  time.sleep(time_speed)

  leftPart = data[left:mid+1]
  rightPart = data[mid+1: right+1]

  leftIdx = rightIdx = 0

  for dataIdx in range(left, right+1):
    if(leftIdx < len(leftPart) and rightIdx < len(rightPart)):
      
      if(leftPart[leftIdx] <= rightPart[rightIdx]):
        data[dataIdx] = leftPart[leftIdx]
        leftIdx += 1
      else:
        data[dataIdx] = rightPart[rightIdx]
        rightIdx+=1

    elif leftIdx < len(leftPart):
      data[dataIdx]= leftPart[leftIdx]
      leftIdx+=1

    else:
      data[dataIdx] = rightPart[rightIdx]
      rightIdx+=1
  draw_initial(data, ["green" if x>=left and x<=right else "white" for x in range(len(data))])
  time.sleep(time_speed)

def colour_bar(data_length, left, mid, right):
  colorArray=[]

  for i in range(data_length):
    if(i >= left and i <= right):
      if( i>= left and i <= mid):
        colorArray.append("yellow")
      else:
        colorArray.append("brown")
    else:
      colorArray.append("white")
  return colorArray