
# import tkinter as tk
# from tkinter import messagebox


# # Function to handle user input and selection
# def handle_selection(input_text, list_names):
#     try:
#         # Convert input to an integer
#         choice = int(input_text)

#         # Check if the choice is valid
#         if 1 <= choice <= len(list_names):
#             # Clear the current frame
#             for widget in main_frame.winfo_children():
#                 widget.destroy()

#             # Display the selected option
#             response_label = tk.Label(main_frame, text=f"You selected: {list_names[choice - 1]}", 
#                                        fg="white", bg="black", font=("Arial", 14))
#             response_label.pack(pady=20)

#             # Button to go back to the main menu
#             back_button = tk.Button(main_frame, text="Back to Menu", command=display_menu, font=("Arial", 12))
#             back_button.pack(pady=10)
#         else:
#             messagebox.showerror("Invalid Choice", "Please enter a valid number from the menu.")
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Please enter a number.")


# # Function to display the menu
# def display_menu():
#     # Clear the current frame
#     for widget in main_frame.winfo_children():
#         widget.destroy()

#     # Menu options
#     list_names = ['Custom Control', 'Picking', 'Payment of Public Service and Administration', 
#                   'Suppliers', 'Contact', 'Solutionary']
    
#     # Header
#     tk.Label(main_frame, text="Routes of Access", fg="white", bg="black", font=("Arial", 16)).pack(pady=10)

#     # Display the options as a list
#     for i, option in enumerate(list_names, 1):
#         tk.Label(main_frame, text=f"{i}. {option}", fg="white", bg="black", font=("Arial", 12)).pack()

#     # Input field for user choice
#     tk.Label(main_frame, text="Enter your choice:", fg="white", bg="black", font=("Arial", 12)).pack(pady=10)
#     input_field = tk.Entry(main_frame, font=("Arial", 12))
#     input_field.pack(pady=5)
#     input_field.focus()

#     # Submit button to process the input
#     submit_button = tk.Button(
#         main_frame,
#         text="Submit",
#         command=lambda: handle_selection(input_field.get(), list_names),
#         font=("Arial", 12),
#         bg="gray",
#         fg="black"
#     )
#     submit_button.pack(pady=10)

#     # Exit button
#     exit_button = tk.Button(main_frame, text="Exit", command=app.quit, font=("Arial", 12), bg="red", fg="white")
#     exit_button.pack(pady=10)


# # Initialize the app window
# app = tk.Tk()
# app.title("Black Square App")
# app.geometry("400x300")
# app.configure(bg="black")

# # Create the main frame for content
# main_frame = tk.Frame(app, bg="black")
# main_frame.pack(expand=True, fill="both")

# # Display the initial menu
# display_menu()

# # Run the app
# app.mainloop()


import tkinter as tk


# Function to handle user input
def handle_input(event):
    input_text = input_field.get().strip()  # Get the input text
    input_field.delete(0, tk.END)  # Clear the input field

    if input_text.lower() in ['exit', 'e']:
        app.quit()  # Exit the app
    else:
        try:
            choice = int(input_text)  # Convert input to integer
            if 1 <= choice <= len(list_names):  # Validate choice
                display_response(f"You selected: {list_names[choice - 1]}")
            else:
                display_response("Invalid option. Please try again.")
        except ValueError:
            display_response("Invalid input. Please enter a number or type 'exit'.")


# Function to display the main menu
def display_menu():
    output_text.set("Routes of Access:\n" + "\n".join([f"{i + 1}. {name}" for i, name in enumerate(list_names)]))
    input_field.focus()  # Set focus to the input field


# Function to display a response or message
def display_response(message):
    output_text.set(message + "\n\nType a number to choose an option or type 'exit' to quit.")


# List of options
list_names = ['Custom Control', 'Picking', 'Payment_of_Public_Service_and_Administration','Suppliers', 'Contact', 'Solutionary']

# Initialize the app window
app = tk.Tk()
app.title("Black Box App")
app.geometry("600x400")
app.configure(bg="black")

# Create a text variable for displaying output
output_text = tk.StringVar()
output_text.set("")

# Create a label to display the text output
output_label = tk.Label(app, textvariable=output_text, fg="white", bg="black", font=("Courier", 12), justify="left")
output_label.pack(pady=20, padx=20, anchor="w")

# Create an entry field for user input
input_field = tk.Entry(app, font=("Courier", 14), fg="white", bg="black", insertbackground="white", width=40)
input_field.pack(pady=10)
input_field.bind("<Return>", handle_input)  # Bind Enter key to handle_input function

# Display the main menu initially
display_menu()

# Run the app
app.mainloop()
