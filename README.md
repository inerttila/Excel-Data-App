# Timesheet Management Application

A Python and C++-based timesheet management application for tracking work hours and tasks. This application provides an easy-to-use interface for users to input their work-related data, which is then stored and managed in an Excel workbook.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Introduction

The Timesheet Management Application simplifies the process of recording and managing work-related data, making it efficient and user-friendly. It offers the following key features:

- Input work details such as date, service line, type of service, company, task, hours worked, and notes.
- Option menus for selecting specific categories like service line, type of service, company, and task.
- A date picker for easy date selection.
- Validation checks for hours input.
- An organized and visually appealing user interface.
- Data is saved in an Excel workbook for record-keeping and analysis.

## Requirements

To run this application, you need the following:

- Python 3.x (Check your Python version using `python --version`)
- C++ build environment and compatible compiler (for the C++ part)
- Required Python packages (specified in `requirements.txt`)
  
```bash
pip install -r requirements.txt
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/inerttila/excel-data.git
```
```bash
cd excel-data
```
Ensure you have Python installed on your system. If not, install or update it from the Python official website.

Install the required Python packages by running the following command in the project's root directory:
```bash
pip install -r requirements.txt
```
Make sure you have the necessary C++ build environment and a compatible C++ compiler installed if you intend to use the C++ part of the project.

## Usage
Execute the Python script to run the application:
```bash
python excel.py
```
The application window will open, allowing you to input your work-related data.

Fill in the required information using the user interface, and click the "Confirm" button to save the data.

# Compiling the C++ Part (main.cpp)

To compile the C++ part of the application, follow these steps:

1. Open your command prompt or terminal.
2. Navigate to the project's root directory.
3. Use the `g++` command to compile the `main.cpp` file and create an executable named `timesheet_app`. Run the following command:

```bash
g++ main.cpp -o timesheet_app
```
## Contact

For inquiries or assistance, feel free to reach out through the following channels:

- Email: [inert.etila@gmail.com](mailto:inert.etila@gmail.com)
- LinkedIn: [Inert Tila](https://al.linkedin.com/in/inerttila)

You can email me for any questions or support related to this project, and you can also connect with me on LinkedIn to stay updated on my professional activities.
