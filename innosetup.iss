[Setup]
AppName=Excel Data App
AppVersion=1.0
DefaultDirName=C:\Users\User\Desktop\Excel-Data-App
DefaultGroupName=Excel Data App
OutputDir=Output
OutputBaseFilename=ExcelDataAppInstaller

[Files]
Source: "C:\Users\User\Desktop\Excel-Data-App\*"; DestDir: {app}; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{commondesktop}\Excel App"; Filename: "{app}\excel.exe"; WorkingDir: {app}; IconFilename: "C:\Users\User\Desktop\Excel-Data-App\Media\otr.ico"

[Code]
function InitializeSetup: Boolean;
begin
  Result := True;
end;
