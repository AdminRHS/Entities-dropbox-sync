@echo off
echo ============================================================
echo CLEANUP: Removing Remaining Old Folders
echo ============================================================
echo.
echo This will remove:
echo   - CREATIVES/
echo   - DEPARTMENTS/
echo.
echo Please close any files from these folders in your IDE first!
echo.
pause

cd /d "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"

echo.
echo Removing CREATIVES folder...
if exist "CREATIVES" (
    rmdir /s /q "CREATIVES"
    if not exist "CREATIVES" (
        echo [OK] CREATIVES removed
    ) else (
        echo [ERROR] Could not remove CREATIVES - files may be open
    )
) else (
    echo [SKIP] CREATIVES already removed
)

echo.
echo Removing DEPARTMENTS folder...
if exist "DEPARTMENTS" (
    rmdir /s /q "DEPARTMENTS"
    if not exist "DEPARTMENTS" (
        echo [OK] DEPARTMENTS removed
    ) else (
        echo [ERROR] Could not remove DEPARTMENTS - files may be open
    )
) else (
    echo [SKIP] DEPARTMENTS already removed
)

echo.
echo ============================================================
echo Cleanup Complete!
echo ============================================================
echo.
echo Current structure:
dir /ad /b
echo.
echo All prompts should now be in Core/ folder only
echo.
pause
