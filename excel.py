import os
import openpyxl
from tkinter import Tk, simpledialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Button
from openpyxl.styles import Font, PatternFill


# Set the file path and name
file_path = 'C:/path/to/your_file.xlsx'

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Load the workbook or create a new one if it doesn't exist
try:
    workbook = openpyxl.load_workbook(file_path)
except FileNotFoundError:
    workbook = openpyxl.Workbook()

# Select the worksheet (replace 'Sheet1' with the actual sheet name)
worksheet = workbook['Sheet']

# Define the category labels
categories = ['Date', 'Service Line', 'Type Of Service',
              'Company', 'Task', 'Hours', 'Notes']


# Apply font and fill styles to the header row
header_font = Font(bold=True, color="ffffff")  # Bold font with white color
header_fill = PatternFill(start_color="061c43", end_color="061c43",
                          fill_type="solid")  # Black background color

# Add category labels and apply styles to the header row
for col_num, category in enumerate(categories, start=1):
    cell = worksheet.cell(row=1, column=col_num, value=category)
    cell.font = header_font
    cell.fill = header_fill

# Define the predefined company options
company_options = ['Skaitech', '3DSkai']

# Function to handle company selection


def select_company():
    # Create the top-level window for company selection
    top = Tk()
    top.title("Select a Company")

    var = StringVar(top)
    combobox = Combobox(top, textvariable=var,
                        values=company_options, state="readonly")
    combobox.current(0)  # Set the default option
    combobox.pack()

    def confirm_selection():
        value = var.get()
        top.destroy()
        data.append(value)  # Append the selected value to the data list

    confirm_button = Button(top, text="Confirm", command=confirm_selection)
    confirm_button.pack()

    # Use wait_window on the top-level window
    top.wait_window(top)


# Prompt user for data using pop-up dialog
data = []
for category in categories:
    if category == 'Company':
        select_company()
    else:
        value = simpledialog.askstring("Data Input", f"Enter {category}:")
        data.append(value)

# Add category labels
for col_num, category in enumerate(categories, start=1):
    cell = worksheet.cell(row=1, column=col_num, value=category)

# Add user-provided data to the table
worksheet.append(data)

# Save the changes
workbook.save(file_path)
