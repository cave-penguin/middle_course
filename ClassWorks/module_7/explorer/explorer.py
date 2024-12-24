import os
import tkinter
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("Text file", ".txt"), ("All files", "*")),
    )
    print(filename)
    print(text['text'])
    text["text"] = text["text"] + " " + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title("Explorer")
window.geometry("350x148")
window.configure(bg="red")
window.resizable(False, False)
text = tkinter.Label(
    window, text="File", height=5, width=49, background="silver",
    foreground="blue"
)
text.grid(column=1, row=1)
button_select = tkinter.Button(
    window,
    width=20,
    height=3,
    text="Select file",
    background="silver",
    foreground="blue",
    command=file_select,
)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
