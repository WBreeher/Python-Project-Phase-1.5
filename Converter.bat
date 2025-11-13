@echo off   
setlocal    
cd /d "%~dp0"   

REM Use the Python launcher if available, else python.exe   
where py >nul 2>nul && set "PY=py" || set "PY=python" 

"%PY%" "TempConvert.py" 
echo. 
pause 