import tkinter as tk
from tkinter import simpledialog, messagebox
from sqlalchemy import create_engine
from pymongo import MongoClient


def create_connection(db_type, username, password, host, port):
    if db_type == 'oracle':
        connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port or 1521}'
    elif db_type == 'sqlserver':
        connection_string = f'mssql+pymssql://{username}:{password}@{host}:{port or 1433}'
    elif db_type == 'mysql':
        connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port or 3306}'
    elif db_type == 'postgres':
        connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port or 5432}'
    elif db_type == 'mongodb':
        connection_string = f'mongodb://{username}:{password}@{host}:{port or 27017}'
    else:
        raise ValueError("Unsupported database type.")

    if db_type == 'mongodb':
        client = MongoClient(connection_string)
        return client
    else:
        engine = create_engine(connection_string)
        return engine


class ConfigApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Database Configuration")

        tk.Label(self, text="Select Database Type:").grid(row=0, column=0, pady=10, padx=10)

        self.db_type = tk.StringVar(self)
        db_options = ["oracle", "sqlserver", "mysql", "postgres", "mongodb"]
        self.db_type.set(db_options[0])

        tk.OptionMenu(self, self.db_type, *db_options).grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self, text="Username:").grid(row=1, column=0, pady=10, padx=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self, text="Password:").grid(row=2, column=0, pady=10, padx=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self, text="Host:").grid(row=3, column=0, pady=10, padx=10)
        self.host_entry = tk.Entry(self)
        self.host_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self, text="Port:").grid(row=4, column=0, pady=10, padx=10)
        self.port_entry = tk.Entry(self)
        self.port_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Button(self, text="Connect", command=self.connect).grid(row=5, column=0, columnspan=2, pady=20)

    def connect(self):
        db_type = self.db_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        host = self.host_entry.get()
        port = self.port_entry.get()

        try:
            connection = create_connection(db_type, username, password, host, port)
            messagebox.showinfo("Success", f"Successfully connected to {db_type} database.")
            if db_type != 'mongodb':
                connection.connect()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")


if __name__ == "__main__":
    app = ConfigApp()
    app.mainloop()
