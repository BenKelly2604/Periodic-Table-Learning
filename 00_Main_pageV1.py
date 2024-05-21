import tkinter as tk
from PIL import Image, ImageTk


def open_learn():
    # Functionality for the "Learn" button
    print("Opening Learn page")


def open_quiz():
    # Functionality for the "Quiz" button
    print("Opening Quiz page")


def open_help():
    # Functionality for the "Help" button
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_window.geometry("400x300")

    help_text = """
    Welcome to Periodic Table Learning!
    
    This website helps you learn about the elements
    of the periodic table in a fun and interactive way.
    
    To get started, you can click on the "Learn" button
    to explore information about each element.
    
    If you want to test your knowledge, click on the "Quiz"
    button to take a quiz about the periodic table.
    
    Enjoy learning!
    """

    help_label = tk.Label(help_window, text=help_text, justify=tk.LEFT)
    help_label.pack(padx=20, pady=20)

    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)


# Create main window
root = tk.Tk()
root.title("Periodic Table Learning")

# Set the size of the main window
root.geometry("800x600")  # Set the width and height as desired

# Add a text label at the top
title_label = tk.Label(root, text="Periodic Table Learning", font=("Helvetica", 30, "bold"))
title_label.pack(pady=20)  # Add some padding to the top

# Load and display image of periodic table
image = Image.open("Periodic_table.jpg")
# Resize the image to desired dimensions
image = image.resize((675, 325))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

# Create "Learn" button with larger text size
learn_button = tk.Button(root, text="Learn", width=5, height=1, command=open_learn)
learn_button['font'] = ('Arial', 28, 'bold')  # Change the text size here
learn_button.place(relx=0.4, rely=0.8, anchor=tk.CENTER)

# Create "Quiz" button with larger text size and bold font
quiz_button = tk.Button(root, text="Quiz", width=5, height=1, command=open_quiz)
quiz_button['font'] = ('Arial', 28, 'bold')  # Change the text size and make it bold
quiz_button.place(relx=0.6, rely=0.8, anchor=tk.CENTER)



# Create "Help" button
help_button = tk.Button(root, text="Help", width=10, height=2, command=open_help)
help_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

root.mainloop()
