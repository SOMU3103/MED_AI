from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, Frame, Label, VERTICAL, RIGHT, Y, BOTH, END
import google.generativeai as genai
import subprocess
import os

# Constants for paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize the main window
window = Tk()
window.geometry("956x551")
window.configure(bg="#15132C")
window.title("Tech Marvel Chatbot")

# Try to load the icon image
try:
    icon_image = PhotoImage(file=relative_to_assets("image_1.png"))
    window.iconphoto(False, icon_image)
except Exception as e:
    print(f"Could not load icon image: {e}")

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
    outline="")

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


try:
    entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg = canvas.create_image(
        578.0,
        489.0,
        image=entry_image
    )
except Exception as e:
    print(f"Could not load entry image: {e}")
    entry_bg = None

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


try:
    genai.configure(api_key="AIzaSyCaAaW1tKxyM8AUNo482w74SYNyvmb3HmQ")
    
    
    model = None
    for model_name in ["gemini-1.5-pro-latest", "gemini-pro", "chat-bison-001"]:
        try:
            model = genai.GenerativeModel(model_name)
            break
        except:
            continue
    
    if model:
        chat_history.config(state="normal")
        chat_history.insert(END, "AI Assistant ready to help!\n\n")
        chat_history.config(state="disabled")
    else:
        raise Exception("No working model found")
        
except Exception as e:
    print(f"API Error: {e}")
    model = None
    chat_history.config(state="normal")
    chat_history.insert(END, "Error: Failed to initialize AI assistant\n")
    chat_history.config(state="disabled")

# Function to get the bot's response
def get_bot_response(message):
    if not model:
        return "Error: AI model not available."
    
    try:
        response = model.generate_content(
            message,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.8,
                top_k=40,
                max_output_tokens=1024
            )
        )
        return response.text
    except Exception as e:
        print(f"Response Error: {e}")
        return "Sorry, I encountered an error processing your request."

# Function to send a message
def send_message():
    message = user_input.get()
    if message.strip() != "":
        chat_history.config(state="normal")
        chat_history.insert(END, f"You: {message}\n\n")
        user_input.delete(0, END)
        
        bot_response = get_bot_response(message)
        chat_history.insert(END, f"Assistant: {bot_response}\n\n")
        
        chat_history.config(state="disabled")
        chat_history.yview(END)

send_button = Button(
    text="Send",
    command=send_message,
    bg="#3b3368",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    font=("Helvetica", 12, "bold"),
    padx=20,
    pady=10,
    activebackground="#3b3368",
    activeforeground="white"
)
send_button.place(
    x=800,
    y=469,
    width=100,
    height=40.0
)

# Logo and title
try:
    logo_image = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(
        80.0,
        44.0,
        image=logo_image
    )
except Exception as e:
    print(f"Could not load logo image: {e}")

canvas.create_text(
    25.0,
    69.0,
    anchor="nw",
    text="TECH MARVEL",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 15 * -1)
)

# Sidebar buttons
try:
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    image_label = Label(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0
    )
    image_label.place(x=13.0, y=113.0, width=165, height=42)
except Exception as e:
    print(f"Could not load button image 2: {e}")

def open_gui3():
    try:
        script_path = os.path.join(os.path.dirname(__file__), "gui1.py")
        subprocess.Popen(["python", script_path])
        window.destroy()
    except Exception as e:
        print(f"Error opening GUI3: {e}")

try:
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui3,
        relief="flat"
    )
    button_3.place(
        x=10,
        y=155,
        width=170,
        height=65
    )
except Exception as e:
    print(f"Could not load button image 3: {e}")

def open_gui4():
    try:
        script_path = os.path.join(os.path.dirname(__file__), "gui2.py")
        subprocess.Popen(["python", script_path])
        window.destroy()
    except Exception as e:
        print(f"Error opening GUI4: {e}")

try:
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui4,
        relief="flat"
    )
    button_4.place(
        x=10,
        y=230,
        width=175,
        height=50
    )
except Exception as e:
    print(f"Could not load button image 4: {e}")

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
about_label.insert(END, "Med AI is a medical chatbot by the Tech Marvel team\n\n")
about_label.insert(END, "Developed by: Tech Marvel\n")
about_label.config(state="disabled")

# Bind Enter key to send message
user_input.bind('<Return>', lambda event: send_message())

# Make chat history read-only initially
chat_history.config(state="disabled")

window.resizable(False, False)
window.mainloop()