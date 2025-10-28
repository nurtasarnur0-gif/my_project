import subprocess

# Commit хабарламасын консольдан сұрау
commit_message = input("Commit хабарламасын енгізіңіз: ")

if commit_message:
    try:
        # Барлық файлдарды қосу
        subprocess.run(["git", "add", "."], check=True)

        # Commit жасау
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push жасау
        subprocess.run(["git", "push"], check=True)

        print("Commit және push сәтті өтті!")
    except subprocess.CalledProcessError as e:
        print(f"Қате пайда болды: {e}")
else:
    print("Commit хабарламасы енгізілмеді.")
