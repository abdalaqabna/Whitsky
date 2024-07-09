import tkinter as tk
from tkinter import scrolledtext
import threading


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill=tk.X, expand=False)
        self.entry.bind('<Return>', self.process_command)

        self.send_button = tk.Button(root, text="Send", command=self.process_command)
        self.send_button.pack(padx=10, pady=10)

        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, "Welcome to the Chat App! Type 'help' for a list of commands.\n")
        self.chat_area.configure(state='disabled')

    def process_command(self, event=None):
        command = self.entry.get().strip()
        if command:
            self.entry.delete(0, tk.END)
            self.display_message(f"You: {command}\n")
            threading.Thread(target=self.handle_command, args=(command,)).start()

    def display_message(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message)
        self.chat_area.yview(tk.END)
        self.chat_area.configure(state='disabled')

    def handle_command(self, command):
        if command == 'help':
            response = "Available commands:\n1. help - Show this help message\n2. greet - Greet the user\n3. exit - Close the app"
        elif command == 'greet':
            response = "Hello! How can I assist you today?"
        elif command == 'exit':
            self.root.quit()
            return
        else:
            response = "Unknown command. Type 'help' for a list of available commands."

        self.display_message(f"App: {response}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
