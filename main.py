import tkinter as tk

# Function to update the color of the block based on the current value
def update_color(value):
    red_value = int(value)
    gray_value = 255 - red_value
    color = f'#{red_value:02x}{gray_value:02x}{gray_value:02x}'  # Convert to hex
    canvas.itemconfig(block, fill=color)

# Function to handle left and right arrow key events
def key_press(event):
    global current_value
    if event.keysym == 'Right':
        current_value = min(current_value + 3, 255)  # Increase red (max 255)
        
    elif event.keysym == 'Left':
        current_value = max(current_value - 3, 0)    # Decrease red (min 0)
    update_color(current_value)

# Initialize the main window
root = tk.Tk()
root.title("Perception-based Color Adjustment")

# Create a canvas for the color block
canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(row=0, column=0, columnspan=3)
#canvas.pack()
canvas.create_text(300, 20, text="Please adjust grayscale", font=("Arial", 16), fill="black", anchor = "n")

# Draw a rectangle (the block) in the canvas
block = canvas.create_rectangle(100, 60, 500, 350, fill="#ff0000")

# Set an initial value for the current color (start fully red)
current_value = 255

# Bind left and right arrow keys to adjust the color
root.bind('<Left>', key_press)
root.bind('<Right>', key_press)

# Less red and more red buttons
less_red_button = tk.Button(root, text="Less red", command=key_press)
less_red_button.grid(row=3, column=1)

more_red_button = tk.Button(root, text="More red", command=key_press)
more_red_button.grid(row=3, column=3)

done_button = tk.Button(root, text="Done") #, command=show_color)
done_button.grid(row=3, column=2)

# Start the Tkinter event loop
root.mainloop()
