import os
import http.server
import socketserver
import qrcode


def generate_qr_code_and_start_server(file_path, filename):
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

    print(f"Serving at http://localhost:{PORT}")
    print(f"Scan the QR code to download the Excel file on your phone.")

    # Generate QR code with the local server URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"http://192.168.40.14:{PORT}/Timesheet-managementt.xlsx")
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image in the "qr_code_photo" directory
    img.save(filename)

    httpd.serve_forever()


excel_file_path = 'C:\\Users\\User\\Desktop\\Excel-Data-App\\Timesheet-managementt.xlsx'
generate_qr_code_and_start_server(excel_file_path, "local_qrcode.png")
