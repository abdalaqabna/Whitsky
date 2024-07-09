import tkinter as tk
import requests



def send_input():
    user_input = entry.get()
    response = requests.post('http://127.0.0.1:5000/process_input', json={'input': user_input})
    result_label.config(text=response.json().get('message'))

# Set up the GUI
root = tk.Tk()
root.title('Desktop App')

tk.Label(root, text='Enter something:').pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text='Send', command=send_input).pack()
result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
