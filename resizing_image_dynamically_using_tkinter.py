from tkinter import *
from tkinter import simpledialog, filedialog
import cv2

rootwindow = Tk()
rootwindow.title("Resizing Images Dynamically")
rootwindow.maxsize(600, 600)
rootwindow.minsize(500, 500)

# Global variables
image = None
displayed_image = None

def open_image():
    global image, displayed_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            displayed_image = image.copy()  # Create a copy for displaying
            cv2.imshow("Image Window", displayed_image)
        else:
            print("Error: Unable to open the selected image.")

def resize_image():
    global displayed_image
    print("Image will be resized")
    x = simpledialog.askinteger("Width", "Enter width")
    y = simpledialog.askinteger("Height", "Enter height")
    
    if x and y:
        displayed_image = cv2.resize(displayed_image, (x, y))
        cv2.imshow("Image Window", displayed_image)

btn1 = Button(text="Open Image", command=open_image)
btn1.grid(row=0, column=0)

btn2 = Button(text="Resize Image", command=resize_image)
btn2.grid(row=0, column=4)

rootwindow.mainloop()
