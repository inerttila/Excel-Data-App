import tkinter as tk

# Define the local file path for copying to the server
local_file_path = "C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx"


def create_buttons(window, categories, max_button_width, select_date, confirm_input, copy_to_server, open_excel_file, display_weekly_total, create_backup, send_email):
    # Create a "Select Date" button for date selection
    select_date_button = tk.Button(
        window, text="Select Date", command=select_date, width=max_button_width, pady=1)
    select_date_button.grid(row=len(categories) - 6, column=3,
                            padx=(5, 10), pady=1, sticky="e")

    # Create a "Confirm" button for submitting input with the same style as "Send File" button
    confirm_button = tk.Button(window, text="Confirm",
                               command=confirm_input, width=max_button_width)
    confirm_button.grid(row=len(categories) - 5, column=3,
                        padx=(5, 10), pady=1, sticky="e")

    # Create a "Send File" button for copying the Excel file to the server with the same style
    send_file_button = tk.Button(
        window, text="Send File", command=lambda: copy_to_server(local_file_path), width=max_button_width, pady=1
    )
    send_file_button.grid(row=len(categories) - 4, column=3,
                          padx=(50, 10), pady=1, sticky="e")

    # Create an "Open File" button for opening the Excel file with the same style as "Confirm" button
    open_file_button = tk.Button(
        window, text="Open File", command=open_excel_file, width=max_button_width, pady=1)
    open_file_button.grid(row=len(categories) - 3, column=3,
                          padx=(5, 10), pady=1, sticky="e")

    # Create a "Total" button for displaying weekly total with the same style as other buttons
    total_button = tk.Button(
        window, text="Total", command=display_weekly_total, width=max_button_width, pady=1)
    total_button.grid(row=len(categories) - 2, column=3,
                      padx=(5, 10), pady=1, sticky="e")

    # Create a "Backup" button for creating a backup copy with the same style as other buttons
    backup_button = tk.Button(
        window, text="Backup", command=create_backup, width=max_button_width, pady=1)
    backup_button.grid(row=len(categories) - 1, column=3,
                       padx=(5, 10), pady=1, sticky="e")

    # Create a "Send Email" button
    send_email_button = tk.Button(
        window, text="Send Email", command=send_email, width=max_button_width, pady=1)
    send_email_button.grid(row=len(categories) - 1, column=4,
                           padx=(5, 10), pady=1, sticky="e")

    return select_date_button, confirm_button, send_file_button, open_file_button, total_button, create_backup, send_email
