from tkinter import *


class Window(Frame):
    def __init__(self, master):
        self.master = master
        self.counter = 0 # counts how many letters the user types, back space will decrement counter
        self.key = '' # key user pressed
        self.line = "" # line being read from file to be displayed
        self.text_display = Text()
        self.text_input = Text()
            

    def key_pressed(self, e):
        self.text_input.see("end")
        self.text_display.see("1.0")
        self.key = e.keysym

        valid_words = ["equal", "space", "braceright", "braceleft", "parenright", "parenleft", "asterisk", "colon", "underscore", "semicolon", "numbersign", "comma", "period", "exclam", "quoteright", "quotedbl"]
        valid_words_signs = ["=", " ", "}", "{", ")", "(", "*", ":", "_", ";", "#", ",", ".", "!", "'", '"']
  
        print("Counter:", self.counter)
        print("Key pressed:", self.key)
        print("Key on line:", self.line[self.counter] )

        if self.key == "BackSpace" and self.counter > 0:
            txt = self.text_input.get("1.0", END)
            txt = txt[:len(txt)-2]

            self.text_input.configure(state="normal")
            self.text_input.delete("1.0", END)
            self.text_input.insert("1.0", txt)
            self.text_input.configure(state="disabled")
            self.counter -= 1

        elif self.key in valid_words:
            index = valid_words.index(self.key)
            if valid_words_signs[index] == self.line[self.counter]:
                self.text_input.configure(state="normal")
                self.text_input.insert("end", valid_words_signs[index])
                self.text_input.configure(state="disabled")
                print(self.key)
                self.counter += 1
            else:
                print("Wrong")

        elif len(self.key) == 1:
            if (self.line[self.counter] == self.key):
                print(self.key)
                self.text_input.configure(state='normal')
                self.text_input.insert("end", self.key)
                self.text_input.configure(state='disabled')
                self.counter += 1
            else:
                self.text_input.config(state="disabled")
                print("Wrong")
     
           
    def text_box(self):
        # Read information from file
        f = open("words.txt", "r")
        self.line = f.readline()
        f.close()
        lineSize = len(self.line)

        font = ("Verdana", 25)

        # Text (Display information)
        self.text_display = Text(bg="#bebebe", fg="black", font=font, height="6", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_display.pack(pady=50)
        self.text_display.insert(1.0, self.line)
        self.text_display.focus()
        self.text_display.config(state="disabled")
        self.text_display.mark_set("insert", "%d.%d" % (1, 0))

        # Text (take user input)
        self.text_input = Text(bg="#bebebe", fg="black", font=font, height="2", width="30", borderwidth=2, relief="solid", yscrollcommand="true", wrap="word")
        self.text_input.pack(pady=50)
        self.text_input.focus()
        self.text_input.config(state="disabled")


    def input_listener(self):
        test = self.text_input.get("1.0", END)
        root.bind("<Key>", self.key_pressed)


root = Tk()

root.title("Typing Test")
root.geometry("1000x600")

window = Window(root)

window.text_box()
window.input_listener()

root.mainloop()