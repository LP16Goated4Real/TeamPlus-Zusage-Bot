@echo off
SETLOCAL

SET PROJECT_DIR=%~dp0
CD /D "%PROJECT_DIR%"

SET LOG_FILE=%PROJECT_DIR%Log\bot.log

IF NOT EXIST "%LOG_FILE%" (
  echo ===================== > "%LOG_FILE%"
  echo Log Datei wurde erstellt! >> "%LOG_FILE%"
  echo ===================== >> "%LOG_FILE%"
)

python --version >nul 2>&1
if ERRORLEVEL 1 (
  echo Python ist nicht installiert oder nicht im PATH! >> "%LOG_FILE%"
  echo Bitte Python installieren: https://www.python.org/downloads/ >> "%LOG_FILE%"
  pause
  exit /b 1
)

SET VENV_DIR=%PROJECT_DIR%.venv

IF NOT EXIST "%VENV_DIR%\Scripts\python.exe" (
  echo Erstelle virtuelle Umgebung... >> "%LOG_FILE%"
  python -m venv "%VENV_DIR%"
  echo Upgrade pip... >> "%LOG_FILE%"
  "%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
)

CALL "%VENV_DIR%\Scripts\activate.bat"

IF EXIST "requirements.txt" (
  echo Installiere/aktualisiere Pakete aus requirements.txt... >> "%LOG_FILE%"
  "%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade -r requirements.txt
)

echo Starte zusage_bot.py >> "%LOG_FILE%"
python "%PROJECT_DIR%src\zusage_bot.py"

ENDLOCAL