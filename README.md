# <a name="title"></a> Speed Typing

### Introduction
After reaching 130 WPM from constant speed typing training, I figured I would make my own speed typing program with custom input to maximize educational value. <br>


### Usage


#### Setup
1 - Clone the master repository (```git clone https://github.com/Sebastian-git/SpeedTyping.git```) <br>
2 - (Optional) Check if all [libraries](#Launch) are up to date with [pip](https://pip.pypa.io/en/stable/installing/) (```pip install [package_name] --upgrade```) <br>
3 - (Optional) Set up a custom ```words.txt``` file using the ```script.py``` file, instructions below <br>

Now, you are ready to begin improving your typing skills! <br><br>


#### Customization (script.py)

With the addition of ```script.py```, users can appreciate a speed typing game with a custom set of words. The  technical information for the quick script is displayed in detail [below](#Technical Information).  <br>

Follow the given steps to create a custom data set to type to: <br>
1 - Put the desired content into a `.txt` file <br>
2 - On line 4 of `script.py`, set file_name equal to the text file (`file_name = [file.txt]`) <br>
3 - Run script.py, which will parse the content to be readable by the main program <br> <br>

The content will be written to words.txt, and will now be displayed when the program is run! <br><br>


### Previews

(1) The program will display the words to type at the top, color the last word typed in light green, and shows the timer at the bottom <br>

<img width="1000" height="600" alt="portfolio_view" src="https://github.com/Sebastian-git/SpeedTyping/blob/master/imgs/Screenshot_2.png"> <br><br>

(2) A fun example of using the `script.py` file is on the program itself! Here is an example of what it looks like when loaded <br>

<img width="1000" height="600" alt="portfolio_view" src="https://github.com/Sebastian-git/SpeedTyping/blob/master/imgs/Screenshot_1.png"> <br> <br>

### Technical Information 

(1)
The most important piece of code in `script.py` is the for loop which removes double spaces and all white space characters (`\t`, `\n`). Starting on line 10: <br>
``` py
newData = ""
prev = ""
for char in data:
    if char.isspace() and not (prev.isspace()): # Only allows one space at a time
        newData += " "
    elif not (char.isspace()):
        newData += char

    prev = char
```
First, the code loops through each character in a string containing the contents of a file. <br>

Then, it checks if the current character is a white space, and if the previous character is not a white space.
If this condition is met, only one space is appended to the new string. <br>

Otherwise, if the current character isn't a white space (a normal letter/number), then append the character. <br>

Finally, set the previous character equal to the current for the next iteration. <br> <br>


(2)
An interesting portion of `speedtyping.py` is the thread for the timer, which is split into two parts <br>

First, `timer_thread` is created, the thread's target being the `timer_threading()` function.
```py
# Creates new thread and calls function
def timer_display(self):
    timer_thread = threading.Thread(target=self.timer_threading)
    timer_thread.daemon = True
    timer_thread.start() 
```

Second, `timer_threading()` loops through the specified total time (usually 60). After sleeping for one second, the label that keep strack of time is set to the current index plus one (for the first iteration, 0 + 1) and displayed. The function ends with a call to `stats_message()`, which displays the statistics (accuracy and WPM). 
```py
# New thread updates time label every second until one minute
def timer_threading(self):
    for i in range(self.total_time):
        time.sleep(1)
        self.time_label.config(text=str(i+1))
        self.time_label.pack()
    self.stats_message() 
```
<br><br>


### Launch
Python 3.9.0 <br>
Libraries: TKinter, Threading, Time <br>
VS Code 1.48 <br>

### Status: 

In progress

#### [back to the top](#title)
