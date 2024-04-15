import os
import http.server
import socketserver
import qrcode
from tkinter import messagebox  # Import the messagebox module

# Define the file name
excel_file_name = "Timesheet-managementt.xlsx"
relative_file_path = "Excel-Data-App/" + excel_file_name
base_dir = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(base_dir, relative_file_path)


def generate_qr_code_and_start_server(file_path):
    excel_directory = os.path.dirname(file_path)
    qr_code_directory = os.path.join(excel_directory,)

    # Create the "qr_code_photo" directory if it doesn't exist
    os.makedirs(qr_code_directory, exist_ok=True)

    os.chdir(excel_directory)  # Set the server's base directory

    # Specify the port to run the server on
    PORT = 8000

    # Start the server
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)

    # Show a success message
    messagebox.showinfo(
        "Success", "Scan the QR code to download the Excel file.")

    # Generate QR code with the local server URL
    qr_data = f"http://192.168.40.14:{PORT}/Timesheet-managementt.xlsx"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image in the "qr_code_photo" directory
    img.save("local_qrcode.png")

    httpd.serve_forever()


def generate_qr_code_and_start_server_wrapper():
    generate_qr_code_and_start_server(local_file_path)
