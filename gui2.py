from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, Frame, Label, VERTICAL, RIGHT, Y, BOTH, END
import mysql.connector
import subprocess 

# Constants for paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\somna\VScode\project\page1\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize the main window
window = Tk()
window.geometry("956x551")
window.configure(bg="#15132C")
window.title("Tech Marvel Home remedies ")

icon_image = PhotoImage(file=relative_to_assets("image_1.png"))  # Add your icon file
window.iconphoto(False, icon_image)

# Canvas for drawing the UI
canvas = Canvas(
    window,
    bg="#15132C",
    height=551,
    width=956,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create a rectangle for the chat area
canvas.create_rectangle(
    203.0,
    22.0,
    931.0,
    530.0,
    fill="#191B3B",
    outline=""
)

# Chat history display area
chat_history_frame = Frame(window, bg="#191B3B")
chat_history_frame.place(x=203, y=22, width=728, height=430)

chat_history = Text(
    chat_history_frame,
    bg="#191B3B",
    fg="#FFFFFF",
    wrap="word",
    font=("Arial", 12),
    bd=0,
    highlightthickness=0
)
chat_history.pack(side="left", fill=BOTH, expand=True)

scrollbar = Scrollbar(chat_history_frame, orient=VERTICAL, command=chat_history.yview)
scrollbar.pack(side=RIGHT, fill=Y)
chat_history.config(yscrollcommand=scrollbar.set)

# Entry field for user input
entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg = canvas.create_image(
    578.0,
    489.0,
    image=entry_image
)
user_input = Entry(
    bd=0,
    bg="#3B3368",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial", 12)
)
user_input.place(
    x=261.0,
    y=469.0,
    width=634.0,
    height=38.0
)

send_button = Button(
    text="Send",
    command=lambda: send_message(),  # Added a comma here
    bg="#3b3368",  # Background color (green)
    fg="white",    # Text color (white)
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    font=("Helvetica", 12, "bold"),  # Font style
    padx=20,  # Horizontal padding
    pady=10,  # Vertical padding
    activebackground="#3b3368",  # Background color when clicked
    activeforeground="white"  # Text color when clicked
)

# Place the button in the window
send_button.place(
    x=800,
    y=469,
    width=100,  # Slightly wider for better appearance
    height=40.0
)

# Logo and title
logo_image = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    80.0,
    44.0,
    image=logo_image
)

canvas.create_text(
    25.0,
    69.0,
    anchor="nw",
    text="TECH MARVEL",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 15 * -1)
)
#------------------------------------------------------------------------#
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
image_label = Label(
    window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0
)
image_label.place(x=13, y=100, width=170, height=65)
#--------------------------------------------------------------------#
def open_gui3():
    subprocess.Popen(["python", r"C:\Users\somna\VScode\project\page1\build\gui1.py"])
    window.destroy()
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui3,
    relief="flat"
)
button_3.place(x=13, y=165, width=165, height=53)# Same position as the button
#-------------------------------------------------------------------#
def open_gui2():
    subprocess.Popen(["python", r"C:\Users\somna\VScode\project\page1\build\gui.py"])
    window.destroy()

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
    relief="flat"
)
button_2.place(
    x=10, y=230, width=165, height=50
)
#--------------------------------------------------------------------------#
# About section
about_frame = Frame(window, bg="#15132C")
about_frame.place(x=10, y=300, width=180, height=200)

about_label = Text(
    about_frame,
    bg="#15132C",
    fg="#FFFFFF",
    wrap="word",
    font=("Arial", 10),
    bd=0,
    highlightthickness=0
)
about_label.pack(fill=BOTH, expand=True)
about_label.insert(END, "About Tech Marvel:\n\n")
about_label.insert(END, "Med AI is a medical chatbot by the Tech Marvel team, CSE Department, Mahendra Institute of Technology\n\n")
about_label.insert(END, "Developed by: Tech Marvel\n")
about_label.config(state="disabled")  # Make the text read-only

#--------------------------------------------------------------------------#
# MySQL Connection Function
def get_doctor_suggestion(symptom):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="somu"
        )
        cursor = conn.cursor(dictionary=True)

        # Fetch doctors where specialization matches symptom
        query = "SELECT * FROM home_remedies WHERE symptom LIKE %s"
        cursor.execute(query, ("%"+symptom+"%",))

        doctors = cursor.fetchall()

        if doctors:
            response_text = "Home_remedy🌿💊:\n"
            for doctor in doctors:
                response_text += f"{doctor['remedy']}\nMedicine: {doctor['medicine']} \n"
                return response_text
        else:
            return "Sorry, no doctors found for this symptom."

    except mysql.connector.Error as err:
        return f"Database Error: {err}"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to send a message
def send_message():
    message = user_input.get()
    if message.strip() != "":
        chat_history.insert(END, f"You: {message}\n\n")
        user_input.delete(0, END)

        # Fetch doctor details from MySQL database
        bot_response = get_doctor_suggestion(message)
        
        chat_history.insert(END, f"Doctor: {bot_response}\n\n")
        chat_history.yview(END)

window.resizable(False, False)
window.mainloop()
