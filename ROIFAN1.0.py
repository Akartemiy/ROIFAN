import os

def replace_text_in_file(file_path, search_text, replace_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated_content = content.replace(search_text, replace_text)
        updated_content = updated_content.replace(f"_{search_text}_", f"_{replace_text}_")
        updated_content = updated_content.replace(f"_ {search_text} _", f"_ {replace_text} _")

        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated content in: {file_path}")
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"Could not process {file_path}: {e}")

def replace_in_folder(folder_path, search_text, replace_text):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_text_in_file(file_path, search_text, replace_text)
            
            if search_text in file:
                new_file_name = file.replace(search_text, replace_text)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {file_path} -> {new_file_path}")
        
        for dir_name in dirs:
            if search_text in dir_name:
                dir_path = os.path.join(root, dir_name)
                new_dir_name = dir_name.replace(search_text, replace_text)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dir_path} -> {new_dir_path}")

if __name__ == "__main__":
    base_folder = "."
    search_text = "Your old text"
    replace_text = "Your new text"

    print(f"Starting replacement of '{search_text}' with '{replace_text}' in folder: {base_folder}")
    replace_in_folder(base_folder, search_text, replace_text)
    print("Replacement complete.")