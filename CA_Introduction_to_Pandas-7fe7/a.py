"""
1) Add the file name and activity details.
   a) Mention the file name as `my-photo-album.py`.
   b) Mention the activity name as "My Photo Album".
   c) Mention the lesson topic and grade range.

2) Import the required libraries.
   a) Import Tkinter widgets using `from tkinter import *`.
   b) Import `messagebox` to show pop-up messages.
   c) Import `Image` and `ImageTk` from PIL to display images.

3) Create the main window.
   a) Create the window using `Tk()`.
   b) Set the window title.
   c) Set the window size using `geometry()`.

4) Add the title and image.
   a) Create a title label for "My Photo Album".
   b) Place the label using `pack()`.
   c) Open the image file using `Image.open()`.
   d) Resize the image.
   e) Convert it into a Tkinter-compatible image using `ImageTk.PhotoImage()`.
   f) Display the image using a `Label`.

5) Create the message box function.
   a) Define the `show_message()` function.
   b) Use `messagebox.showinfo()` to show a pop-up message.
   c) Create a button that calls this function when clicked.

6) Create the photo details window.
   a) Define the `show_details()` function.
   b) Create a new window using `Toplevel()`.
   c) Set the new window title and size.
   d) Add labels for the date and location.
   e) Place the labels using `pack()`.

7) Add the details button.
   a) Create a button with the text "See Details".
   b) Connect it to the `show_details()` function.
   c) Place the button using `pack()`.

8) Run the Tkinter app.
   a) Use `window.mainloop()` to keep the main window open.
"""