import customtkinter as ctk
import tkinter as tk
from PIL import Image
from Sorting import sorting
from Sorting import bubbleSort
import graph.graph as graph

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def main_dashboard(root1):
  root1.withdraw()
  root = ctk.CTk()

  root.title("VisuaLearn")
  root.geometry("800x500")
  root.resizable(width=False, height=False)
  # Configure grid layout 
  root.grid_columnconfigure(0, weight=1)
  root.grid_rowconfigure(0, weight=1)

  def to_graph_dashboard():
    visualize = graph.GraphVisualizer()
    root.withdraw()
    visualize.run()

  def to_Sorting_dashboard():
    sorting.sorting_dashboard(root)
  # Creation of main frame
  # ## main frame 1
  # main_frame1 = ctk.CTkFrame(root, corner_radius=25, )
  # main_frame1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
  # main_frame1.grid_columnconfigure(0, weight=1)
  # main_frame1.grid_rowconfigure(0, weight=1)
  ## main frame 2
  main_frame2 = ctk.CTkFrame(root, corner_radius=25, )
  main_frame2.grid(row=0, column=0, padx=20, pady=5, sticky='nsew')
  main_frame2.grid_columnconfigure(0, weight=1)
  main_frame2.grid_rowconfigure(0, weight=1)
  ## main frame 3
  main_frame3 = ctk.CTkFrame(root, corner_radius=25, )
  main_frame3.grid(row=1, column=0, padx=20, pady=30, sticky='nsew')
  main_frame3.grid_columnconfigure(0, weight=1)
  main_frame3.grid_rowconfigure(0, weight=1)



  main_label = ctk.CTkLabel(main_frame3, text="What do you want to learn, today ?", font=ctk.CTkFont(size=20, weight="bold"),text_color="white")
  main_label.grid(row=0, column=0, padx=10, pady=(5,20))

  sorting_btn = ctk.CTkButton(main_frame3, text="Sorting  Algorithms",
                              height=70,
                              width=100,
                              hover_color="dark orange",
                              fg_color="orange",
                              border_color="white",
                              font=ctk.CTkFont("arial", size=20, weight="bold"),
                              corner_radius=15,
                              border_width=2,
                              command=to_Sorting_dashboard
                              )
  sorting_btn.grid(row=1, column=0, padx=50, pady=(5, 20))

  graph_btn = ctk.CTkButton(main_frame3, text="Graph Traversal Algorithms",
                            height=70,
                            width=100,
                            hover_color="dark green",
                            fg_color="green",
                            border_color="white",
                            font=ctk.CTkFont("arial", size=20, weight="bold"),
                            corner_radius=15,
                            border_width=2,
                            command=to_graph_dashboard
                            )
  graph_btn.grid(row=1, column=1, padx=50, pady=(5, 20))



  LOGO_label = ctk.CTkLabel(main_frame2, text="VisuaLearn", font=ctk.CTkFont("Segoe UI", 100, "bold"), text_color="#3b5194", fg_color="#c2d6ed", corner_radius=20)  # display image with a CTkLabel
  LOGO_label.grid(row=0, column=0, padx=5, pady=(30, 70))

  # back_btn = ctk.CTkButton(main_frame1, text="Back",
  #                           height=20,
  #                           width=20,
  #                           border_color="white",
  #                           font=ctk.CTkFont("arial", size=10, weight="bold"),
  #                           corner_radius=35
  #                           )
  # back_btn.grid(row=0, column=1, padx=10, pady=(1, 1))
  # home_btn = ctk.CTkButton(main_frame1, text="Home",
  #                           height=20,
  #                           width=20,
  #                           border_color="white",
  #                           font=ctk.CTkFont("arial", size=10, weight="bold"),
  #                           corner_radius=35
  #                           )
  # home_btn.grid(row=0, column=0, padx=10, pady=(1, 1))

  root.mainloop()
