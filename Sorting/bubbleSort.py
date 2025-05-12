import time
import winsound
def bubbleSort(data,draw_initial,timeSpeed):
  for _ in range(len(data)-1):
    for j in range(len(data)-1):

      draw_initial(data, ["yellow" if x==j or x== j+1 else "#A90042" for x in range(len(data))])
      time.sleep(timeSpeed)
      
      if data[j] > data[j+1]:
        data[j],data[j+1]=data[j+1],data[j]

        draw_initial(data, ["green" if x==j or x== j+1 else "#A90042" for x in range(len(data))])
        time.sleep(timeSpeed)
  winsound.Beep(2500,300)
  draw_initial(data, ["green" for x in range(len(data))])

# data=[10,9,8,7,6,5,4,3,2,1]
# data=bubbleSort(data)
# print(data)
