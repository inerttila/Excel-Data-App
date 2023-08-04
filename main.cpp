#include <iostream>
#include <cstdlib>

int main() {
    // Replace the path below with the correct path to your Python script
    std::string pythonScriptPath = "C:\\Users\\User\\Desktop\\excel-data\\excel.py";

    // Check if Python is available and print version
    int pythonVersionCheck = std::system("python --version");
    if (pythonVersionCheck != 0) {
        std::cout << "\033[1;31mPython is not installed or accessible. Aborting.\033[0m" << std::endl;
        return 1;
    }

    // Print "made by Inert" along with Python version
    std::cout << "\033[1;32mPython is installed. Version:\033[0m ";
    std::system("python --version && echo \033[1;34mMade by Inert - Using Python\033[0m");

    // Build and execute the shell command to run the Python script
    std::string command = "python ";
    command += pythonScriptPath;

    int returnCode = std::system(command.c_str());

    if (returnCode == 0) {
        std::cout << "\033[1;32mPython script executed successfully.\033[0m" << std::endl;
    } else {
        std::cout << "\033[1;31mError executing Python script.\033[0m" << std::endl;
    }

    return 0;
}
