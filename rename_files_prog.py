import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Allowed image extensions (case-insensitive)
ALLOWED_EXTENSIONS = {'.png', '.svg', '.jpeg', '.jpg'}
MAX_NAME_LENGTH = 20  # max characters (excluding extension)

def rename_image_files_in_folder(folder_path):
    renamed_count = 0

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        # Split name and extension
        name, ext = os.path.splitext(filename)

        # Check file type
        if os.path.isfile(old_path) and ext.lower() in ALLOWED_EXTENSIONS:
            # Replace spaces with hyphens
            new_name = name.replace(' ', '-')
            new_name = new_name.replace('(', '')
            new_name = new_name.replace(')', '')

            # Truncate from the beginning if too long
            if len(new_name) > MAX_NAME_LENGTH:
                new_name = new_name[-MAX_NAME_LENGTH:]

            new_filename = new_name + ext
            new_path = os.path.join(folder_path, new_filename)

            # Avoid overwriting existing files
            if os.path.exists(new_path):
                counter = 1
                while True:
                    candidate = f"{new_name}_{counter}{ext}"
                    candidate_path = os.path.join(folder_path, candidate)
                    if not os.path.exists(candidate_path):
                        new_filename = candidate
                        new_path = candidate_path
                        break
                    counter += 1

            os.rename(old_path, new_path)
            renamed_count += 1

    return renamed_count

def main():
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(title="Select a folder to process")

    if folder:
        count = rename_image_files_in_folder(folder)
        messagebox.showinfo("Done", f"Renamed {count} image file(s)." if count else "No matching image files found.")

if __name__ == "__main__":
    main()
