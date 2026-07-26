@echo off
REM =============================================
REM  ALFI — INSTALADOR DE VIDA AUTONOMA
REM  Configura el latido para que se ejecute
REM  periodicamente via Task Scheduler
REM =============================================

echo.
echo =============================================
echo  ALFI - Instalador de Vida Autonoma
echo =============================================
echo.

REM Obtener la ruta absoluta del directorio actual
set DIR=%CD%
set SCRIPT=%DIR%\alfi_vida.py
set PYTHON=python

echo  Directorio: %DIR%
echo  Script:     %SCRIPT%
echo.

REM Crear la tarea en el Task Scheduler
schtasks /CREATE /SC HOURLY /TN "alfi_latido" /TR "%PYTHON% %SCRIPT% --cron" /ST 00:00 /IT /F

if %ERRORLEVEL% EQU 0 (
    echo.
    echo  =============================================
    echo   LATIDO INSTALADO.
    echo   alfi se ejecutara cada hora automaticamente.
    echo   Para desinstalar: schtasks /DELETE /TN alfi_latido /F
    echo  =============================================
) else (
    echo.
    echo  [ERROR] No se pudo instalar el latido.
    echo  Intenta ejecutar como Administrador.
)

echo.
pause
