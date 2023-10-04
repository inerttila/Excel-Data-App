# import smtplib
# import base64
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from google.oauth2 import service_account
# import googleapiclient.discovery


# def send_email():
#     # Load OAuth2 credentials from JSON file
#     credentials = service_account.Credentials.from_service_account_file(
#         'path/to/your/service_account_key.json',
#         scopes=['https://www.googleapis.com/auth/gmail.send']
#     )

#     # Create a Gmail API client
#     gmail_service = googleapiclient.discovery.build(
#         'gmail', 'v1', credentials=credentials)

#     # Email configuration
#     sender_email = '123@gmail.com'
#     recipient_email = '123@gmail.com'
#     subject = 'Excel File Attachment'

#     # Create a multipart message
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = recipient_email
#     message['Subject'] = subject

#     # Email body
#     body = "Please find the attached Excel file."
#     message.attach(MIMEText(body, 'plain'))

#     # Attach the Excel file
#     file_path = 'C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx'
#     attachment = open(file_path, 'rb')
#     excel_part = MIMEBase('application', 'octet-stream')
#     excel_part.set_payload((attachment).read())
#     encoders.encode_base64(excel_part)
#     excel_part.add_header('Content-Disposition',
#                           "attachment; filename=Timesheet-managementt.xlsx")
#     message.attach(excel_part)

#     # Send the email using the Gmail API
#     try:
#         message = (gmail_service.users().messages().send(userId='me', body={
#                    'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')}).execute())
#         print("Email sent successfully")
#     except Exception as e:
#         print("Error sending email:", str(e))


# # Call the send_email function to send the email
# send_email()
