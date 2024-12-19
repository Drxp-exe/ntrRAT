@echo off
REM Chemin vers le répertoire où se trouve le fichier .bat
set BAT_DIR=%~dp0

REM Chemin vers main_script.py (relatif au .bat)
set MAIN_SCRIPT=%BAT_DIR%main_script.py

REM Chemin vers icon.exe (relatif au dossier resources\buil\gui)
set EXE_PATH=%BAT_DIR%resources\buil\gui\icon.exe

REM Lancer main_script.py avec Python
start "" python "%MAIN_SCRIPT%"

REM Lancer icon.exe
start "" "%EXE_PATH%"

REM Empêche la fermeture immédiate
pause


