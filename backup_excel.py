import shutil
import os
import time
import tkinter.messagebox as messagebox


def create_backup():
    # Source path (path to the original Excel file)
    source_path = "C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx"

    # Destination path (path to the backup folder)
    backup_folder = "C:\\Users\\User\\Desktop\\excel-data\\BackupFolder"

    # Create the backup folder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Create a timestamp for the backup filename
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.xlsx"
    backup_path = os.path.join(backup_folder, backup_filename)

    # Create the backup copy
    shutil.copyfile(source_path, backup_path)

    # Display a message box to show completion message
    messagebox.showinfo("Backup", "Backup completed successfully!")
