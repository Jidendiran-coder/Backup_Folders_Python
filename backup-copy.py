'''
MIT License

Copyright (c) 2025 [Jidendiran]

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the Software), to deal 
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os        # 📂 Provides functions for interacting with the operating system (file paths, directories, etc.)
import sys       # 🖥️ Handles command-line arguments and system-specific functions
import shutil    # 📦 Used for file operations like copying while preserving metadata
from datetime import datetime  # ⏳ Provides date and time functions for timestamping backups

def backup_files(source_dir, destination_dir):
    """
    📌 Backs up files from the source directory to the destination directory.

    - Ensures the destination directory exists.
    - Copies files while maintaining uniqueness by renaming duplicates with timestamps.
    - Logs important actions such as errors, warnings, and successful copies.
    
    Parameters:
    source_dir (str): The directory containing files to be backed up.
    destination_dir (str): The directory where files will be copied.
    """

    # ✅ Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"❌ [ERROR] Source directory '{source_dir}' does not exist.")
        return

    # ✅ Create the destination directory if it does not exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"📁 [INFO] Destination directory '{destination_dir}' created.")

    # 🔄 Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # 📝 Check if the current item is a file (not a directory)
        if os.path.isfile(source_path):
            # ⚠️ If the file already exists in the destination, rename it with a timestamp
            if os.path.exists(destination_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_backup_{timestamp}{ext}"
                destination_path = os.path.join(destination_dir, new_filename)
                print(f"⚠️ [WARNING] File '{filename}' already exists. Renaming to '{new_filename}'.")

            # 📄 Copy the file while preserving metadata
            shutil.copy2(source_path, destination_path)
            print(f"✅ [SUCCESS] Copied: {source_path} -> {destination_path}")

if __name__ == "__main__":
    """
    🏁 Main execution block that handles command-line arguments.

    - Validates input arguments (source and destination directories).
    - Initiates the backup process if valid arguments are provided.
    """

    # 🚨 Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("⚠️ [USAGE] python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    print("🚀 [START] Backup Process Initiated...")
    backup_files(source_directory, destination_directory)
    print("🎉 [END] Backup Process Completed.")
