import os
import shutil

def rename_and_organize(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for index, filename in enumerate(files):
        name, ext = os.path.splitext(filename)
        new_filename = f"file_{index + 1}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

        ext_folder = os.path.join(folder_path, ext[1:].lower() + "_files")
        os.makedirs(ext_folder, exist_ok=True)
        shutil.move(new_path, os.path.join(ext_folder, new_filename))

    print("Files renamed and organized successfully.")

rename_and_organize("C:/Users/YourName/Desktop/test_folder")
