#include <iostream>
#include <cstdlib>

int main() {
    // Replace the path below with the correct path to your Python script
    const char* pythonScriptPath = "/Users/skaitech/Desktop/excel-data/excel.py";

    // Build and execute the shell command to run the Python script
    std::string command = "python3 ";
    command += pythonScriptPath;

    int returnCode = std::system(command.c_str());

    if (returnCode == 0) {
        std::cout << "Python script executed successfully." << std::endl;
    } else {
        std::cout << "Error executing Python script." << std::endl;
    }

    return 0;
}
