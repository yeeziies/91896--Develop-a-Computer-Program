import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

app = Tk()
app.title("Math Quiz")

app.geometry("550x500")  # Set Window Size
app.resizable(False, False)  # Do not allow window resize

# Load image safely
button_img = None
try:
    button_img = PhotoImage(file="C:/Users/21300/Downloads/KUREMI.png")
except Exception as e:
    print(f"Error loading image: {e}")

if button_img:
    cool_button = Button(app, image=button_img)
    cool_button.place(relx=0.5, rely=0.05, anchor='n')
    cool_label = Label(app, image=button_img)
    cool_label.place(relx=0.5, rely=0.25, anchor='n')
else:
    print("No Image")

# Variables to store current numbers and widgets for messages
current_num1 = None
current_num2 = None
question_label = None
message_label = None

def generate_question():
    global current_num1, current_num2, question_label, message_label
    current_num1 = random.choice(num)
    current_num2 = random.choice(num)
    question_text = f"{current_num1} + {current_num2} = ?"

    # Remove old question label if exists
    if question_label:
        question_label.destroy()
    question_label = Label(app, text=question_text, font=("Courier", 16))
    question_label.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

    # Clear previous message
    if message_label:
        message_label.destroy()

def check_answer(user_entry):
    global message_label
    user_input = user_entry.get()

    # Remove old message label
    if message_label:
        message_label.destroy()

    # Validation
    if user_input == "":
        message_label = Label(app, text="NO BLANKS!", fg="RED", font=("Comic Sans MS", 16))
        message_label.place(relx=0.3, rely=0.1)
        return
    if not user_input.isdigit():
        if user_input.isalnum():
            message_label = Label(app, text="NO LETTERS!", fg="RED", font=("Comic Sans MS", 16))
            message_label.place(relx=0.3, rely=0.1)
        elif " " in user_input:
            message_label = Label(app, text="No Spaces Allowed!", fg="RED", font=("Comic Sans MS", 16))
            message_label.place(relx=0.3, rely=0.1)
        else:
            message_label = Label(app, text="No Symbols Allowed!", fg="RED", font=("Comic Sans MS", 16))
            message_label.place(relx=0.3, rely=0.1)
        return
    if len(user_input) > 6:
        message_label = Label(app, text="Character Limit is 6", fg="RED", font=("Comic Sans MS", 16))
        message_label.place(relx=0.3, rely=0.1)
        return

    # Check answer
    if int(user_input) == (current_num1 + current_num2):
        message_label = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        message_label.place(relx=0.3, rely=0.2)
    else:
        message_label = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
        message_label.place(relx=0.3, rely=0.2)

def on_start():
    generate_question()

# Start button
start_button = Button(app, text="Start", command=on_start)
start_button.place(relx=0.45, rely=0.2)

# Entry text box
user_entry = Entry(app)
user_entry.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

# Submit button
submit_button = Button(app, text="Submit", command=lambda: check_answer(user_entry))
submit_button.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

# Try Again button - just generates a new question
try_again_button = Button(app, text="Try Again", command=generate_question)
try_again_button.place(relx=0.39, rely=0.9)

app.mainloop()
