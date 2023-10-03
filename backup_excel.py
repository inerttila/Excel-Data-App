import shutil
import os
import time

# Source path (path to the original Excel file)
source_path = "C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx"


# Destination path (path to the backup folder)
backup_folder = "C:\\Users\\User\\Desktop\\excel-data\\BackupFolder"

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Define a function to create a backup copy


def create_backup():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.xlsx"
    backup_path = os.path.join(backup_folder, backup_filename)
    shutil.copyfile(source_path, backup_path)


# Schedule the backup to run at a specific interval (e.g., every day)
while True:
    create_backup()
    # Adjust the sleep duration (e.g., 86400 seconds for daily backup)
    time.sleep(86400)
