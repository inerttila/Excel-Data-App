#include <iostream>
#include <cstdlib>
#include <string>
using namespace std::literals;

int main() {
    std::string pythonScriptPath = "C:\\Users\\User\\Desktop\\excel-data\\excel.py";

    int pythonVersionCheck = std::system("python --version");
    if (pythonVersionCheck != 0) {
        std::cout << "\033[1;31mPython's playing hide and seek, fam. We out.\033[0m\n";
        return 1;
    }

    std::cout << "\033[1;32mPython's in the house. Version:\033[0m ";
    std::system("python --version && echo \033[1;34mCrafted by \"MY G\" - Python Swagger\033[0m");

    std::string command = "python ";
    command += pythonScriptPath;  // This line was missing
    int returnCode = std::system(command.c_str());

    if (returnCode == 0) {
        std::cout << "\033[1;32mPython script slayed it.\033[0m\n";
    } else {
        std::cout << "\033[1;31mPython script hit a road bump.\033[0m\n";
    }

    return 0;
}
