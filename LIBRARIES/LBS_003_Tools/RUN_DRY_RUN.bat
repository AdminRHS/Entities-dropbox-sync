@echo off
echo ================================================================================
echo TOOL MIGRATION - DRY RUN
echo ================================================================================
echo.
echo This will simulate the migration without making any changes.
echo.

REM Try different Python commands
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: python
    python migrate_tools_to_tol.py --dry-run
    goto :end
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: py
    py migrate_tools_to_tol.py --dry-run
    goto :end
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Found: python3
    python3 migrate_tools_to_tol.py --dry-run
    goto :end
)

echo.
echo ERROR: Python not found!
echo.
echo Please install Python 3.7+ from https://www.python.org/downloads/
echo.
pause
exit /b 1

:end
echo.
echo ================================================================================
echo DRY RUN COMPLETE
echo ================================================================================
echo.
echo Review the reports in:
echo C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\
echo.
echo Key files to review:
echo - migration_mapping_table.csv (ID mappings)
echo - unmapped_tools_report.csv (tools needing manual IDs)
echo - duplicate_resolution_decisions.json (duplicate handling)
echo - dry_run_summary.json (statistics)
echo.
pause