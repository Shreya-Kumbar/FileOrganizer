import os
import shutil
source_folder = r"C:\Users\Shreya\OneDrive\Desktop\testFolder"
print(os.listdir(source_folder))
file_types = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Others": []
    }
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)
    
    if os.path.isfile(file_path):
        file_moved = False
        
        for folder, extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                file_moved=True
                break
                
        print(f"Moved {file_name} to {folder}")

        if not file_moved:
            other_folder= os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            
            print(f"Moved {file_name} to {folder}")
            #prints messages showing which files are moved.