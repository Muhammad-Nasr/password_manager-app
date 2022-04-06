from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters  = [random.choice(letters) for i in range (random.randint(6, 10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 6))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 6))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get().title()
    user_name = user_entry.get()
    password = pass_entry.get()
    data_dict = {website: {"user_name": user_name, "password": password}}

    if website == "" or password == "":
        messagebox.showinfo(title="OOPS", message="please don't leave any field empty")

    else:
        message_box = messagebox.askyesno(title= website, message=f"this is the details entered:\n"
                    f"your email {user_name}\n"f"password:{password}\nis it ok to save ")

        if message_box:
                          # load data
            try:
                with open("password_data.json", mode="r") as file:
                    new_data = json.load(file)



                           # add data to the file
            except (FileNotFoundError, ValueError):    ## when the file is empty or not exist
                with open("password_data.json", mode="w") as file:
                    json.dump(data_dict, file, indent=4)

            else:
                      #update data
                new_data.update(data_dict)
                       #saving updated data
                with open("password_data.json", mode="w") as file:
                    json.dump(new_data,file, indent=4)

            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

#--------------- Find Data-------------------------#
def find_data():
    search_web = web_entry.get().title()

    try:
        with open("password_data.json", mode="r") as data:
            data_search = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title=search_web, message="No data file found")

    else:

        if search_web in data_search:
            find_user = data_search[search_web]["user_name"]
            find_password = data_search[search_web]["password"]
            messagebox.showinfo(title=search_web, message=f"Email: {find_user}\nPassword: {find_password}")

        else:
            messagebox.showinfo(title=search_web, message="You don't have data before")



# ---------------------------- UI SETUP ------------------------------- #
# construct a tk class
window = Tk()
window.title("         Password Manager")
window.config(padx=50, pady=50)

# construct a canvas
canvas = Canvas(width=200, height=200)

pass_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=pass_img )
canvas.grid(column=1, row=0)

# construct a first web input label ant entry
web_label = Label(text ="Website:")
web_label.grid(column=0, row=1, sticky="EW")

web_entry = Entry()
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
web_entry.focus()

# create a second input user name
user_label = Label(text = "Email / UserName:")
user_label.grid(row=2, column=0, sticky="EW")

user_entry = Entry()
user_entry.grid(row=2, column=1, columnspan=2 , sticky="EW")
user_entry.insert(0, "mnasreldin2@gmail.com")

# create third pass entry
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry()
pass_entry.grid(row=3, column=1, columnspan=2, sticky="EW")

# create  buttons
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2 , sticky="EW")


add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_data)
search_button.grid(row=1, column=2, sticky="EW")


window.mainloop()
