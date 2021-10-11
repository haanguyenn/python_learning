import tkinter
from tkinter import END
from tkinter import messagebox
import random
import pyperclip

# TODO: 2.Password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


def generate_password():
    password_entry.delete(0, END)

    random_letters = random.randint(3, 7)
    random_symbols = random.randint(1, 3)
    random_numbers = random.randint(1, 3)

    password_list = []

    password_list += [random.choice(letters) for char in range(random_letters)]
    password_list += [random.choice(symbols) for char in range(random_symbols)]
    password_list += [random.choice(numbers) for char in range(random_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)  # copy and paste clipboard function

# TODO: 3.Save password


def add():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if len(email_input) == 0 or len(website_input) == 0 or len(password_input) == 0:
        is_blank = messagebox.showerror(title='Alert!', message='Do not leave any fields empty')
        print(is_blank)
    else:
        is_ok = messagebox.askokcancel(title='Confirm',
                                       message=f'Are you sure you want to add this information? \n '
                                               f'Website: {website_input}\n Email: {email_input}\n Password: {password_input}')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website_input} | {email_input} |{password_input}\n')
            clear_field()


def clear_field():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# TODO: 1.Create UI
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=100, pady=100)

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file='logo.png')
create_img = canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=2)

# create Label
website_txt = tkinter.Label()
website_txt.config(text='Website: ')
website_txt.grid(row=2, column=1)

email_txt = tkinter.Label()
email_txt.config(text='Email/Username: ')
email_txt.grid(row=3, column=1)

password_txt = tkinter.Label()
password_txt.config(text='Password: ')
password_txt.grid(row=4, column=1)

# create entry
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.insert(0, 'lynn@1pac.vn')  # get 2 params: index & string
email_entry.grid(row=3, column=2, columnspan=2)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=4, column=2)

# create button
generate_btn = tkinter.Button(text='Generate Button', padx=10, command=generate_password)
generate_btn.grid(row=4, column=3)

add_btn = tkinter.Button(text='Add', width=36, command=add)
add_btn.grid(row=5, column=2, columnspan=2)

window.mainloop()
