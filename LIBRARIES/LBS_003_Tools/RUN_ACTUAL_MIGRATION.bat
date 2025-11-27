@echo off
echo ================================================================================
echo TOOL MIGRATION - ACTUAL EXECUTION
echo ================================================================================
echo.
echo WARNING: This will modify your tool files!
echo.
echo Make sure you have reviewed the dry run results first.
echo.
pause

REM Try different Python commands
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: python
    python migrate_tools_to_tol.py
    goto :end
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: py
    py migrate_tools_to_tol.py
    goto :end
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: python3
    python3 migrate_tools_to_tol.py
    goto :end
)

echo.
echo ERROR: Python not found!
echo.
pause
exit /b 1

:end
echo.
echo ================================================================================
echo MIGRATION COMPLETE
echo ================================================================================
echo.
pause