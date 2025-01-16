from utils import sort_cont, new_item, del_item, dict_procces
import tkinter as tk 

import tkinter as tk
from utils import sort_cont, new_item, del_item

def handle_input(event):
    list_names = sort_cont()
    procces = dict_procces()
    






    input_text = input_field.get().strip()
    input_field.delete(0, tk.END)

    if input_text.lower() in ['exit', 'e']:
        app.quit()
    else:
        try:
            choice = int(input_text)
            if 1 <= choice <= len(list_names):
                dict_1 = {i+1:list_names[i] for i in range(len(list_names))}
                choice = dict_1[choice]
                print(procces[choice])

                for option in list_names:
                    if choice == option:
                        display_message(procces[choice])



                    #display_response(f"You selected: {list_names[choice - 1]}")

                    #display_response("If you want to add another option, write 1.\n"
                    #                 "If you want to delete an option, write 0.\n"
                    #                 "If you want to go to the menu, write m.")                    
                
                    #input_field.bind('<Return>', handle_secondary_input)  # Bind next input to a new handler

            else:
                display_response("Invalid choice. Please select a valid option number.")

        except ValueError:
            display_response("Invalid input. Please enter a number or type 'exit' to quit.")

            

def handle_secondary_input(event):
    input_text_2 = input_field.get().strip()
    input_field.delete(0, tk.END)

    if input_text_2.lower() in ['menu', 'm']:
        display_menu()
    else:
        try:
            choice_2 = int(input_text_2)

            if choice_2 == 1:
                display_message("Please enter the new option name:")
                input_field.bind('<Return>', handle_new_item)

            elif choice_2 == 0:
                display_message("Please enter the name of the option to delete:")
                input_field.bind('<Return>', handle_delete_item)

            else:
                display_response("Invalid input. Please enter 1, 0, or 'menu'.")

        except ValueError:
            display_response("Invalid input. Please enter a valid option or type 'menu'.")

def handle_new_item(event):
    input_text_3 = input_field.get().strip()
    input_field.delete(0, tk.END)
    new_1 = new_item(input_text_3)
    display_message(f"You have created the option '{input_text_3}'.")
    display_message(f"Current options: \n{new_1}")
    display_menu()

def handle_delete_item(event):
    input_text_3 = input_field.get().strip()
    input_field.delete(0, tk.END)
    new_1 = del_item(rem_item=input_text_3)
    display_message(f"You have deleted the option '{input_text_3}'.")
    display_message(f"Current options: \n{new_1}")
    display_menu()

def display_menu():
    list_names = sort_cont()
    output_text.set("Routes of access:\n" + "\n".join([f"{1+i}. {name}" for i, name in enumerate(list_names)]))
    input_field.focus()

def display_response(message):
    output_text.set(message + "\n\nType a number to choose an option or type 'exit' to quit")

def display_message(message):
    output_text.set(message)

app = tk.Tk()
app.title("Administrator")
app.geometry("1500x900")
app.configure(bg='black')

output_text = tk.StringVar()
output_text.set("")

output_label = tk.Label(app, textvariable=output_text, fg="white", bg="black", font=("Courier", 12), justify="left")
output_label.pack(pady=20, padx=20, anchor="w")

input_field = tk.Entry(app, font=("Courier", 14), fg='white', bg='black', insertbackground='white', width=40)
input_field.pack(pady=10)
input_field.bind("<Return>", handle_input)

display_menu()

app.mainloop()
