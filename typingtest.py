from tkinter import *
from tkinter import messagebox
import threading
import time


# Main class for tkinter window
class Window(Frame):

    # Contains member variables
    def __init__(self):
        self.total_counter = 0 # counts how many letters the user types, back space will decrement counter
        self.counter = 0 # Specific counter to key_pressed() for tracking correct/incorrect words
        self.mistakes = 0 # Counts mistakes
        self.key = '' # Key user pressed
        self.line = "" # Line being read from file to be displayed
        self.text_display = Text() # Text() containing words to display to user
        self.text_input = Text() # Text() for user input
        self.time_label = Label(text="0") # Label for timer
        self.total_time = 60 # Integer the timer counts up to 
        self.start_timer = True

    # Creates key listener
    def input_listener(self):
        root.bind("<Key>", self.key_pressed)

    # Colors previous and current text
    def text_colors(self, char):
        self.text_input.configure(state="normal")
        self.text_input.tag_add('previous_letters', 'end-1c linestart', 'end-1c')
        self.text_input.tag_configure("previous_letters", foreground="#0a5d00")
        self.text_input.insert("end", char)
        self.text_input.configure(state="disabled")
        self.counter += 1

    # Function called every time key is pressed
    def key_pressed(self, e):
        if self.start_timer:
            window.timer_display()
            self.start_timer = False

        self.text_input.see("end")
        self.text_display.see("1.0")
        self.key = e.keysym

        valid_words = ["equal", "space", "braceright", "braceleft", "parenright", "parenleft", "asterisk", "colon", "underscore", "semicolon", "numbersign", "comma", "period", "exclam", "quoteright", "quotedbl", "slash", "backslash", "less", "greater", "question", "quoteleft", "asciitilde", "bracketleft", "brackerright", "bar", "plus", "minus"]
        valid_words_signs = ["=", " ", "}", "{", ")", "(", "*", ":", "_", ";", "#", ",", ".", "!", "'", '"', "/", "\\", "<", ">", "?", "`", "~", "[", "]", "|", "+", "-"]

        # Handles special cases (valid_words) because tkinter uses strings instead of the actual char
        if self.key in valid_words: 
            index = valid_words.index(self.key)
            if valid_words_signs[index] == self.line[self.counter]:
                self.text_colors(valid_words_signs[index])
            else:
                self.mistakes += 1

        # Handles normal numbers/letters
        elif len(self.key) == 1: 
            if (self.line[self.counter] == self.key):
                self.text_colors(self.key)
            else:
                self.mistakes += 1     

        self.total_counter += 1
    
    # Creates two text boxes
    def text_box(self):
        # Read information from file
        f = open("words.txt", "r")
        self.line = f.readline()
        f.close()
        lineSize = len(self.line)

        # Set fonts for both displays
        font1 = ("Consolas", 15)
        font2 = ("Consolas", 30)

        # Text (Display information)
        self.text_display = Text(bg="#bebebe", fg="black", font=font1, height="6", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_display.pack(pady=50, padx=50)
        self.text_display.insert(1.0, self.line)
        self.text_display.focus()
        self.text_display.config(bg="#2a2a2a", state="disabled", fg="#0eff00")
        self.text_display.mark_set("insert", "%d.%d" % (1, 0))
        self.text_display.pack(fill=BOTH, expand=1)

        # Text (take user input)
        self.text_input = Text(bg="#bebebe", fg="black", font=font2, height="2", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_input.pack(pady=50)
        self.text_input.focus()
        self.text_input.config(state="disabled", bg="#2a2a2a", fg="#0eff00")

        # Label background
        self.time_label.config(bg="#161616", fg="#0eff00", font=font1)

    # Creates new thread and calls function
    def timer_display(self):
        timer_thread = threading.Thread(target=self.timer_threading)
        timer_thread.daemon = True
        timer_thread.start()

    # New thread updates time label every second until one minute
    def timer_threading(self):
        for i in range(self.total_time):
            time.sleep(1)
            self.time_label.config(text=str(i+1))
            self.time_label.pack()
        self.stats_message()

    # Displays round's statistics
    def stats_message(self):
        if self.total_counter - self.mistakes < 0:
            accuracy = "Your accuracy was 0%"
        else:
            accuracy = "Your accuracy was " + str(int(((self.total_counter - self.mistakes) / self.total_counter) * 100)) + "%"

        wpm = "Your WPM was " + str(int(self.total_counter/5))
        stats = wpm + "\n" + accuracy

        messagebox.showinfo("", stats)


# Tkinter settings
root = Tk()

root.title("Typing Test")
root.geometry("1000x600")
root.configure(bg="#161616")

# Create class and call methods
window = Window()

window.text_box()
window.input_listener()

# Start GUI
root.mainloop()