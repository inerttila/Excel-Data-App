## Timesheet Management Application


A Python and C++-based timesheet management application for tracking work hours and tasks. This application provides an easy-to-use interface for users to input their work-related data, which is then stored and managed in an Excel workbook.

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Usage with Compiling the C++ Part](#usage-with-compiling-the-c-part)
- [Email Sender using Python and Gmail API](#Email-Sender-using-Python-and-Gmail-API)

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
- Inno Setup desktop app.
- QR code generator for excel file tranfer.

This concise introduction provides an overview of the Timesheet Management Application's key features and additional functionalities.

## Installation

Clone the repository to your local machine:

```bash
  git clone https://github.com/inerttila/Excel-Data-App.git
  cd Excel-Data-App
```

## Usage

```bash
  pip install requirement.txt
```

## Usage with Compiling the C++ Part

To compile the C++ part of the application, follow these steps:

1. Open your terminal and navigate to the project's root directory
2. Use the `g++` command to compile the `main.cpp` file and create an executable named `yourapp_name`. Run the following command:

```bash
  g++ main.cpp -o yourapp_name
```

When you use the Timesheet Management Application and click the "Confirm" button, your work-related data will be saved in an Excel file. This Excel file acts as your digital timesheet, storing all the information you input.

By default, the Excel file will be automatically created and saved in the `Excel-Data-App` folder within the project directory. You can easily access and manage your work records in this Excel file for record-keeping and analysis.

## Email Sender using Python and Gmail API

This project demonstrates how to send emails with attachments using Python and Gmail. It provides an example of sending emails with Excel file attachments using the Gmail API and OAuth2 authentication.

### Prerequisites

Before using this code, ensure you have the following prerequisites in place:

```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
