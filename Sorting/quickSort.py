import time

def partition(data, head, tail, draw_initial, time_speed):
  initial=head
  pivot=data[tail]

  draw_initial(data, colourBar(len(data), head, tail, initial, initial))
  time.sleep(time_speed)

  for j in range(head, tail):
    if(data[j] < pivot):
      draw_initial(data, colourBar(len(data), head, tail, j, True))
      time.sleep(time_speed)
  
      data[initial],data[j] = data[j], data[initial]
      initial +=1
    
    draw_initial(data, colourBar(len(data), head, tail, initial, j))
    time.sleep(time_speed)
  
  draw_initial(data, colourBar(len(data), head, tail, initial, tail, True))
  time.sleep(time_speed)
  data[initial],data[tail] = data[tail], data[initial]
  return initial

def quickSort(data, head, tail, draw_initial, time_speed):
  if( head< tail):
    pivot = partition(data, head, tail, draw_initial, time_speed )
    quickSort(data, head, pivot-1, draw_initial, time_speed)
    quickSort(data, pivot+1, tail, draw_initial, time_speed)

def colourBar(data_length, head, tail, initial, curridx, isSwapping= False):
  colorBar=[]

  for i in range(data_length):

    if i>= head and i<=tail:
      colorBar.append("gray")
    else:
      colorBar.append("white")
    
    if(i== tail):
      colorBar[i]=='orange'
    elif (i == initial) :
      colorBar[i]=='red'
    elif (i==curridx):
      colorBar[i]=='yellow'
    
    if(isSwapping):
      if(i==initial or i == curridx):
        colorBar[i]= 'green'
  return colorBar
      



# data = [10,9,8,7,6,5,4,3,2,1]
# quickSort(data, 0, len(data)-1, 0,0)
# print(data)