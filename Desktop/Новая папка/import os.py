import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

# Tkinter терезесін жасаймыз, бірақ негізгі терезені көрсетпейміз
root = tk.Tk()
root.withdraw()

# Commit хабарламасын сұрау
commit_message = simpledialog.askstring("Git Commit", "Commit хабарламасын енгізіңіз:")

if commit_message:
    try:
        # Файлдарды қосу
        subprocess.run(["git", "add", "."], check=True)

        # Commit жасау
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push жасау (егер remote орнатылған болса)
        subprocess.run(["git", "push"], check=True)

        messagebox.showinfo("Жетістік", "Commit және push сәтті өтті!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Git қатесі", f"Қате пайда болды:\n{e}")
else:
    messagebox.showwarning("Бос хабарлама", "Commit хабарламасы енгізілмеді.")
