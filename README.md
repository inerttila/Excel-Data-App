# Timesheet Management Application 
![Screenshot 2023-10-30 175452](https://github.com/inerttila/Excel-Data-App/assets/137422939/76cea38a-78b2-4b13-baa0-90e170f2232d)


A Python and C++-based timesheet management application for tracking work hours and tasks. This application provides an easy-to-use interface for users to input their work-related data, which is then stored and managed in an Excel workbook.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)![Uploading Screenshot 2023-10-30 175452.png…]()

- [Installation](#installation)
- [Compiling the C++ Part (main.cpp)](#compiling-the-c-part-maincpp)
- [Usage](#usage)
- [Email Sender using Python and Gmail API](#Email-Sender-using-Python-and-Gmail-API)
- [Contact](#contact)

## Introduction

The Timesheet Management Application streamlines the recording and management of work-related data with efficiency and user-friendliness. It offers the following features:
- Input work details: date, service line, type of service, company, task, hours worked, and notes.
- Option menus for selecting categories.
- A date picker for easy date selection.
- Validation checks for hours input.
- Organized user interface.
- Data saved in Excel for record-keeping and analysis.

Additional Features:
- Weekly Sheet: Starts fresh each week for organized tracking.
- Yearly Sheet: Separates data by week for readability.
- Customizable Pop-Up Window Style: Tailor the user interface.
- Calculate Weekly Total Hours: Easily track your work hours.
- Send Files: Share Timesheet data for other user.
- Open Excel Files: Access Timesheet Data.
- Excel Backup Automator: Automated file backups.
- Email Excel Files: Secure data sharing via Gmail API.
- Dockerfile for Python app with GUI.

This concise introduction provides an overview of the Timesheet Management Application's key features and additional functionalities.

## Requirements

To run this application, you need the following:

- Python 3.x (Check your Python version using `python --version`)
- C++ build environment and compatible compiler (for the C++ part)

## Installation

Clone the repository to your local machine:

```bash
  git clone https://github.com/inerttila/Excel-Data-App.git
```

```bash
  cd Excel-Data-App
```

Install the required Python packages by running the following command in the project's root directory:

```bash
  pip install -r requirements.txt
```

### Customizing the File Path

You can customize the file path where the Excel file is saved based on your preferences. To do this, follow these steps:

1. Locate the following line of code in the Python script :

```python
  file_path = 'C:\\Users\\User\\Desktop\\Excel-Data-App\\Timesheet-managementt.xlsx'
```

## Usage with Compiling the C++ Part (main.cpp)

To compile the C++ part of the application, follow these steps:

1. Open your terminal and navigate to the project's root directory
2. Use the `g++` command to compile the `main.cpp` file and create an executable named `yourapp_name`. Run the following command:

```bash
  g++ main.cpp -o yourapp_name
```

When you use the Timesheet Management Application and click the "Confirm" button, your work-related data will be saved in an Excel file. This Excel file acts as your digital timesheet, storing all the information you input.

By default, the Excel file will be automatically created and saved in the `Excel-Data-App` folder within the project directory. You can easily access and manage your work records in this Excel file for record-keeping and analysis.

## Usage

Create and activate a virtual environment:

```bash
  python -m venv venv
```

```bash
  venv\Scripts\activate
```

Install the required Python packages by running the following command :

```bash
  pip install -r requirements.txt
```

Execute the Python script to run the application:

```bash
  python excel.pyw
```

## Email Sender using Python and Gmail API

This project demonstrates how to send emails with attachments using Python and Gmail. It provides an example of sending emails with Excel file attachments using the Gmail API and OAuth2 authentication.

### Prerequisites

Before using this code, ensure you have the following prerequisites in place:

```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Contact

For inquiries or assistance, feel free to reach out through the following channels:

- Email: [inert.etila@gmail.com](mailto:inert.etila@gmail.com)
- LinkedIn: [Inert Tila](https://al.linkedin.com/in/inerttila)

You can email me for any questions or support related to this project, and you can also connect with me on LinkedIn to stay updated on my professional activities.
