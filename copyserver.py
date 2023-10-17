import os
import shutil
import tkinter.messagebox as messagebox

# Define file paths as constants
base_dir = os.path.dirname(os.path.abspath(__file__))
excel_file_name = "Timesheet-managementt.xlsx"
local_file_path = os.path.join(base_dir, excel_file_name)
server_file_path = r"\\192.168.40.21\Fileshare SV1\Timesheet-managementt.xlsx"


def copy_to_server(local_file_path):
    try:
        shutil.copy(local_file_path, server_file_path)
        messagebox.showinfo(
            "Success", "Excel file copied to the server successfully.")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"Source file not found: {e}")
    except PermissionError as e:
        messagebox.showerror("Error", f"Permission denied: {e}")
    except OSError as e:
        messagebox.showerror("Error", f"File operation error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    copy_to_server(local_file_path)
