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
img = Image.open("chotGPT.ico")
img2 = Image.open("user.jpg")



def apply_icon(w):
    try:
        icon = tk.PhotoImage(data=icondata)
        w.iconphoto(True, icon)
    except Exception as e:
        print("Could not load icon due to:\n  ",e)

icondata = '''
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
mg6aMlIfMn21P+Q5q1rXutaAAAA7
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
send_button = ctk.CTkButton(root, text="Send", command=send_message, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
send_button.pack(side=tk.RIGHT)

image = ImageTk.PhotoImage(img)
image2 = ImageTk.PhotoImage(img2)

chat_output.config(state=tk.NORMAL)
chat_output.insert(tk.END, "Welcome to V3ectorGPT! The first message you send will set the personaloty for this conversation.\n")
chat_output.config(state=tk.DISABLED)
            

load_button = ctk.CTkButton(root, text="Load Chat Log", command=UploadAction, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
load_button.pack(side=tk.LEFT)

save_button = ctk.CTkButton(root, text="Save chat log", command=save_chathistory, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
save_button.pack(side=tk.LEFT)

# Bind the <Return> key to the send_message function
root.bind("<Return>", lambda event: send_message())

# Auto-resize window when fullscreened
def resize_window(event):
    if root.state() == "zoomed":
        root.update_idletasks()
        root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
button = ctk.CTkButton(root, text="Change theme", command=change_color, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
button.pack(side=tk.RIGHT)
label = tk.Label(root, text="", bg=current_color, width=20, height=5)
label.pack()



root.bind("<Configure>", resize_window)
root.mainloop()
