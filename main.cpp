#include <iostream>
#include <cstdlib>

int main() {
    // Replace the path below with the correct path to your Python script
    std::string pythonScriptPath = "C:\\Users\\User\\Desktop\\excel-data\\excel.py";

    // Check if Python is available and print version
    int pythonVersionCheck = std::system("python --version");
    if (pythonVersionCheck != 0) {
        std::cout << "Python is not installed or accessible. Aborting." << std::endl;
        return 1;
    }

    // Print "made by Inert" along with Python version
    std::cout << "Python is installed. Version: ";
    std::system("python --version && echo made by Inert");

    // Build and execute the shell command to run the Python script
    std::string command = "python ";
    command += pythonScriptPath;

    int returnCode = std::system(command.c_str());

    if (returnCode == 0) {
        std::cout << "Python script executed successfully." << std::endl;
    } else {
        std::cout << "Error executing Python script." << std::endl;
    }

    return 0;
}
