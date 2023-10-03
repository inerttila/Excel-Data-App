#include <iostream>
#include <string>
#include <windows.h>

int main() {
    // Path to your Python script
    const std::string PYTHON_SCRIPT_PATH = "C:\\Users\\User\\Desktop\\excel-data\\excel.pyw";

    // Construct the full command with the script path
    std::string command = "python " + PYTHON_SCRIPT_PATH;

    int pythonVersionCheck = std::system("python --version");
    if (pythonVersionCheck != 0) {
        std::cout << "\033[1;31mPython's playing hide and seek, fam. We out.\033[0m\n";
        return 1;
    }

    std::cout << "\033[1;32mPython's in the house. Version:\033[0m ";
    std::system("python --version && echo \033[1;34mCrafted by \"TOP G\" - Python Swagger\033[0m");

    ///----------------------------------------------------------------------------------
    // Note for Clients:
    // If you want to run the Python script without the command prompt window appearing in the background,
    // use this modified code below. It hides the console window when executing the Python script.
    // You can find the code marked with "ADDED FOR HIDING CONSOLE WINDOW" below.

    // Create a STARTUPINFO structure to specify that the process should be created hidden
    STARTUPINFO si = { sizeof(STARTUPINFO) }; // Using designated initializer
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE;

    PROCESS_INFORMATION pi = {}; // Using default initialization

    // Use DETACHED_PROCESS flag to hide the console window
    int returnCode = CreateProcess(NULL, const_cast<char*>(command.c_str()), NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi);

    ///-------------------------------------------------------------------------------------------

    if (returnCode != 0) {
        std::cout << "\033[1;32mPython script slayed it.\033[0m\n";
    } else {
        std::cout << "\033[1;31mPython script hit a road bump.\033[0m\n";
    }

    return 0;
}
