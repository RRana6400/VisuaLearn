from tkinter import *
import winsound
def sorting_dashboard(pre_root):

  
  from tkinter import ttk
  import random
  import Sorting.bubbleSort as bs
  import Sorting.selectionSort as ss
  import Sorting.quickSort as qs
  import Sorting.mergeSort as ms
  import customtkinter as ctk


  pre_root.withdraw()
  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("blue")
  root=ctk.CTk()
  root.title("VisuaLearn || Sorting Algorithms")
  root.geometry("1000x700")
  root.resizable(width=False, height=False)

    # Creation of main frame
  ## main frame 1
  main_frame1 = ctk.CTkFrame(root, corner_radius=25,width=1000, height=500 )
  main_frame1.grid(row=0, column=0, padx=50, pady=5)

  ## main frame 2
  main_frame2 = ctk.CTkFrame(root, corner_radius=25,width=900, height=180 )
  main_frame2.grid(row=1, column=0, padx=50, pady=5, sticky="ew")

  #main frame 3
  main_frame3 = ctk.CTkFrame(main_frame2, corner_radius=25,width=200, height=170 )
  main_frame3.grid(row=0, column=0, padx=5, pady=5)

  #main frame 4
  main_frame4 = ctk.CTkFrame(main_frame2, corner_radius=25,width=680, height=170 )
  main_frame4.grid(row=0, column=1, padx=5, pady=5, sticky="news")




  #draw_function
  def draw_initial(data, colour_bars):
    canvas.delete("all")
    canvas_height = 500
    canvas_width = 1000
    x_width=canvas_width/(len(data)+1)
    offset=10
    bars_spacing=10
    normalised_data= (i / max(data) for i in data)

    for i, height in enumerate(normalised_data):
      x0 = i*x_width +offset+bars_spacing
      y0=canvas_height-height*400

      x1=(i+1)*x_width
      y1=canvas_height

      canvas.create_rectangle(x0,y0,x1,y1,fill=colour_bars[i])
      canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]), font=("new roman",15,"bold"), fill="orange")
    #for visualization
    root.update_idletasks()


  #Start_ALgorithm.....
  def Start_Algo():
    global data
    if not data:
      return
    
    if(sort_menu.get() == "Quick Sort"):
      qs.quickSort(data, 0, len(data)-1, draw_initial, 5-speed.get())
      winsound.Beep(2500,300)
      draw_initial(data, ["green" for x in range(len(data))])
    elif sort_menu.get() == "Bubble Sort":
      bs.bubbleSort(data,draw_initial,5-speed.get())
    elif sort_menu.get() == "Selection Sort":
      ss.selection_sort(data,draw_initial,5-speed.get())
    elif sort_menu.get() == "Merge Sort":
      ms.merge_Sort(data,draw_initial,5-speed.get())

  #generate_function
  def Generate():
    global data
    min_value=int(minValue.get())
    max_value=int(maxValue.get())
    size_value=int(sizeValue.get())
    
    data=[]
    for _ in range(size_value):
      data.append(random.randrange(min_value, max_value+1))

    draw_initial(data,["#A90042" for x in range(len(data))])

    
  #main label --Algorithm
  mn_label = ctk.CTkLabel(master=main_frame4,text="Algorithm:", font=ctk.CTkFont("new roman", size=16,weight= "bold"),bg_color="green", width=10, corner_radius=30  )
  mn_label.grid(row=0, column=0,padx=5, pady=20)



  #list of sorting algorithms
  selected_algorithm = StringVar()
  sort_menu = ctk.CTkComboBox(main_frame4,width=200,border_width=2, font=("new roman", 19, "bold"), variable=selected_algorithm, values=['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort'])
  sort_menu.grid(row=0, column=1,padx=5,pady=5)

  # Generate btn
  generate_rdm = ctk.CTkButton(main_frame3, text="Generate", font= ("arial",30,"bold"),fg_color="orange",hover_color="dark orange",height=15, width=30, command=Generate)
  generate_rdm.grid(row=1, column=0,padx=5, pady=20, sticky="ew")


  #size label
  size_of_array_label = ctk.CTkLabel(main_frame4, text="Size: ", font= ctk.CTkFont("new roman", size=16, weight="bold"), bg_color="green", width= 10)
  size_of_array_label.grid(row=2, column=0, padx=5,pady=20, sticky="news")
  #range of size of array
  sizeValue = ctk.CTkSlider(main_frame4, from_=0, to=30,  orientation=HORIZONTAL,  width=100, )
  sizeValue.grid(row=2, column=1, padx=5, pady=20, sticky="news")



  #min label
  min_label = ctk.CTkLabel(main_frame4, text="Minimum: ", font= ctk.CTkFont("new roman", size=16, weight="bold"), bg_color="green", width= 10)
  min_label.grid(row=2, column=2, padx=5,pady=20, sticky="news")
  #range of size of array
  minValue = ctk.CTkSlider(main_frame4, from_=0, to=30,  orientation=HORIZONTAL,  width=100, )
  minValue.grid(row=2, column=3, padx=5, pady=20, sticky="news")

  #max label
  max_label = ctk.CTkLabel(main_frame4, text="Maximum: ", font= ctk.CTkFont("new roman", size=16, weight="bold"), bg_color="green", width= 10)
  max_label.grid(row=2, column=4, padx=5,pady=20, sticky="news")
  #range of size of array
  maxValue = ctk.CTkSlider(main_frame4, from_=0, to=30,  orientation=HORIZONTAL,  width=100, )
  maxValue.grid(row=2, column=5, padx=5, pady=20, sticky="news")

  #start button
  start_btn = ctk.CTkButton(main_frame3, text="START", font= ("arial",30,"bold"),height=15, width=30, command=Start_Algo)
  start_btn.grid(row=0, column=0,padx=5, pady=25, sticky="ew")


  #speed label
  speed_label = ctk.CTkLabel(main_frame4, text="Speed: ", font= ctk.CTkFont("new roman", size=16, weight="bold"), bg_color="green", width= 10)
  speed_label.grid(row=1, column=0, padx=5,pady=5, sticky="news")
  #range of speed of array
  speed = ctk.CTkSlider(main_frame4, from_=0, to=5,  orientation=HORIZONTAL,  width=100, )
  speed.grid(row=1, column=1, padx=5, pady=5, sticky="news")



  #canvas
  canvas = Canvas(main_frame1, width=1000, height=500, background="black")
  canvas.grid(row=0, column=0,padx=50, pady=50, sticky="news")

  root.mainloop()
