@echo off
setlocal
set "scriptPath=C:\Users\Truss10 User\Documents\Projects\PDFMerger\merge.py"
set "pythonExe="C:\Program Files\Python311\python.exe""  

%pythonExe% "%scriptPath%" "%~1"

