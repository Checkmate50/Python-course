## Installation

The first (and hardest) step of getting started with Python is getting it installed.  I'll explain the steps for Windows and note that Mac is similar (if slightly different).  If you already have Python installed, you can just ignore this first section and move onto section 2: our first Python program!

First, download the python installer from [this website](https://www.python.org/downloads/), which should auto-detect which operating system (Windows or Mac) you have.  Next, run the resulting downloaded executable.  Make sure when installing to add Python to your PATH variable (this will make your life easier later).  If you forgot to add Python to your path, lookup how to add Python to the environment path or let me know; I can walk you through the steps.

Next, to make sure python got installed correctly, open your command prompt (or terminal if you're on Mac), and type the word `python`.  You should get a message saying python 3.9.1 (or whatever version you installed) followed by a line with the symbols `>>>`.  To exit, type `exit()` or close the terminal window.  If you don't get this, don't panic!  Make sure you already installed python and added it to your path.  If you get some weird error or if this didn't work, let me know and I can help you out.

## First Python Program

Now it's time to write our first Python program!  Here we get the chance to tell the computer what to do for once: specifically, we're going to have the computer print out the words "Hello World".

To write this program, you have a couple of options:

* Make a file with IDLE (recommended)
* Make a blank text file (advanced)

This tutorial will assume that you're using IDLE, though we will also look at how to run python on a blank text file in a bit.  

### IDLE

To open IDLE, type the word "IDLE" into your search bar: a window that looks something like [this](https://www.tutorialsteacher.com/Content/images/python/idle.png) should pop up (let me know if that image doesn't display, it's just a random website that worked for me).  

Once you get IDLE open, click `File` then `new file` (or press `ctrl-n`).  Save this file with `ctrl-s` to a nice place on your computer (I recommend making a course folder for this course to help with organization!), calling it whatever you want, though I recommend "hello".

In this new file, type `print("Hello World!")`, then press `F5` (or navigate to `run` and `run module (F5)`.  This should cause the words `Hello World!` to pop up in the IDLE terminal!  If this fails for some reason, make sure you don't have any spaces or tabs (called "whitespace") before or after your line of text.  Again, let me know if you get stuck and/or have issues

### Running From a File

You can also just run Python on files directly!  To do this, open your command prompt or terminal and navigate to the folder containing the file you want (with `dir` on Windows and `ls` on other systems).  In this folder, type `python hello.py` (or whatever you called your file) to print `Hello World!`  I won't refer to this method again, but it is actually how I do things and is very powerful once you learn the basics.

### Jupyter Notebook

As another option to make and run Python, you can check out [Jupyter Notebook](https://jupyter.org/try) a free online Python solution.  This setup is a bit more complicated than what we need for this course, so I won't refer to it again, but it might be worth looking into if you like Python and want to share programs with friends!