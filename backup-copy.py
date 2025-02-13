import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, destination_dir):
    """
    Custom Backup Script
    - Ensures uniqueness of backed-up files
    - Provides detailed logs of actions performed
    """
    if not os.path.exists(source_dir):
        print(f"[ERROR] Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"[INFO] Destination directory '{destination_dir}' created.")

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        if os.path.isfile(source_path):
            if os.path.exists(destination_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_backup_{timestamp}{ext}"
                destination_path = os.path.join(destination_dir, new_filename)
                print(f"[WARNING] File '{filename}' already exists. Renaming to '{new_filename}'.")
            
            shutil.copy2(source_path, destination_path)
            print(f"[SUCCESS] Copied: {source_path} -> {destination_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[USAGE] python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    print("[START] Backup Process Initiated...")
    backup_files(source_directory, destination_directory)
    print("[END] Backup Process Completed.")
