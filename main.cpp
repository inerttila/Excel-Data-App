#include <windows.h>
#include <string>  // Include the string header

int main() {
    const std::string PYTHON_SCRIPT_PATH = "C:\\Users\\User\\Desktop\\Excel-Data-App\\excel.pyw";

    std::string command = "python " + PYTHON_SCRIPT_PATH;

    STARTUPINFO si = { sizeof(STARTUPINFO) };
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE;

    PROCESS_INFORMATION pi = {};

    int returnCode = CreateProcess(NULL, const_cast<char*>(command.c_str()), NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi);

    // Wait for the Python process to finish
    WaitForSingleObject(pi.hProcess, INFINITE);

    // Close process and thread handles
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return 0;
}
