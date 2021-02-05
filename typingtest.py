from tkinter import *
import threading
import time


class Window(Frame):

    # Contains member variables
    def __init__(self, master):
        self.master = master
        self.counter = 0 # counts how many letters the user types, back space will decrement counter
        self.mistakes = 0 # counts mistakes
        self.key = '' # key user pressed
        self.line = "" # line being read from file to be displayed
        self.text_display = Text()
        self.text_input = Text()
        self.time_label = Label(text="0")

    # Creates key listener
    def input_listener(self):
        root.bind("<Key>", self.key_pressed)

    # Function called every time key is pressed
    def key_pressed(self, e):
        self.text_input.see("end")
        self.text_display.see("1.0")
        self.key = e.keysym

        valid_words = ["equal", "space", "braceright", "braceleft", "parenright", "parenleft", "asterisk", "colon", "underscore", "semicolon", "numbersign", "comma", "period", "exclam", "quoteright", "quotedbl"]
        valid_words_signs = ["=", " ", "}", "{", ")", "(", "*", ":", "_", ";", "#", ",", ".", "!", '"', "'"]

        if self.key == "BackSpace" and self.counter > 0: # Handles the removal of characters
            txt = self.text_input.get("1.0", END)
            txt = txt[:len(txt)-2]

            self.text_input.configure(state="normal")
            self.text_input.delete("1.0", END)
            self.text_input.insert("1.0", txt)
            self.text_input.configure(state="disabled")
            self.counter -= 1

        elif self.key in valid_words: # Handles special cases (valid_words) because tkinter uses strings instead of the actual char
            index = valid_words.index(self.key)
            if valid_words_signs[index] == self.line[self.counter]:
                self.text_input.configure(state="normal")
                self.text_input.insert("end", valid_words_signs[index])
                self.text_input.configure(state="disabled")
                self.counter += 1
            else:
                self.mistakes += 1

        elif len(self.key) == 1: # Handles normal numbers/letters
            if (self.line[self.counter] == self.key):
                self.text_input.configure(state='normal')
                self.text_input.insert("end", self.key)
                self.text_input.configure(state='disabled')
                self.counter += 1
            else:
                self.mistakes += 1     
    
    # Creates two text boxes
    def text_box(self):
        # Read information from file
        f = open("words.txt", "r")
        self.line = f.readline()
        f.close()
        lineSize = len(self.line)

        font1 = ("Verdana", 15)
        
        font2 = ("Verdana", 30)

        # Text (Display information)
        self.text_display = Text(bg="#bebebe", fg="black", font=font1, height="6", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_display.pack(pady=50, padx=50)
        self.text_display.insert(1.0, self.line)
        self.text_display.focus()
        self.text_display.config(state="disabled")
        self.text_display.mark_set("insert", "%d.%d" % (1, 0))
        self.text_display.pack(fill=BOTH, expand=1)

        # Text (take user input)
        self.text_input = Text(bg="#bebebe", fg="black", font=font2, height="2", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_input.pack(pady=50)
        self.text_input.focus()
        self.text_input.config(state="disabled")

    # Creates new thread and calls function
    def timer_display(self):
        x = threading.Thread(target=self.timer_thread)
        x.daemon = True
        x.start()

    # New thread updates time label every second until one minute
    def timer_thread(self):
        for i in range(60):
            time.sleep(1)
            self.time_label.config(text=str(i+1))
            self.time_label.pack()
                

root = Tk()

root.title("Typing Test")
root.geometry("1000x600")

window = Window(root)

window.text_box()
window.input_listener()
window.timer_display()

root.mainloop()