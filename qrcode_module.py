import os
import http.server
import socketserver
import qrcode
from tkinter import messagebox
import socket  # To dynamically get the local IP address


# Define the file name and path
excel_file_name = "Timesheet-managementt.xlsx"
base_dir = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(base_dir, excel_file_name)


def get_local_ip():
    """Get the local IP address of the machine."""
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def generate_qr_code_and_start_server(file_path):
    """Generate a QR code for downloading the file and start an HTTP server."""
    try:
        # Ensure the file exists
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File not found: {file_path}")
            return

        # Set the server's base directory
        excel_directory = os.path.dirname(file_path)
        os.chdir(excel_directory)

        # Specify the port to run the server on
        PORT = 8000

        # Start the server
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)

        # Get the local IP address dynamically
        local_ip = get_local_ip()
        qr_data = f"http://{local_ip}:{PORT}/{excel_file_name}"

        # Generate the QR code
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

        # Save the QR code image
        qr_image_path = os.path.join(excel_directory, "local_qrcode.png")
        img.save(qr_image_path)

        # Show success message with instructions
        messagebox.showinfo(
            "Success",
            f"Scan the QR code to download the Excel file.\nQR Code saved at: {qr_image_path}"
        )

        # Serve the HTTP server
        print(f"Serving on {local_ip}:{PORT}")
        httpd.serve_forever()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def generate_qr_code_and_start_server_wrapper():
    """Wrapper function for generating QR code and starting the server."""
    generate_qr_code_and_start_server(local_file_path)
