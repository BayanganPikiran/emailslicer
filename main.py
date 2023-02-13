from tkinter import *

BACKGROUND_COLOR = "#4649FF"


def result():
    try:
        email = email_entry.get().strip()
        username = email[0:email.index("@")]
        domain = email[email.index("@") + 1:]
        message = f"You entered: {email}\nYour email username is: {username}\nYour email domain is: {domain}"
        results_textbox.insert(END, message)
        email_entry.delete(0, END)
    except:
        results_textbox.delete("1.0", END)
        results_textbox.insert(END, "You're a doofus.\nYou didn't enter a complete email address.\nTry again, numbnuts.")


def reset():
    results_textbox.delete("1.0", END)
    email_entry.delete(0, END)
# ----------------------------WINDOW---------------------------- #


window = Tk()
window.title("Email Slicer")
window.geometry("480x440")
window.resizable(width=FALSE, height=FALSE)
window.configure(background=BACKGROUND_COLOR, padx=20, pady=20)

# ----------------------------LABELS----------------------------#
greeting_label = Label(text="Welcome to the Email Slicer", font=("arial", 11), background="black", foreground="white")

info_label = Label(text="Enter your email address and click the 'slice' button."
                        "\nThe application will extract your username and domain name",
                   font=("arial", 11), background=BACKGROUND_COLOR, foreground="white")

entry_label = Label(text="Enter your email address in the box below", font=("arial", 11), background="black",
                    foreground="white")

results_label = Label(text="The results are as follows:", background="black", foreground="white", font=("arial", 11))

# ----------------------------ENTRY-----------------------------#
e1 = StringVar()
email_entry = Entry(font=11, width=40, textvariable=e1)
email_entry.focus()

# ----------------------------BUTTONS---------------------------#
slice_button = Button(command=result, text="Slice", font=("arial", 11))

reset_button = Button(command=reset, text="Reset", font=("arial", 11))

# ----------------------------TEXTBOX----------------------------#

results_textbox = Text(width=50, height=5, font=("arial", 12))

# ----------------------------PACKING----------------------------#
greeting_label.pack(pady=5)
info_label.pack(pady=5)
entry_label.pack(pady=5)
email_entry.pack(pady=5)
slice_button.pack(pady=5)
reset_button.pack(pady=5)
results_label.pack(pady=10)
results_textbox.pack(pady=15)


window.mainloop()
