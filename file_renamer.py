import os

def rename_files():
    print("\n--- File Renamer Tool ---")
    folder_path = input("Enter the folder path: ").strip()
    
    # Validation: Check if path exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    pattern_prefix = input("Enter the new naming pattern (e.g., 'document'): ").strip()
    
    try:
        files = os.listdir(folder_path)
        count = 1
        
        for filename in files:
            # Construct full file paths
            old_file_path = os.path.join(folder_path, filename)
            
            # Skip directories, only rename files
            if os.path.isfile(old_file_path):
                file_extension = os.path.splitext(filename)[1]
                new_filename = f"{pattern_prefix}_{count}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)
                
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
                count += 1
                
        print("\nSuccess: All files renamed successfully!")
        
    except PermissionError:
        print("Error: Permission denied. Try running as administrator.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    rename_files()