[Setup]
AppName=PDF Merger
AppVersion=1.0
DefaultDirName={pf}\PDFMerger
DefaultGroupName=PDF Merger
OutputDir=/
OutputBaseFilename=Setup
SetupIconFile=merge.ico
Compression=lzma2/ultra64
SolidCompression=yes

[Files]
Source: "build/exe.win-amd64-3.11\*"; DestDir: "{app}"; Flags: recursesubdirs

[Registry]
Root: HKCR; Subkey: "Directory\shell\MergePDFs"; ValueType: string; ValueName: ""; ValueData: "Merge PDFs"
Root: HKCR; Subkey: "Directory\shell\MergePDFs\command"; ValueType: string; ValueName: ""; ValueData: """{app}\merge.exe"" ""%1"" ""output_filename.pdf"""

[Icons]
Name: "{group}\Merge PDFs"; Filename: "{app}\merge.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\merge.exe"; Parameters: "%1"; Description: "Merge PDFs"; Flags: runhidden
