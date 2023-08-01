import sys
import tkinter as tk
import random
import time
import plot_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global lbl_words
global frm_words
global counter
global start_time
global typ
global correct
global times
global color
global df
global window


def end():
    """End programm"""
    sys.exit(0)

def start_page(data):
    """Display the startpage of the experiment"""
    global window
    global df
    
    df=data
    window = tk.Tk()
    window.geometry("700x350")
    window.title("Welcome to the Sroop Task")

    frm_label = tk.Frame()
    frm_btn = tk.Frame()

    label_a = tk.Label(master=frm_label, text="Welcome to the Stroop Test!\nIn this test, you will see words " 
                                            "displayed in different ink colors.\n Your task is to identify the ink color "
                                            "of each word as accurately and quickly as possible.\n\nPress 'r' for red, "
                                            "'b' for blue, 'y' for yellow, and 'g' for green.")
    label_a.pack(expand=True)

    btn_start = tk.Button( master=frm_btn,
        text="Start",
        command=experiment,
    )
    btn_start.pack()

    frm_label.pack(expand=True)
    frm_btn.pack(expand=True)

    return window.mainloop()

def keypress(event):
    """Continue stroop task until the end of the experiment.

    Keyword arguments:
    event -- key pressed by user
    """    
    
    global lbl_words
    global frm_words
    global counter
    global start_time
    global typ
    global correct
    global times
    global color
    global df

    limit= 30 #number of trials per experiment

    if event.char == "r" or event.char =="g" or event.char =="b" or event.char =="y":
        end_time = time.time()
        times= end_time-start_time
        correct = (event.char == color[0])
        
        df.loc[counter] = [typ, correct, times]

        counter += 1
     
        if counter ==limit:
            plot_data.combine_results(df)
            end_screen()

        words=["red", "green", "blue", "yellow"]

        word= random.choice(words)
        color= random.choice(words)
        if word == color:
            typ= "con"
        else:
            typ = "incon"

        lbl_words.config(text=word, fg=color)
        start_time = time.time()
        

    else:
        print("Try another key, this one is not a color")
   

def experiment():
    """Start the stroop task experiment"""
    global window
    global lbl_words
    global frm_words
    global counter
    global start_time
    global typ
    global color

    window.destroy()
    counter = 0
    
    window = tk.Tk()
    window.geometry("700x350")
    window.title("Sroop Task")
    window.configure(bg='black')
    frm_words = tk.Frame()

    words=["red", "green", "blue", "yellow"]

    word= random.choice(words)
    color= random.choice(words)

    if word == color:
        typ= "con"
    else:
        typ = "incon"

    lbl_words= tk.Label(master=frm_words, text=word, fg=color, bg='black', font=("Arial", 25))
    

    window.bind("<Key>", keypress)
    lbl_words.pack(expand=True)
    frm_words.pack(expand=True)
    start_time= time.time()
    return window.mainloop()

def show_results():
    """Display the results aof the experiment"""
    global window
    global df

    window.destroy()
    
    window = tk.Tk()
    window.title("Results")

    figure1, ax1 = plot_data.plot_time(df)
    canvas1 = FigureCanvasTkAgg(figure1, window)
    canvas1.get_tk_widget().grid(row=1, column=0, sticky="ew")
  
    figure2, ax2 = plot_data.plot_true(df)
    canvas2 = FigureCanvasTkAgg(figure2, window)
    canvas2.get_tk_widget().grid(row=1, column=1, sticky="ew")

    figure3, ax3 = plot_data.plot_true_you(df)
    canvas3 = FigureCanvasTkAgg(figure3, window)
    canvas3.get_tk_widget().grid(row=0, column=1, sticky="ew")

    figure4, ax4= plot_data.plot_your_time(df)
    canvas4 = FigureCanvasTkAgg(figure4, window)
    canvas4.get_tk_widget().grid(row=0, column=0, sticky="ew")

    window.protocol('WM_DELETE_WINDOW', end)

    return window.mainloop()

def end_screen():
    """Display the end screen of the experiment"""
    global window

    window.destroy()
    
    window = tk.Tk()
    window.geometry("700x350")
    window.title("Sroop Task")

    frm_label = tk.Frame()
    frm_btn = tk.Frame()

    label_a = tk.Label(master=frm_label, text="Great, you are done. \n What do you want to do next?")
    label_a.pack(expand=True)

    btn_again = tk.Button( master=frm_btn,
        text="Try again",
        command=experiment,
    )
    btn_results = tk.Button( master=frm_btn,
        text="Show results",
        command=show_results,
    )
    btn_again.pack()
    btn_results.pack()

    frm_label.pack(expand=True)
    frm_btn.pack(expand=True)

    return window.mainloop()
