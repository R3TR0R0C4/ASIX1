import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
import os
import shutil
import zipfile

# Initialize the main window
root = tk.Tk()
root.title("Bloc de Notes")
root.geometry("800x600")

current_folder = os.getcwd()  # Current working directory

# Create frames
folder_frame = ttk.Frame(root)
folder_frame.pack(side=tk.LEFT, fill=tk.Y)

notes_frame = ttk.Frame(root)
notes_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

note_text = tk.Text(notes_frame)
note_text.pack(fill=tk.BOTH, expand=True)

# Create folder buttons
def create_folder():
    folder_name = simpledialog.askstring("Crear Carpeta", "Nom de la Carpeta:")
    if folder_name:
        os.makedirs(os.path.join(current_folder, folder_name))
        load_folders()

def delete_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_folder:
        shutil.rmtree(os.path.join(current_folder, selected_folder))
        load_folders()

def export_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_folder:
        zip_filename = filedialog.asksaveasfilename(defaultextension=".zip")
        if zip_filename:
            shutil.make_archive(zip_filename.replace('.zip', ''), 'zip', os.path.join(current_folder, selected_folder))

def import_folder():
    zip_filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if zip_filename:
        extract_to = filedialog.askdirectory()
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        load_folders()

def open_folder():
    global current_folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        current_folder = folder_path
        load_folders()

ttk.Button(folder_frame, text="Crear Carpeta", command=create_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Eliminar Carpeta", command=delete_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Exportar Carpeta", command=export_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Importar Carpeta", command=import_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Obrir Carpeta", command=open_folder).pack(fill=tk.X)

folder_listbox = tk.Listbox(folder_frame)
folder_listbox.pack(fill=tk.Y, expand=True)

def load_folders():
    folder_listbox.delete(0, tk.END)
    for folder in os.listdir(current_folder):
        if os.path.isdir(os.path.join(current_folder, folder)):
            folder_listbox.insert(tk.END, folder)

def on_folder_select(event):
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_folder:
        load_notes(selected_folder)

folder_listbox.bind("<<ListboxSelect>>", on_folder_select)
load_folders()

# Create note buttons
def create_note():
    note_title = simpledialog.askstring("Crear Nota", "Títol de la Nota:")
    if note_title:
        selected_folder = folder_listbox.get(tk.ACTIVE)
        if selected_folder:
            note_path = os.path.join(current_folder, selected_folder, note_title + ".txt")
            with open(note_path, 'w') as file:
                file.write("")
            load_notes(selected_folder)

def save_note():
    selected_note = notes_listbox.get(tk.ACTIVE)
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)
        with open(note_path, 'w') as file:
            file.write(note_text.get(1.0, tk.END))

def delete_note():
    selected_note = notes_listbox.get(tk.ACTIVE)
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)
        os.remove(note_path)
        load_notes(selected_folder)
        note_text.delete(1.0, tk.END)

ttk.Button(notes_frame, text="Crear Nota", command=create_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Guardar Nota", command=save_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Eliminar Nota", command=delete_note).pack(fill=tk.X)

notes_listbox = tk.Listbox(notes_frame)
notes_listbox.pack(fill=tk.Y, expand=True)

def load_notes(folder):
    notes_listbox.delete(0, tk.END)
    notes_path = os.path.join(current_folder, folder)
    for note in os.listdir(notes_path):
        if note.endswith(".txt"):
            notes_listbox.insert(tk.END, note)

def on_note_select(event):
    selected_note = notes_listbox.get(tk.ACTIVE)
    selected_folder = folder_listbox.get(tk.ACTIVE)
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)
        with open(note_path, 'r') as file:
            content = file.read()
        note_text.delete(1.0, tk.END)
        note_text.insert(tk.END, content)

notes_listbox.bind("<<ListboxSelect>>", on_note_select)

root.mainloop()
