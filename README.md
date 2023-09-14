# Timesheet Management Application

A Python and C++-based timesheet management application for tracking work hours and tasks. This application provides an easy-to-use interface for users to input their work-related data, which is then stored and managed in an Excel workbook.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Compiling the C++ Part (main.cpp)](#compiling-the-c-part-maincpp)
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

Additionally, here are some important details about the application:

##### Weekly Sheet

Every week, the weekly sheet is cleared, allowing you to start fresh for the new week's work entries. This ensures that your data is neatly organized by week, making it easier to track your work hours.

##### Yearly Sheet

The yearly sheet is designed to print an empty line at the beginning of each week, making it easy to separate data by week. This feature enhances the readability and organization of your work records over time.

##### Customizable Pop-Up Window Style

The application provides control over the style of pop-up windows using Python, allowing you to tailor the user interface to your preferences. You can modify the appearance and behavior of pop-up windows to match your desired style and user experience.

Feel free to customize the Excel file style, including fonts, colors, and more, to suit your specific needs and preferences. This level of control ensures that your work records are not only accurate but also visually appealing and organized.

##### Calculating Weekly Total Hours

The Timesheet Management Application includes a feature that automatically calculates your weekly total hours. When you input your work hours for various tasks and days, the application sums up these hours to provide you with a convenient weekly total. This calculation ensures you have an accurate overview of your work hours, making it easy to track your progress and manage your time effectively.

## Requirements

To run this application, you need the following:

- Python 3.x (Check your Python version using `python --version`)
- C++ build environment and compatible compiler (for the C++ part)
- Required Python packages (specified in `requirements.txt`)

## Installation

Clone the repository to your local machine:

```bash
  git clone https://github.com/inerttila/excel-data.git

  cd excel-data
```

Install the required Python packages by running the following command in the project's root directory:

```bash
  pip install -r requirements.txt
```

### Customizing the File Path

You can customize the file path where the Excel file is saved based on your preferences. To do this, follow these steps:

1. Locate the following line of code in the Python script (`excel.py`):

```python
  file_path = 'C:\\Users\\User\\Desktop\\excel-data\\Timesheet-managementt.xlsx'
```

## Usage with Compiling the C++ Part (main.cpp)

To compile the C++ part of the application, follow these steps:

1. Open your command prompt or terminal.
2. Navigate to the project's root directory.
3. Use the `g++` command to compile the `main.cpp` file and create an executable named `timesheet_app`. Run the following command:

```bash
  g++ main.cpp -o timesheet_app
```

When you use the Timesheet Management Application and click the "Confirm" button, your work-related data will be saved in an Excel file. This Excel file acts as your digital timesheet, storing all the information you input.

By default, the Excel file will be automatically created and saved in the `excel-data` folder within the project directory. You can easily access and manage your work records in this Excel file for record-keeping and analysis.

## Usage

Create and activate a virtual environment:
On Windows:

```bash
  python -m venv venv

  venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv venv

source venv/bin/activate
```

Install the required Python packages by running the following command :

```bash
  pip install -r requirements.txt
```

Ensure you have Python installed on your system. If not, install or update it from the Python official website.

Execute the Python script to run the application:

```bash
  python excel.py
```

When you use the Timesheet Management Application and click the "Confirm" button, your work-related data will be saved in an Excel file. By default, the Excel file will be saved in the `excel-data` folder within the project directory.

## Contact

For inquiries or assistance, feel free to reach out through the following channels:

- Email: [inert.etila@gmail.com](mailto:inert.etila@gmail.com)
- LinkedIn: [Inert Tila](https://al.linkedin.com/in/inerttila)

You can email me for any questions or support related to this project, and you can also connect with me on LinkedIn to stay updated on my professional activities.
