import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk

class ColorAdjuster:
    def __init__(self, root):
        self.root = root
        self.root.title("Color to Grayscale Adjuster")

        # Create a canvas to display the color block
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        # Set the initial color
        self.color = (255, 0, 0)  # Red as an example
        self.update_canvas()

        # Add sliders for R, G, B values
        self.red_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Red", command=self.update_color, length=300)
        self.red_slider.set(self.color[0])
        self.red_slider.pack()

        self.green_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Green", command=self.update_color, length=300)
        self.green_slider.set(self.color[1])
        self.green_slider.pack()

        self.blue_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blue", command=self.update_color, length=300)
        self.blue_slider.set(self.color[2])
        self.blue_slider.pack()

        # Add a button to submit the selected color
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=15)

    def update_canvas(self):
        # Update the color block on the canvas
        color_hex = "#{:02x}{:02x}{:02x}".format(*self.color)
        self.canvas.create_rectangle(0, 0, 300, 300, fill=color_hex, outline=color_hex)

    def update_color(self, event=None):
        # Update the color based on the slider values
        r = self.red_slider.get()
        g = self.green_slider.get()
        b = self.blue_slider.get()
        self.color = (r, g, b)
        self.update_canvas()

    def submit(self):
        # Convert the selected color to grayscale and display it
        grayscale_value = int(0.3*self.color[0] + 0.59*self.color[1] + 0.11*self.color[2])
        grayscale_color = (grayscale_value, grayscale_value, grayscale_value)
        self.color = grayscale_color
        self.update_canvas()
        print(f"Selected grayscale value: {grayscale_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorAdjuster(root)
    root.mainloop()
