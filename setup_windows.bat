@echo off
title Jarvis - Quick Setup for Windows
color 0A

echo.
echo ===============================================================================
echo                      JARVIS - Windows Quick Setup
echo                     Getting Started in Under 5 Minutes
echo ===============================================================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please download Python 3.8+ from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [OK] Python found!
echo.

echo Running Jarvis setup...
python quick_setup.py

echo.
echo ===============================================================================
echo Setup complete! 
echo.
echo To start Jarvis, run:
echo    python Jarvismain.py
echo.
echo Say "Wake up" to activate your assistant!
echo ===============================================================================
pause
