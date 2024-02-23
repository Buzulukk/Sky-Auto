import os

import tkinter as tk
from tkinter import ttk, filedialog

import threading

import time
import winsound

import main

play_thread = None
stop_thread = threading.Event()

def play_selected_music(selected_file, stop_signal):
    main.file_processing("music\\" + selected_file)

def play_button_action():
    global play_thread
    stop_button_action()
    
    selected_file = listbox.get(tk.ANCHOR) # Get the selected file
    
    if selected_file:
        for i in range(3):  # sound signals for start
            winsound.Beep(500, 200)
            time.sleep(1)

        stop_thread.clear() # Clear the stop signal
        play_thread = threading.Thread(target=play_selected_music, args=(selected_file, stop_thread))
        play_thread.start()
        
def stop_button_action():
    global play_thread
    if play_thread is not None:
        stop_thread.set() # Signal the thread to stop
        play_thread.join() # Wait for the thread to finish
        play_thread = None
    
        
def start():
    root = tk.Tk()
    root.title("Sky Auto")
    root.geometry("400x300")
    try:
        root.iconbitmap('source code\\piano-icon.ico')
    except Exception as e:
            pass

    global listbox
    listbox = tk.Listbox(root, width=50, height=10)
    listbox.pack(pady=15)

    music_folder = 'music'
    music_files = [f for f in os.listdir(music_folder) if os.path.isfile(os.path.join(music_folder, f))]
    for file in music_files:
        listbox.insert(tk.END, file)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    play_button = tk.Button(button_frame, text="Play", command=play_button_action, height=2, width=10)
    play_button.pack(side=tk.RIGHT, padx=10)

    stop_button = tk.Button(button_frame, text="Stop", command=stop_button_action, height=2, width=10)
    stop_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()
