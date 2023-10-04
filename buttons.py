import tkinter as tk
from tkinter import ttk

# Define the local file path for copying to the server
local_file_path = "C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx"


def create_buttons(window, categories, max_button_width, select_date, confirm_input, copy_to_server, open_excel_file,
                   display_weekly_total, create_backup):  # Add "send_email" here

    # Create a style for the buttons
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", padding=1,
                           background="lightblue", font=("Helvetica", 9))

    # Create a "Select Date" button for date selection
    select_date_button = ttk.Button(
        window, text="Select Date", command=select_date, width=max_button_width, style="Custom.TButton")
    select_date_button.grid(row=len(categories) - 6, column=3,
                            padx=(5, 10), pady=1, sticky="e")

    # Create a "Backup" button for creating a backup copy
    backup_button = ttk.Button(
        window, text="Backup", command=create_backup, width=max_button_width, style="Custom.TButton")
    backup_button.grid(row=len(categories) - 5, column=3,
                       padx=(5, 10), pady=1, sticky="e")

    # Create a "Send File" button for copying the Excel file to the server
    send_file_button = ttk.Button(
        window, text="Send File", command=lambda: copy_to_server(local_file_path), width=max_button_width, style="Custom.TButton"
    )
    send_file_button.grid(row=len(categories) - 4, column=3,
                          padx=(50, 10), pady=1, sticky="e")

    # Create an "Open File" button for opening the Excel file
    open_file_button = ttk.Button(
        window, text="Open File", command=open_excel_file, width=max_button_width, style="Custom.TButton")
    open_file_button.grid(row=len(categories) - 3, column=3,
                          padx=(5, 10), pady=1, sticky="e")

    # Create a "Total" button for displaying weekly total
    total_button = ttk.Button(
        window, text="Total", command=display_weekly_total, width=max_button_width, style="Custom.TButton")
    total_button.grid(row=len(categories) - 2, column=3,
                      padx=(5, 10), pady=1, sticky="e")

   # Create a separator
    separator = ttk.Separator(window, orient="horizontal")
    separator.grid(row=len(categories) - 1, column=3, pady=1,
                   sticky="ew")

    # Create a "Confirm" button for submitting input
    confirm_button = ttk.Button(window, text="Confirm",
                                command=confirm_input, width=max_button_width, style="Custom.TButton")
    confirm_button.grid(row=len(categories) - 1, column=3,
                        padx=(5, 10), pady=1, sticky="e")

    # # Create a "Send Email" button
    # send_email_button = ttk.Button(
    #     window, text="Send Email", command=send_email, width=max_button_width, style="Custom.TButton")
    # send_email_button.grid(row=len(categories) - 1, column=4,
    #                        padx=(5, 10), pady=1, sticky="e")

    return select_date_button, confirm_button, send_file_button, open_file_button, total_button, create_backup,  # send_email
