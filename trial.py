# Import Module
import tkinter as tk
from tkinter import filedialog, messagebox, Frame
import os
import pyttsx3
import PyPDF2
from multipart import file_path
from pygame import mixer

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Welcome to PDF to AudioBook converter")
# Set geometry(widthxheight)
root.geometry('500x500')

root.config(bg="skyblue")

def clear_frame(reset_frame: bool=True):
    widgets_to_clear = frame.winfo_children()
    for widget in widgets_to_clear:
        widget.destroy()
    if reset_frame:
        label = tk.Label(frame, text="Welcome to PDF-to-Audiobook Converter", bg="lightblue")
        label.pack(pady=50)
    return None

def about_app():
    clear_frame(False)
    text_widget = tk.Text(frame, bg="lightblue", borderwidth=0)
    text_widget.pack(fill="both", expand=True, pady=50, padx=20)
    text_widget.tag_configure("center", justify="center")
    text_widget.insert(tk.INSERT, "I am PDF to AudioBook Converter.\n", "left")
    text_widget.insert(tk.INSERT, "Version: 1.0.0.\n")
    text_widget.insert(tk.INSERT, "Creation Date: 07-Jul-2025 ", "normal")

def show_upload_form():
    upload_button = tk.Button(frame, text="Upload PDF", command=upload_file)
    upload_button.pack(pady=50, padx=20)

def upload_file():
    #clear_frame(False)
    global uploaded_file_path
    uploaded_file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        print(f"Selected file: {uploaded_file_path}")
        filename_with_extension = os.path.basename(uploaded_file_path)
        # Split the filename into base name and extension
        filename_without_extension, extension = os.path.splitext(filename_with_extension)
        if extension == ".pdf":
            uploaded_file = tk.Label(frame, text=f"You Selected: {filename_with_extension}", bg="lightblue")
            uploaded_file.pack(pady=2)

            read_button_1 = tk.Button(frame, text="Read PDF (Male Voice)", command=read_male_voice)
            read_button_1.pack(pady=5)

            read_button_2 = tk.Button(frame, text="Read PDF (Female Voice)", command=read_female_voice)
            read_button_2.pack(pady=5)

            download_button = tk.Button(frame, text="Download Audio File", command=download_audio_file)
            download_button.pack(pady=5)

            # open_button = tk.Button(root, text="Open PDF", command=read_file)
            # open_button.pack(pady=10)
            #
            # play_button = tk.Button(root, text="Play", command=read_file)
            # play_button.pack(pady=5)
            #
            # pause_button = tk.Button(root, text="Pause", command=read_file)
            # pause_button.pack(pady=5)
            #
            # speed_up_button = tk.Button(root, text="Speed Up", command=read_file)
            # speed_up_button.pack(pady=5)
            #
            # speed_down_button = tk.Button(root, text="Speed Down", command=read_file)
            # speed_down_button.pack(pady=5)
            #
            # stop_button = tk.Button(root, text="Stop", command=read_file)
            # stop_button.pack(pady=5)
        else:
            # this case will never run
            messagebox.showerror("Error", "Please upload PDF file only")
    else:
        messagebox.showwarning("Warning", "You decided not to upload file")

def read_male_voice():
    read_file(1)

def read_female_voice():
    read_file(2)

def read_file(voice_type):
    book = open(uploaded_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(book)
    pages = len(pdf_reader.pages)
    extracted_text = ""
    speaker = pyttsx3.init()
    # page =  pdf_reader.pages[4] # page 4 reading
    # text = page.extract_text()
    # speaker.say(text)
    # speaker.runAndWait()
    voices = speaker.getProperty('voices')
    for index, voice in enumerate(voices, start=1):
        if voice_type == index:
            speaker.setProperty('voice', voice.id)
    speaker.setProperty('rate', 2000)
    for num in range(1,pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()
        extracted_text += text
        # speaker.say(text)
        speaker.runAndWait()
    else:
        output_file = "audiobook.mp3"
        speaker.save_to_file(extracted_text, output_file)
        mixer.init()
        mixer.music.load("audiobook.mp3")
        mixer.music.play()

def download_audio_file():
    pass

def exit_app():
    root.destroy()

menuBar = tk.Menu(root)
root.config(menu=menuBar)
file_menu = tk.Menu(menuBar, tearoff=0)  # tearoff=0 prevents the menu from being "torn off"
menuBar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Upload PDF", command=show_upload_form)
file_menu.add_command(label="Clear Frame", command=clear_frame)
file_menu.add_separator()  # Add a visual separator
file_menu.add_command(label="Exit", command=exit_app)

help_menu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_app)

# Create Frame widget
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

clear_frame(True)

# Execute Tkinter
root.mainloop()