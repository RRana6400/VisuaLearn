import time
import winsound
def selection_sort(data,draw_initial, time_speed):
  for i in range(len(data)-1):
    minIdx=i

    for j in range (i+1, len(data)):


      if(data[minIdx] > data[j]):
        minIdx=j
    data[i], data[minIdx] = data[minIdx], data[i]
    draw_initial(data, ["green"  if x<i   else ("blue" if x==minIdx or x==i else "#A90042") for x in range(len(data))])
    time.sleep(time_speed)
  winsound.Beep(2500,300)
  draw_initial(data, ["green" for x in range(len(data))])

