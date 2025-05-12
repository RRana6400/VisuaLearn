import customtkinter as ctk
import tkinter as tk
import dashboard as db
from Sorting import *
from Sorting import bubbleSort
from PIL import Image

# moving to dashboard
def to_dashboard():
  db.main_dashboard(root)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("VisuaLearn")
root.geometry("800x500")
root.resizable(width=False, height=False)
# Configure grid layout 
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Creation of main frame
main_frame = ctk.CTkFrame(root, corner_radius=15, )
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Title label
title_label = ctk.CTkLabel(main_frame, text="Welcome to VisuaLearn !", font=ctk.CTkFont(size=40, weight="bold"))
title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

# Subtitle label
subtitle_label = ctk.CTkLabel(main_frame, text="Learn concepts through Visualization", font=ctk.CTkFont(size=16))
subtitle_label.grid(row=1, column=0, padx=20, pady=(0, 20))

# Button
button = ctk.CTkButton(main_frame, text="Get Started",fg_color="transparent",border_color="white",border_width=2, command=to_dashboard)
button.grid(row=2, column=0, padx=20, pady=(10, 20))

root.mainloop()
