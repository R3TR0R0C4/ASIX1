"""import tkinter as tk  # Importing tkinter for GUI
from tkinter import ttk, filedialog, simpledialog  # Importing additional tkinter modules
import os  # Module for operating system interactions
import shutil  # Module for file operations
import zipfile  # Module for handling ZIP files

# Initialize the main window
root = tk.Tk()
root.title("Bloc de Notes")  # Setting the window title
root.geometry("800x600")  # Setting the window size

current_folder = os.getcwd()  # Get the current working directory

# Create two frames: one for folders, one for notes
folder_frame = ttk.Frame(root)
folder_frame.pack(side=tk.LEFT, fill=tk.Y)  # Left side, fills vertically

notes_frame = ttk.Frame(root)
notes_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Left side, fills both vertically and horizontally

note_text = tk.Text(notes_frame)  # Text area for displaying note content
note_text.pack(fill=tk.BOTH, expand=True)

# Function to create a new folder
def create_folder():
    folder_name = simpledialog.askstring("Crear Carpeta", "Nom de la Carpeta:")  # Prompt for folder name
    if folder_name:
        os.makedirs(os.path.join(current_folder, folder_name))  # Create the folder
        load_folders()  # Refresh the folder list

# Function to delete a selected folder
def delete_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        shutil.rmtree(os.path.join(current_folder, selected_folder))  # Delete the folder
        load_folders()  # Refresh the folder list

# Function to export a selected folder as a ZIP file
def export_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        zip_filename = filedialog.asksaveasfilename(defaultextension=".zip")  # Prompt for ZIP file name
        if zip_filename:
            shutil.make_archive(zip_filename.replace('.zip', ''), 'zip', os.path.join(current_folder, selected_folder))  # Create the ZIP file

# Function to import a ZIP file and extract it
def import_folder():
    zip_filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])  # Prompt for ZIP file
    if zip_filename:
        extract_to = filedialog.askdirectory()  # Prompt for extraction location
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_to)  # Extract the ZIP file
        load_folders()  # Refresh the folder list

# Function to open a different folder
def open_folder():
    global current_folder
    folder_path = filedialog.askdirectory()  # Prompt for folder path
    if folder_path:
        current_folder = folder_path  # Set the new current folder
        load_folders()  # Refresh the folder list

# Create buttons for folder operations
ttk.Button(folder_frame, text="Crear Carpeta", command=create_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Eliminar Carpeta", command=delete_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Exportar Carpeta", command=export_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Importar Carpeta", command=import_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Obrir Carpeta", command=open_folder).pack(fill=tk.X)

# Listbox to display folders
folder_listbox = tk.Listbox(folder_frame)
folder_listbox.pack(fill=tk.Y, expand=True)

# Function to load and display folders
def load_folders():
    folder_listbox.delete(0, tk.END)  # Clear the listbox
    for folder in os.listdir(current_folder):
        if os.path.isdir(os.path.join(current_folder, folder)):
            folder_listbox.insert(tk.END, folder + '/')  # Add folder to listbox with "/"

# Function to load notes when a folder is selected
def on_folder_select(event):
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        load_notes(selected_folder)  # Load notes in the selected folder

folder_listbox.bind("<<ListboxSelect>>", on_folder_select)  # Bind folder selection event

# Function to handle double-click event on folders
def on_folder_double_click(event):
    global current_folder
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        current_folder = os.path.join(current_folder, selected_folder)  # Update the current folder path
        load_folders()  # Refresh the folder list

folder_listbox.bind("<Double-1>", on_folder_double_click)  # Bind double-click event
load_folders()  # Load folders initially

# Function to create a new note
def create_note():
    note_title = simpledialog.askstring("Crear Nota", "Títol de la Nota:")  # Prompt for note title
    if note_title:
        selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
        if selected_folder:
            note_path = os.path.join(current_folder, selected_folder, note_title + ".txt")  # Create note path
            with open(note_path, 'w') as file:
                file.write("")  # Create an empty note
            load_notes(selected_folder)  # Refresh the notes list

# Function to save the current note
def save_note():
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        with open(note_path, 'w') as file:
            file.write(note_text.get(1.0, tk.END))  # Save note content

# Function to delete the current note
def delete_note():
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        os.remove(note_path)  # Delete the note
        load_notes(selected_folder)  # Refresh the notes list
        note_text.delete(1.0, tk.END)  # Clear the text area

# Create buttons for note operations
ttk.Button(notes_frame, text="Crear Nota", command=create_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Guardar Nota", command=save_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Eliminar Nota", command=delete_note).pack(fill=tk.X)

# Listbox to display notes
notes_listbox = tk.Listbox(notes_frame)
notes_listbox.pack(fill=tk.Y, expand=True)

# Function to load and display notes in a folder
def load_notes(folder):
    notes_listbox.delete(0, tk.END)  # Clear the listbox
    notes_path = os.path.join(current_folder, folder)
    for note in os.listdir(notes_path):
        if note.endswith(".txt"):
            notes_listbox.insert(tk.END, note)  # Add note to listbox

# Function to display selected note content
def on_note_select(event):
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        with open(note_path, 'r') as file:
            content = file.read()  # Read the note content
        note_text.delete(1.0, tk.END)  # Clear the text area
        note_text.insert(tk.END, content)  # Insert the note content

notes_listbox.bind("<<ListboxSelect>>", on_note_select)  # Bind note selection event

# Start the main loop
root.mainloop()
"""


import tkinter as tk  # Importing tkinter for GUI
from tkinter import ttk, filedialog, simpledialog  # Importing additional tkinter modules
import os  # Module for operating system interactions
import shutil  # Module for file operations
import zipfile  # Module for handling ZIP files

# Initialize the main window
root = tk.Tk()
root.title("Bloc de Notes")  # Setting the window title
root.geometry("800x600")  # Setting the window size

current_folder = os.getcwd()  # Get the current working directory

# Create two frames: one for folders, one for notes
folder_frame = ttk.Frame(root)
folder_frame.pack(side=tk.LEFT, fill=tk.Y)  # Left side, fills vertically

notes_frame = ttk.Frame(root)
notes_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Left side, fills both vertically and horizontally

note_text = tk.Text(notes_frame)  # Text area for displaying note content
note_text.pack(fill=tk.BOTH, expand=True)

# Function to create a new folder
def create_folder():
    folder_name = simpledialog.askstring("Crear Carpeta", "Nom de la Carpeta:")  # Prompt for folder name
    if folder_name:
        os.makedirs(os.path.join(current_folder, folder_name))  # Create the folder
        load_folders()  # Refresh the folder list

# Function to delete a selected folder
def delete_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        shutil.rmtree(os.path.join(current_folder, selected_folder))  # Delete the folder
        load_folders()  # Refresh the folder list

# Function to export a selected folder as a ZIP file
def export_folder():
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        zip_filename = filedialog.asksaveasfilename(defaultextension=".zip")  # Prompt for ZIP file name
        if zip_filename:
            shutil.make_archive(zip_filename.replace('.zip', ''), 'zip', os.path.join(current_folder, selected_folder))  # Create the ZIP file

# Function to import a ZIP file and extract it
def import_folder():
    zip_filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])  # Prompt for ZIP file
    if zip_filename:
        extract_to = filedialog.askdirectory()  # Prompt for extraction location
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_to)  # Extract the ZIP file
        load_folders()  # Refresh the folder list

# Function to open a different folder
def open_folder():
    global current_folder
    folder_path = filedialog.askdirectory()  # Prompt for folder path
    if folder_path:
        current_folder = folder_path  # Set the new current folder
        load_folders()  # Refresh the folder list

# Create buttons for folder operations
ttk.Button(folder_frame, text="Crear Carpeta", command=create_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Eliminar Carpeta", command=delete_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Exportar Carpeta", command=export_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Importar Carpeta", command=import_folder).pack(fill=tk.X)
ttk.Button(folder_frame, text="Obrir Carpeta", command=open_folder).pack(fill=tk.X)

# Listbox to display folders
folder_listbox = tk.Listbox(folder_frame)
folder_listbox.pack(fill=tk.Y, expand=True)

# Function to load and display folders
def load_folders():
    folder_listbox.delete(0, tk.END)  # Clear the listbox
    for folder in os.listdir(current_folder):
        if os.path.isdir(os.path.join(current_folder, folder)):
            folder_listbox.insert(tk.END, folder + '/')  # Add folder to listbox with "/"

# Function to load notes when a folder is selected
def on_folder_select(event):
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        load_notes(selected_folder)  # Load notes in the selected folder

folder_listbox.bind("<<ListboxSelect>>", on_folder_select)  # Bind folder selection event

# Function to handle double-click event on folders
def on_folder_double_click(event):
    global current_folder
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_folder:
        current_folder = os.path.join(current_folder, selected_folder)  # Update the current folder path
        load_folders()  # Refresh the folder list

folder_listbox.bind("<Double-1>", on_folder_double_click)  # Bind double-click event
load_folders()  # Load folders initially

# Function to create a new note
def create_note():
    note_title = simpledialog.askstring("Crear Nota", "Títol de la Nota:")  # Prompt for note title
    if note_title:
        selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
        if selected_folder:
            note_path = os.path.join(current_folder, selected_folder, note_title + ".txt")  # Create note path
            with open(note_path, 'w') as file:
                file.write("")  # Create an empty note
            load_notes(selected_folder)  # Refresh the notes list

# Function to save the current note
def save_note():
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        with open(note_path, 'w') as file:
            file.write(note_text.get(1.0, tk.END))  # Save note content

# Function to delete the current note
def delete_note():
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        os.remove(note_path)  # Delete the note
        load_notes(selected_folder)  # Refresh the notes list
        note_text.delete(1.0, tk.END)  # Clear the text area

# Create buttons for note operations
ttk.Button(notes_frame, text="Crear Nota", command=create_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Guardar Nota", command=save_note).pack(fill=tk.X)
ttk.Button(notes_frame, text="Eliminar Nota", command=delete_note).pack(fill=tk.X)

# Listbox to display notes
notes_listbox = tk.Listbox(notes_frame)
notes_listbox.pack(fill=tk.Y, expand=True)

# Function to load and display notes in a folder
def load_notes(folder):
    notes_listbox.delete(0, tk.END)  # Clear the listbox
    notes_path = os.path.join(current_folder, folder)
    for note in os.listdir(notes_path):
        if note.endswith(".txt"):
            notes_listbox.insert(tk.END, note)  # Add note to listbox

# Function to display selected note content
def on_note_select(event):
    selected_note = notes_listbox.get(tk.ACTIVE)  # Get the selected note
    selected_folder = folder_listbox.get(tk.ACTIVE).rstrip('/')  # Get the selected folder
    if selected_note and selected_folder:
        note_path = os.path.join(current_folder, selected_folder, selected_note)  # Create note path
        if os.path.exists(note_path):  # Check if the note file exists
            with open(note_path, 'r') as file:
                content = file.read()  # Read the note content
            note_text.delete(1.0, tk.END)  # Clear the text area
            note_text.insert(tk.END, content)  # Insert the note content
        else:
            note_text.delete(1.0, tk.END)  # Clear the text area if file not found

notes_listbox.bind("<<ListboxSelect>>", on_note_select)  # Bind note selection event

# Start the main loop
root.mainloop()
