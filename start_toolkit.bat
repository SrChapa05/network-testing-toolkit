@echo off
TITLE Network Testing Toolkit - Control Panel
COLOR 0A

echo ========================================================
echo       NETWORK TESTING TOOLKIT - LAUNCHER GENERAL
echo ========================================================
echo.

:: 1. Iniciar el Backend de FastAPI
echo [*] Iniciando el Backend (FastAPI)...
cd /d "%~dp0"
start "Backend - FastAPI" cmd /k "call .venv\\Scripts\\activate && uvicorn main:app --reload --port 8000"

:: Esperar un par de segundos para asegurar que el backend levante
timeout /t 3 /nobreak > nul

:: 2. Iniciar el Frontend de React (Vite)
echo [*] Iniciando el Frontend (React / Vite)...
cd /d "%~dp0frontend"
start "Frontend - React" cmd /k "npm run dev"

echo.
echo ========================================================
echo  [+] ¡Servicios desplegados correctamente!
echo  - Backend API: http://127.0.0.1:8000
echo  - Documentacion Swagger: http://127.0.0.1:8000/docs
echo  - Interfaz Frontend: http://localhost:5173
echo ========================================================
echo.
pause