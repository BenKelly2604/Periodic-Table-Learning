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
    help_window.geometry("350x405")

    # Load the "helpguy.png" image
    help_image = Image.open("helpguy.png")
    help_image = help_image.resize((200, 200))  # Resize the image as needed
    help_photo = ImageTk.PhotoImage(help_image)

    # Create a label to display the image
    help_image_label = tk.Label(help_window, image=help_photo)
    help_image_label.pack()

    # Ensure the image stays visible by keeping a reference to it
    help_image_label.image = help_photo

    # Add text
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
    help_label.pack(padx=20, pady=10)

    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)


# Create main window
root = tk.Tk()
root.title("Periodic Table Learning")

# Set the size of the main window
root.geometry("800x495")  # Set the width and height as desired

# Load and resize the background image
background_image = Image.open("background.png")
background_image = background_image.resize((800, 600))  # Change the dimensions as desired
background_photo = ImageTk.PhotoImage(background_image)

# Create the background label and place it behind other widgets
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.lower()


# Add a text label at the top
title_label = tk.Label(root, text="Periodic Table Learning", font=("Helvetica", 22, "bold"), bg="#FFCCCC", fg="black")
title_label.pack(pady=20)  # Add some padding to the top

# Create "Learn" button with larger text size
learn_button = tk.Button(root, text="Learn", width=5, height=1, command=open_learn, bg="#add8e6", fg="black")
learn_button['font'] = ('Arial', 28, 'bold')  # Change the text size here
learn_button.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

# Create "Quiz" button with larger text size and bold font
quiz_button = tk.Button(root, text="Quiz", width=5, height=1, command=open_quiz, bg="#90ee90", fg="black")
quiz_button['font'] = ('Arial', 28, 'bold')  # Change the text size and make it bold
quiz_button.place(relx=0.1, rely=0.7, anchor=tk.CENTER)


# Create "Help" button
help_button = tk.Button(root, text="Help/info", width=10, height=2, command=open_help)
help_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

root.mainloop()
