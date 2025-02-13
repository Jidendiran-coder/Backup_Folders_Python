# 📂 Backup Script

## 📌 Project Description
A Python script that efficiently backs up files from a source directory to a destination directory. The script ensures unique backups by appending timestamps to duplicate filenames and provides detailed logs for better tracking.

## 📖 Table of Contents
1. [⚙️ Prerequisites](https://github.com/Jidendiran-coder/Backup_Folders_Python#%EF%B8%8F-prerequisites)
2. [📥 Installation Instructions](https://github.com/Jidendiran-coder/Backup_Folders_Python#-installation-instructions)
3. [📝 Usage Instructions](https://github.com/Jidendiran-coder/Backup_Folders_Python#-usage-instructions)
4. [🔧 Configuration](https://github.com/Jidendiran-coder/Backup_Folders_Python#-configuration)
5. [🚀 CI/CD Pipeline Details](https://github.com/Jidendiran-coder/Backup_Folders_Python#-cicd-pipeline-details)
6. [🔒 Security Best Practices](https://github.com/Jidendiran-coder/Backup_Folders_Python#-security-best-practices)
7. [🐞 Troubleshooting](https://github.com/Jidendiran-coder/Backup_Folders_Python#-troubleshooting)
8. [🤝 Contribution Guidelines](https://github.com/Jidendiran-coder/Backup_Folders_Python#-contribution-guidelines)
9. [📜 License](https://github.com/Jidendiran-coder/Backup_Folders_Python#-license)
10. [📸 Screenshots & Architecture Diagrams](https://github.com/Jidendiran-coder/Backup_Folders_Python#-screenshots--architecture-diagrams)
11. [📅 Changelog](https://github.com/Jidendiran-coder/Backup_Folders_Python#-changelog)

## ⚙️ Prerequisites
- 🐍 Python 3.x installed on your system
- 📦 Required modules (`os`, `sys`, `shutil`, `datetime`) are part of Python's standard library

## 📥 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/backup-script.git
   ```
2. Navigate to the project directory:
   ```bash
   cd backup-script
   ```

## 📝 Usage Instructions
1. Run the script with the following command:
   ```bash
   python backup.py <source_directory> <destination_directory>
   ```
2. The script will copy all files from `source_directory` to `destination_directory`.
3. For your testing purpose we have provided "Test_Source_Folder" & "Test_Destination_Folder" in current path.
4. If a file already exists in the destination, it will be renamed with a timestamp.

## 🔧 Configuration
- Modify the script to change naming conventions, logging format, or add exclusions.

## 🚀 CI/CD Pipeline Details
- Can be integrated into a CI/CD pipeline to automate backup operations before deployments.

## 🔒 Security Best Practices
- Ensure only trusted users have access to the backup script.
- Store backup logs in a secure location.

## 🐞 Troubleshooting
- If the script fails, ensure source and destination directories exist and have proper permissions.
- Run the script with administrator privileges if permission errors occur.

## 🤝 Contribution Guidelines
- Fork the repository and submit a pull request with improvements.

## 📜 License
This project is licensed under the MIT License.

## 📸 Output Screenshot
![image](https://github.com/user-attachments/assets/5c94fa4c-c020-4f11-95ef-9603896f0d30)

## 📅 Changelog
- **v1.0** - Initial release with basic file backup functionality.

