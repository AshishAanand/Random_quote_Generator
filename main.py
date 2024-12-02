from tkinter import *
from tkinter import filedialog
import random
import json

file_path = 'quotes.json'

get_quote = ""

# Load data from JSON file
def load_data():
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        print(f"Error occurred: {e}")
        return []

# Change the displayed quote
def change_quote_func():
    global get_quote
    data = load_data()
    if data:
        random_quote = random.choice(data)  # Select a random quote
        quote_label.config(text=f'{random_quote["quote"]} - {random_quote["author"]}')
        get_quote = f'{random_quote["quote"]} - {random_quote["author"]}'
    else:
        quote_label.config(text="No quotes available. Please check the JSON file.")

def save_quote(quote):
        # Open file dialog for user to choose save location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save Favorite Quote"
    )
    if file_path:  # If user selects a path
        try:
            with open(file_path, "w") as file:
                file.write(quote)
            print("Quote saved successfully!")
        except Exception as e:
            print(f"Error saving file: {e}")



# Initialize Tkinter
root = Tk()
root.title("Random Quote Generator")

# Defining window size
root.geometry("600x300")
root.minsize(500, 200)

# Showing Quote
quote_label = Label(root, text="Click 'Change Quote' to see a new quote!", padx=10, pady=10, font=("Arial", 12), wraplength=550, justify="center")
quote_label.pack(pady=50)

options_frame = Frame(root)
options_frame.pack(pady=10)

# Button for changing Quote
change_quote_btn = Button(options_frame, text="Change Quote", padx=10, pady=8, font=("Arial", 8), command=change_quote_func)
change_quote_btn.grid(row=0, column=0, padx=20, pady=10)

# Button for saving Quote (No functionality implemented yet)
save_quote_btn = Button(options_frame, text="Save Quote", padx=10, pady=8, font=("Arial", 8), command=lambda: save_quote(get_quote))
save_quote_btn.grid(row=0, column=1, padx=20, pady=10)

# Start the Tkinter main loop
root.mainloop()
