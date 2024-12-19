@echo off
set SCRIPT_DIR=%~dp0
set PYTHON_PATH=%SCRIPT_DIR%main.pyw

rem Simulate an installation message with a loading animation
echo Installation in progress... please wait...

rem Loop for a loading animation (dots)
for /l %%i in (1,1,3) do (
    echo. . . 
    timeout /t 1 >nul
)

if exist "%PYTHON_PATH%" (
    rem Simulate execution message
    echo Executing main.py...
    rem Loop for a loading animation during execution
    for /l %%i in (1,1,3) do (
        echo. . . 
        timeout /t 1 >nul
    )
    pythonw "%PYTHON_PATH%"
) else (
    rem If the file is not found, simulate an error message
    echo Error: main.py not found.
    timeout /t 2 >nul
)

rem End of the execution, simulating installation completion with a message to start another script
echo Installation completed. Please start 'main_script.py'. Press any key to exit.
pause >nul




