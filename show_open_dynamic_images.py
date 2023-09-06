from tkinter import *
from tkinter import filedialog, messagebox
import cv2

root = Tk()
root.maxsize(600, 600)
root.minsize(600, 600)
root.title("Image Viewer")

def openmenu():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        print("Opening file:", file_path)
        image = cv2.imread(file_path)
        if image is not None:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Failed to open image.")

def exit_app():
    decide = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
    if decide:
        root.destroy()

menubar = Menu(root)
root.config(menu=menubar)

mymenu = Menu(menubar)

mymenu.add_command(label='Open', command=openmenu)
mymenu.add_separator()
mymenu.add_command(label='Exit', command=exit_app)

menubar.add_cascade(label='File', menu=mymenu)

root.mainloop()
