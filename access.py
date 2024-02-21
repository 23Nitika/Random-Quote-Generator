import tkinter as tk
import requests
import json
from tkinter import ttk

def fetch_data():
    try: 
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        content = data.get('content', 'Quote not found')
        author = data.get('author', 'Author not found')
        quote_label.config(text=f"\"{content}\"", foreground="#4717F6")
        author_label.config(text=f"- {author}", foreground="#A239CA")
    except Exception as e:
        quote_label.config(text="Error: "+str(e), foreground="red")

root = tk.Tk()
root.geometry("400x200")
root.title("Random Quote Viewer")
root.configure(bg="#0E0B16")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), foreground="#813772", background="black")
style.configure("TLabel", font=("Helvetica",14))

quote_frame = ttk.Frame(root)
quote_frame.pack(pady=20)

quote_label = ttk.Label(root, text="Quote will be displayed here", wraplength=300, anchor="center")
quote_label.pack()

author_label = ttk.Label(root, text="Author will be displayed here", font=("Helvetica", 12))
author_label.pack(pady=10)

fetch_button = ttk.Button(root, text="Fetch Quote", command=fetch_data, style="TButton")
fetch_button.pack()

root.mainloop()