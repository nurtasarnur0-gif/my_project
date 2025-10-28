import os
import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

# Tkinter терезесін жасау
root = tk.Tk()
root.withdraw()  # Негізгі терезені жасыр

# Commit хабарламасын сұрау
commit_message = simpledialog.askstring("Git Commit", "Commit хабарламасын енгізіңіз:")

if commit_message:
    try:
        # Файлдарды қосу
        subprocess.run(["git", "add", "."])

        # Commit жасау
        subprocess.run(["git", "commit", "-m", commit_message])

        # Push жасау
        subprocess.run(["git", "push"])

        messagebox.showinfo("Жетістік", "Commit және push сәтті өтті!")
    except Exception as e:
        messagebox.showerror("Қате", f"Қате пайда болды: {e}")
else:
    messagebox.showwarning("Бос хабарлама", "Commit хабарламасы енгізілмеді.")
