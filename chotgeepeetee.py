import os
os.system("pip install groq")
os.system("pip install customtkinter")
os.system("pip install pillow")
import tkinter.messagebox
from groq import Groq
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import *
import tkinter
current_color = "#000000"
opposite_color = "#ffffff"
from tkinter import filedialog
from PIL import Image, ImageTk
upload = "default"
img = Image.open("ChotGPT.ico")
img2 = Image.open("user.jpg")



def apply_icon(w):
    try:
        icon = tk.PhotoImage(data=icondata)
        w.iconphoto(True, icon)
    except Exception as e:
        print("Could not load icon due to:\n  ",e)

icondata = '''
R0lGODdhQABAAIMAABm1fvv9/Sy7iLLm00vFmnTSsdny6WXNqZbdxB62gMru4VnKoobYuzvAkcLr
3Z3gyCwAAAAAQABAAEAI/wABCBxIsKDBgwgTKlzIEGEDAwECDBgQsWLEAQUaNNzI8IHFAwYFILA4
QCNHAAIucmxQkQHBlBEJECRQEQFFixFBIiSgwGLPAAs4MohJsADOAQQOEE0IE4FAATclvoTo4OTP
qBERCDgIFadWAEalEqRoIMFAAT8dbBW6dGPYi2tnWnR6si5XAUkZDPjp1a7fv4ADF62okytWBQcO
YA1g4MGCuH4XVCRAsy2AygFkGiSwuCXkygU43oQM4KZmgUoDFD6IOYCCoFwhZt4IU7XCA7IZFyAt
suKAqYzNnoX4W3REyAkO8PVNemDqAJBvFvj5QDDKBQwc4Iyo3eKD5gLDKv8Ab728+fPo0xN8eHG3
esGSI7osmKBBgc4SD5A3j3U1QdwWMUCeAPfhdJpdb00mV0Sv3aaAAbAZNBJ0J7GUk0AWzjYQZoVx
hlNozuXWYGmM7bcgiAMlINuBz2VlUgIJDjAgVsUxBFONAt20WmoHhnRRd/KRlpp/CanoGmtAKqhQ
T1WdFVFZg2nIUIIBfIUQgRY5MN12OAIAEZRR9pgQaAItsNhXCY64oUpjHYcSdXbBVB1XBRQgnEEL
5GblQB5VNCdgCeCkAAL6GZTAUB8dlACQdL1HUH0F5GaRAQ4gUMACBOClpKOcdurpp6CGKipHeJk4
akLsCYpApqcmFF8A8wn/sAACkjJIqKnqPTffTrVW1Nhj74mEqG1cDavbnQQuZsCqdwLWp2UbYrWn
QgT+hKJfxkoJAIwkiZnifj0p8Ndbwx6ImbcCecicQWGh6yphALxqbkURpouVAwQ0gJWdT7HZUIa7
1jbvherW1FxvzCGKKwCINvrUilF6tQBf+CLEbV82+iuQkdo+V1JIE0bEL2u5LTxkQab9B21Bta1r
kHQbaWcAZCEjhdrKL2UF1qT1WrjrQpX9fBl+2vooVngMouymjT+Rt0CSCDRbUGU4wgRmuvJtFJV7
FkfqK2wX+/bol1KP9u92Ve4nQLaMHYBol2Q1i5bIGylccFafSfox0kfnbLj03BIt3G/fEwtq0cgL
NjnQTQ0IINufJ4VV78YABlAxVzUXlC3kdvV0NW1RGSBmi5z7RTXXCukbYGw1nacY2pWyypNPJr0M
l9TpyUor2oHjHm9Fgqd33wC98n5tq0w1sEABD0yE/PPQRw9qQAA7
'''


# Create the Groq client
client = Groq(api_key="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", )

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":
    "The first message the user sends sets the personality for the conversation."
}
def save_chathistory():
    # Open a file dialog to select the file location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save Chat History"
    )
      # Check if a file path was selected
    if file_path:
        # Write the chathistory list to the selected file
        with open(file_path, 'a') as file:
            for line in chathistory:
                file.write(str(line) + '\n')
        

        print(f"Chat history saved to {file_path}")


# Initialize the chat history
chat_history = [system_prompt]
chathistory = []

def change_color():
    global current_color
    global opposite_color
    if  current_color == "#ffffff":
        current_color = ("#000000")
        opposite_color = ("#ffffff")
    else:
        current_color = ("#ffffff")
        opposite_color = ("#000000")
    root.configure(bg=current_color)
    chat_output.configure(bg=current_color)
    chat_output.configure(fg=opposite_color)
    chat_frame.configure(bg=current_color)
    label.configure(bg=current_color)
    input_entry.configure(bg=current_color)
    input_entry.configure(fg=opposite_color)
    
def UploadAction(event=None):
            filename = filedialog.askopenfilename()
            print(filename)
            txtfile = open(filename,'r')
            data = txtfile.read()
            chat_history.append({
                "role": "system", 
                "content": "Continue acting how you were before, this is your old chat log: " + str(data)  })
            
            
            print(str(data))
            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, str(data))
            chat_output.config(state=tk.DISABLED)
            
            




def send_message():
    user_input = input_entry.get("1.0", tk.END).strip()
    if user_input:
        chat_history.append({"role": "user", "content": user_input})
        

        chat_output.config(state=tk.NORMAL)
        chat_output.image_create("current",image=image2)
        chat_output.insert(tk.END, f"User: {user_input}\n")
        appendvar2 = (f"User: {user_input}")
        print(str(appendvar2))
        chathistory.append(appendvar2)
        chat_output.config(state=tk.DISABLED)
        input_entry.delete("1.0", tk.END)

        response = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=chat_history,
                                                max_tokens=100,
                                               temperature=1.2)
        chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        chat_output.config(state=tk.NORMAL)
        appendvar = (f"V3ectorGPT: {response.choices[0].message.content}\n")
        print(str(appendvar))
        chathistory.append(appendvar)
        chat_output.image_create("current",image=image)
        chat_output.insert(tk.END, f"V3ectorGPT: {response.choices[0].message.content}\n")
        
        chat_output.config(state=tk.DISABLED)
        
        chat_output.see(tk.END)  # Scroll to the bottom

# Create the main window
root = tk.Tk()
apply_icon(root)
root.geometry('1000x1000')


     
    



# root has no image argument, so use a label as a panel

root.title("ChotGeePeeTee")
root.configure(bg=current_color)  # White background

# Create a frame to hold the chat output and scrollbar
chat_frame = tk.Frame(root, bg=current_color)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create the chat output area
chat_output = tk.Text(chat_frame, state=tk.DISABLED, wrap=tk.WORD, bg=current_color, fg=opposite_color, font=("Consolas", 12))
chat_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the vertical scrollbar
scrollbar = tk.Scrollbar(chat_frame, command=chat_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the text widget to use the scrollbar
chat_output.config(yscrollcommand=scrollbar.set)

# Create the input area
input_entry = tk.Text(root, height=1, bg=current_color, fg=opposite_color, font=("Consolas", 12))
input_entry.pack(fill=tk.X)

# Create the send button
send_button = ctk.CTkButton(root, text="Send", command=send_message, fg_color=fg_color="#7DDA58", hover_color="#5EA941", text_color="#ffffff", font=("Consolas", 12))
send_button.pack(side=tk.RIGHT)

image = ImageTk.PhotoImage(img)
image2 = ImageTk.PhotoImage(img2)

chat_output.config(state=tk.NORMAL)
chat_output.insert(tk.END, "Welcome to V3ectorGPT! The first message you send will set the personaloty for this conversation.\n")
chat_output.config(state=tk.DISABLED)
            

load_button = ctk.CTkButton(root, text="Load Chat Log", command=UploadAction, fg_color="#7DDA58", hover_color="#5EA941", text_color="#ffffff", font=("Consolas", 12))
load_button.pack(side=tk.LEFT)

save_button = ctk.CTkButton(root, text="Save chat log", command=save_chathistory, fg_color="#7DDA58", hover_color="#5EA941", text_color="#ffffff",, font=("Consolas", 12))
save_button.pack(side=tk.LEFT)

# Bind the <Return> key to the send_message function
root.bind("<Return>", lambda event: send_message())

# Auto-resize window when fullscreened
def resize_window(event):
    if root.state() == "zoomed":
        root.update_idletasks()
        root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
button = ctk.CTkButton(root, text="Change theme", command=change_color, fg_color="#7DDA58", hover_color="#5EA941", text_color="#ffffff", font=("Consolas", 12))
button.pack(side=tk.RIGHT)
label = tk.Label(root, text="", bg=current_color, width=20, height=5)
label.pack()



root.bind("<Configure>", resize_window)
root.mainloop()
