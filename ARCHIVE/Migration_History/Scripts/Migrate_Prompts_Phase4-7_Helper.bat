@echo off
REM ============================================================================
REM Prompts Migration Helper Script - PHASES 4-7
REM Date: 2025-11-15
REM Purpose: Assist with documentation updates and reference checking
REM Note: This script helps you identify and track Phase 4-7 tasks
REM       Most updates require manual review and editing
REM ============================================================================

echo.
echo ============================================================================
echo    PROMPTS MIGRATION HELPER - PHASES 4-7
echo    Documentation Updates and Reference Checking
echo ============================================================================
echo.

REM Set base path
set ENTITIES_ROOT=C:\Users\Dell\Dropbox\ENTITIES
set DEST_PROMPTS=%ENTITIES_ROOT%\TASK_MANAGERS\PROMPTS
set OUTPUT_DIR=C:\Users\Dell\Dropbox\ENTITIES\Migration_Reports

echo Current settings:
echo   ENTITIES Root: %ENTITIES_ROOT%
echo   Reports Dir:   %OUTPUT_DIR%
echo.

REM Create output directory for reports
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
    echo Created reports directory: %OUTPUT_DIR%
)
echo.

:MENU
echo.
echo ============================================================================
echo PHASE 4-7 HELPER MENU
echo ============================================================================
echo.
echo [4] Phase 4: Update Documentation and Indexes
echo [5] Phase 5: Find External References (51+ files)
echo [6] Phase 6: Create _SHARED Documentation Templates
echo [7] Phase 7: Pre-Delete Verification Checklist
echo.
echo [A] Run All Reference Scans
echo [V] View Generated Reports
echo [Q] Quit
echo.
set /p CHOICE="Select option: "

if /i "%CHOICE%"=="4" goto PHASE4
if /i "%CHOICE%"=="5" goto PHASE5
if /i "%CHOICE%"=="6" goto PHASE6
if /i "%CHOICE%"=="7" goto PHASE7
if /i "%CHOICE%"=="A" goto RUN_ALL
if /i "%CHOICE%"=="V" goto VIEW_REPORTS
if /i "%CHOICE%"=="Q" goto END
goto MENU

REM ============================================================================
REM PHASE 4: UPDATE DOCUMENTATION AND INDEXES
REM ============================================================================

:PHASE4
echo.
echo ============================================================================
echo PHASE 4: UPDATE DOCUMENTATION AND INDEXES
echo ============================================================================
echo.
echo This phase requires MANUAL EDITING of the following files:
echo.

echo [CRITICAL FILES TO UPDATE]
echo.
echo 1. PROMPTS_INDEX.json
echo    Location: %DEST_PROMPTS%\PROMPTS_INDEX.json
echo    Action: Update metadata section with migration info
echo.
echo 2. Prompts README.md
echo    Location: %DEST_PROMPTS%\README.md
echo    Action: Add migration notice at top
echo.
echo 3. TASK_MANAGERS README.md
echo    Location: %ENTITIES_ROOT%\TASK_MANAGERS\README.md
echo    Action: Add PROMPTS documentation
echo.
echo 4. LIBRARIES README.md (if exists)
echo    Location: %ENTITIES_ROOT%\LIBRARIES\README.md
echo    Action: Mark Prompts as MOVED
echo.
echo 5. LIBRARIES_Import_Index.md (if exists)
echo    Location: %ENTITIES_ROOT%\LIBRARIES\LIBRARIES_Import_Index.md
echo    Action: Update catalog with moved status
echo.
echo.

echo Opening files for editing? (Y/N)
set /p OPEN_FILES="> "

if /i "%OPEN_FILES%"=="Y" (
    echo.
    echo Opening critical files in default editor...

    if exist "%DEST_PROMPTS%\PROMPTS_INDEX.json" (
        start "" "%DEST_PROMPTS%\PROMPTS_INDEX.json"
        echo   Opened: PROMPTS_INDEX.json
        timeout /t 2 >nul
    ) else (
        echo   [ERROR] Not found: PROMPTS_INDEX.json
    )

    if exist "%DEST_PROMPTS%\README.md" (
        start "" "%DEST_PROMPTS%\README.md"
        echo   Opened: Prompts README.md
        timeout /t 2 >nul
    ) else (
        echo   [ERROR] Not found: Prompts README.md
    )

    if exist "%ENTITIES_ROOT%\TASK_MANAGERS\README.md" (
        start "" "%ENTITIES_ROOT%\TASK_MANAGERS\README.md"
        echo   Opened: TASK_MANAGERS README.md
        timeout /t 2 >nul
    ) else (
        echo   [INFO] TASK_MANAGERS README.md not found (may need to create)
    )

    if exist "%ENTITIES_ROOT%\LIBRARIES\README.md" (
        start "" "%ENTITIES_ROOT%\LIBRARIES\README.md"
        echo   Opened: LIBRARIES README.md
        timeout /t 2 >nul
    ) else (
        echo   [INFO] LIBRARIES README.md not found (may not exist)
    )

    if exist "%ENTITIES_ROOT%\LIBRARIES\LIBRARIES_Import_Index.md" (
        start "" "%ENTITIES_ROOT%\LIBRARIES\LIBRARIES_Import_Index.md"
        echo   Opened: LIBRARIES_Import_Index.md
        timeout /t 2 >nul
    ) else (
        echo   [INFO] LIBRARIES_Import_Index.md not found (may not exist)
    )

    echo.
    echo All files opened. Please edit according to full prompt instructions.
    echo See: PROMPT_Move_Prompts_to_Departments_Shared.md (Part 3, Phase 4)
)

echo.
pause
goto MENU

REM ============================================================================
REM PHASE 5: FIND EXTERNAL REFERENCES
REM ============================================================================

:PHASE5
echo.
echo ============================================================================
echo PHASE 5: FIND EXTERNAL REFERENCES (51+ files)
echo ============================================================================
echo.
echo Scanning entire Taxonomy directory for references to old Prompts path...
echo This may take a few minutes...
echo.

cd /d "%ENTITIES_ROOT%\.."

echo [Scan 1/4] Searching for "LIBRARIES/DEPARTMENTS/PROMPTS" in .md files...
findstr /S /I /N /C:"LIBRARIES/DEPARTMENTS/PROMPTS" "%ENTITIES_ROOT%\*.md" > "%OUTPUT_DIR%\References_DEPARTMENTS_PROMPTS_MD.txt" 2>nul
echo   Results saved to: References_DEPARTMENTS_PROMPTS_MD.txt

echo [Scan 2/4] Searching for "LIBRARIES\DEPARTMENTS\PROMPTS" in .md files...
findstr /S /I /N /C:"LIBRARIES\DEPARTMENTS\PROMPTS" "%ENTITIES_ROOT%\*.md" > "%OUTPUT_DIR%\References_DEPARTMENTS_PROMPTS_Backslash_MD.txt" 2>nul
echo   Results saved to: References_DEPARTMENTS_PROMPTS_Backslash_MD.txt

echo [Scan 3/4] Searching for "LIBRARIES/DEPARTMENTS/PROMPTS" in .json files...
findstr /S /I /N /C:"LIBRARIES/DEPARTMENTS/PROMPTS" "%ENTITIES_ROOT%\*.json" > "%OUTPUT_DIR%\References_DEPARTMENTS_PROMPTS_JSON.txt" 2>nul
echo   Results saved to: References_DEPARTMENTS_PROMPTS_JSON.txt

echo [Scan 4/4] Searching for "../PROMPTS" references...
findstr /S /I /N /C:"../PROMPTS" "%ENTITIES_ROOT%\*.md" "%ENTITIES_ROOT%\*.json" > "%OUTPUT_DIR%\References_Relative_PROMPTS.txt" 2>nul
echo   Results saved to: References_Relative_PROMPTS.txt

echo.
echo Generating priority-based reports...
echo.

REM TASK_MANAGERS references
echo [Priority Scan 1/4] TASK_MANAGERS references...
findstr /S /I /N /C:"PROMPTS" "%ENTITIES_ROOT%\TASK_MANAGERS\*.md" "%ENTITIES_ROOT%\TASK_MANAGERS\*.json" > "%OUTPUT_DIR%\References_TASK_MANAGERS.txt" 2>nul
echo   Results saved to: References_TASK_MANAGERS.txt

REM Transcribations references
echo [Priority Scan 2/4] Transcribations references...
if exist "%ENTITIES_ROOT%\LIBRARIES\Transcribations" (
    findstr /S /I /N /C:"PROMPTS" "%ENTITIES_ROOT%\LIBRARIES\Transcribations\*.md" > "%OUTPUT_DIR%\References_Transcribations.txt" 2>nul
    echo   Results saved to: References_Transcribations.txt
) else (
    echo   [SKIP] Transcribations directory not found
)

REM Researches references
echo [Priority Scan 3/4] Researches references...
if exist "%ENTITIES_ROOT%\LIBRARIES\Researches" (
    findstr /S /I /N /C:"PROMPTS" "%ENTITIES_ROOT%\LIBRARIES\Researches\*.md" > "%OUTPUT_DIR%\References_Researches.txt" 2>nul
    echo   Results saved to: References_Researches.txt
) else (
    echo   [SKIP] Researches directory not found
)

REM LIBRARIES main directory references
echo [Priority Scan 4/4] LIBRARIES main references...
if exist "%ENTITIES_ROOT%\LIBRARIES\README.md" (
    findstr /I /N /C:"PROMPTS" "%ENTITIES_ROOT%\LIBRARIES\README.md" "%ENTITIES_ROOT%\LIBRARIES\*.md" > "%OUTPUT_DIR%\References_LIBRARIES_Main.txt" 2>nul
    echo   Results saved to: References_LIBRARIES_Main.txt
) else (
    echo   [SKIP] LIBRARIES directory not found
)

echo.
echo ============================================================================
echo SCAN COMPLETE
echo ============================================================================
echo.
echo All reference scans saved to: %OUTPUT_DIR%
echo.
echo FILES GENERATED:
echo   - References_LIBRARIES_Prompts_MD.txt (all .md files)
echo   - References_LIBRARIES_Prompts_Backslash_MD.txt (backslash paths)
echo   - References_LIBRARIES_Prompts_JSON.txt (all .json files)
echo   - References_Relative_Prompts.txt (relative paths)
echo   - References_TASK_MANAGERS.txt (PRIORITY: CRITICAL)
echo   - References_Transcribations.txt (PRIORITY: CRITICAL)
echo   - References_Researches.txt (PRIORITY: MEDIUM)
echo   - References_LIBRARIES_Main.txt (PRIORITY: CRITICAL)
echo.
echo NEXT STEPS:
echo 1. Review each reference file
echo 2. Update all files with old paths to new paths:
echo    OLD: LIBRARIES/DEPARTMENTS/PROMPTS/
echo    NEW: TASK_MANAGERS/PROMPTS/
echo.
echo 3. Pay special attention to CRITICAL priority files:
echo    - TASK_MANAGERS (15+ files)
echo    - Transcribations (2 files)
echo    - LIBRARIES main files (2 files)
echo.

echo.
echo Open reports directory? (Y/N)
set /p OPEN_REPORTS="> "
if /i "%OPEN_REPORTS%"=="Y" explorer "%OUTPUT_DIR%"

pause
goto MENU

REM ============================================================================
REM PHASE 6: CREATE _SHARED DOCUMENTATION TEMPLATES
REM ============================================================================

:PHASE6
echo.
echo ============================================================================
echo PHASE 6: CREATE _SHARED DOCUMENTATION TEMPLATES
echo ============================================================================
echo.

set PROMPTS_DIR=%ENTITIES_ROOT%\TASK_MANAGERS\PROMPTS
set ARCHIVE_DIR=%PROMPTS_DIR%\Archive

echo This will create README templates for:
echo   1. TASK_MANAGERS\PROMPTS\README.md (already exists)
echo   2. TASK_MANAGERS\PROMPTS\Archive\README.md (if Archive exists)
echo.

echo Checking directories...
if not exist "%PROMPTS_DIR%" (
    echo [ERROR] PROMPTS directory not found: %PROMPTS_DIR%
    echo Please complete the move operation first.
    pause
    goto MENU
)

echo Directories verified.
echo.

echo Templates will be created with placeholder content.
echo You can edit them after creation.
echo.
echo Create templates? (Y/N)
set /p CREATE_TEMPLATES="> "

if /i "%CREATE_TEMPLATES%"=="Y" (
    echo.
    echo Creating _SHARED\README.md template...

    if exist "%SHARED_DIR%\README.md" (
        echo   [WARNING] README.md already exists. Overwrite? (Y/N)
        set /p OVERWRITE_SHARED="> "
        if /i not "%OVERWRITE_SHARED%"=="Y" goto SKIP_SHARED_README
    )

    echo # TASK_MANAGERS / PROMPTS >> "%PROMPTS_DIR%\README.md"
    echo. >> "%PROMPTS_DIR%\README.md"
    echo **Purpose:** Centralized AI prompt library for all departments >> "%PROMPTS_DIR%\README.md"
    echo **Last Updated:** 2025-11-15 >> "%PROMPTS_DIR%\README.md"
    echo **Location:** Moved from LIBRARIES/DEPARTMENTS/PROMPTS to TASK_MANAGERS/PROMPTS >> "%PROMPTS_DIR%\README.md"
    echo. >> "%PROMPTS_DIR%\README.md"
    echo [TODO: Add detailed documentation] >> "%PROMPTS_DIR%\README.md"
    echo. >> "%PROMPTS_DIR%\README.md"
    echo   Updated: %PROMPTS_DIR%\README.md

    :SKIP_SHARED_README

    echo.
    echo Creating _SHARED\Archive\README.md template...

    if exist "%ARCHIVE_DIR%\README.md" (
        echo   [WARNING] Archive\README.md already exists. Overwrite? (Y/N)
        set /p OVERWRITE_ARCHIVE="> "
        if /i not "%OVERWRITE_ARCHIVE%"=="Y" goto SKIP_ARCHIVE_README
    )

    echo # _SHARED / Archive > "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo **Purpose:** Historical and deprecated shared resources >> "%ARCHIVE_DIR%\README.md"
    echo **Last Updated:** 2025-11-15 >> "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo ## Contents >> "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo ### Prompts_Archive (^`Prompts_Archive/^`) >> "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo **Archived:** 2025-11-15 (moved with Prompts migration) >> "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo [TODO: Add detailed documentation from full prompt Part 3, Phase 4, Step 4.6] >> "%ARCHIVE_DIR%\README.md"
    echo. >> "%ARCHIVE_DIR%\README.md"
    echo   Created: %ARCHIVE_DIR%\README.md (TEMPLATE - PLEASE EDIT)

    :SKIP_ARCHIVE_README

    echo.
    echo Templates created!
    echo.
    echo IMPORTANT: These are TEMPLATES with placeholder content.
    echo Please edit them according to full prompt instructions.
    echo See: PROMPT_Move_Prompts_to_Departments_Shared.md (Part 3, Phase 4, Steps 4.6.1 and 4.6.2)
    echo.

    echo Open templates for editing? (Y/N)
    set /p OPEN_TEMPLATES="> "
    if /i "%OPEN_TEMPLATES%"=="Y" (
        if exist "%SHARED_DIR%\README.md" start "" "%SHARED_DIR%\README.md"
        timeout /t 2 >nul
        if exist "%ARCHIVE_DIR%\README.md" start "" "%ARCHIVE_DIR%\README.md"
    )
)

echo.
pause
goto MENU

REM ============================================================================
REM PHASE 7: PRE-DELETE VERIFICATION CHECKLIST
REM ============================================================================

:PHASE7
echo.
echo ============================================================================
echo PHASE 7: PRE-DELETE VERIFICATION CHECKLIST
echo ============================================================================
echo.
echo Before deleting the old LIBRARIES\Prompts directory, verify:
echo.

set /a CHECKS_PASSED=0
set /a TOTAL_CHECKS=10

echo [Check 1/10] All files moved to new location?
if exist "%DEST_PROMPTS%\PROMPTS_INDEX.json" (
    echo   [PASS] PROMPTS_INDEX.json exists at new location
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] PROMPTS_INDEX.json NOT FOUND at new location
)

echo [Check 2/10] README exists at new location?
if exist "%DEST_PROMPTS%\README.md" (
    echo   [PASS] README.md exists at new location
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] README.md NOT FOUND at new location
)

echo [Check 3/10] Archive moved separately?
if exist "%DEST_PROMPTS%\Archive\README.md" (
    echo   [PASS] Archive exists at new location
    set /a CHECKS_PASSED+=1
) else (
    echo   [INFO] Archive may not exist or was integrated into PROMPTS
)

echo [Check 4/10] Core directory exists?
if exist "%DEST_PROMPTS%\Core" (
    echo   [PASS] Core/ directory exists
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] Core/ directory NOT FOUND
)

echo [Check 5/10] Video Processing directory exists?
if exist "%DEST_PROMPTS%\Video_Processing" (
    echo   [PASS] Video_Processing/ directory exists
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] Video_Processing/ directory NOT FOUND
)

echo [Check 6/10] HR Operations directory exists?
if exist "%DEST_PROMPTS%\HR_Operations" (
    echo   [PASS] HR_Operations/ directory exists
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] HR_Operations/ directory NOT FOUND
)

echo.
echo [Check 7/10] File count verification
echo   Counting files at new location...
for /f %%A in ('dir /s /b "%DEST_PROMPTS%" ^| find /c /v ""') do set NEW_FILE_COUNT=%%A
echo   Files at new location: %NEW_FILE_COUNT%
echo   Expected: 135 files (or 146 if Archive wasn't deleted from new location)
if %NEW_FILE_COUNT% GEQ 135 (
    echo   [PASS] Sufficient files present
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] Insufficient files - expected at least 135
)

echo.
echo [Check 8/10] PROMPTS_INDEX.json updated?
echo   Please verify manually that PROMPTS_INDEX.json contains migration info
echo   Has PROMPTS_INDEX.json been updated? (Y/N)
set /p INDEX_UPDATED="> "
if /i "%INDEX_UPDATED%"=="Y" (
    echo   [PASS] PROMPTS_INDEX.json updated
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] PROMPTS_INDEX.json NOT updated
)

echo.
echo [Check 9/10] Documentation updated?
echo   Have all documentation files been updated? (Y/N)
echo   (DEPARTMENTS README, LIBRARIES README, LIBRARIES_Import_Index, etc.)
set /p DOCS_UPDATED="> "
if /i "%DOCS_UPDATED%"=="Y" (
    echo   [PASS] Documentation updated
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] Documentation NOT updated
)

echo.
echo [Check 10/10] External references updated?
echo   Have all 51+ external references been updated? (Y/N)
echo   (TASK_MANAGERS, Transcribations, Researches, etc.)
set /p REFS_UPDATED="> "
if /i "%REFS_UPDATED%"=="Y" (
    echo   [PASS] External references updated
    set /a CHECKS_PASSED+=1
) else (
    echo   [FAIL] External references NOT updated
)

echo.
echo ============================================================================
echo VERIFICATION RESULTS: %CHECKS_PASSED% / %TOTAL_CHECKS% PASSED
echo ============================================================================
echo.

if %CHECKS_PASSED% EQU %TOTAL_CHECKS% (
    echo [SUCCESS] All checks passed! Safe to delete old location.
    echo.
    echo WARNING: This action is IRREVERSIBLE!
    echo.
    echo Old location: %ENTITIES_ROOT%\LIBRARIES\DEPARTMENTS\PROMPTS
    echo.
    echo Delete old LIBRARIES\DEPARTMENTS\PROMPTS directory now? (Y/N)
    set /p DELETE_OLD="> "

    if /i "%DELETE_OLD%"=="Y" (
        echo.
        echo Final confirmation required!
        echo Type "DELETE" to confirm deletion (case-sensitive):
        set /p CONFIRM_DELETE="> "

        if "%CONFIRM_DELETE%"=="DELETE" (
            echo.
            echo Deleting old LIBRARIES\DEPARTMENTS\PROMPTS directory...
            rmdir /S /Q "%ENTITIES_ROOT%\LIBRARIES\DEPARTMENTS\PROMPTS"

            if %errorlevel% equ 0 (
                echo   [SUCCESS] Old directory deleted successfully
                echo.
                echo Verifying deletion...
                if not exist "%ENTITIES_ROOT%\LIBRARIES\DEPARTMENTS\PROMPTS" (
                    echo   [VERIFIED] Old directory no longer exists
                    echo.
                    echo ============================================================================
                    echo MIGRATION COMPLETE!
                    echo ============================================================================
                    echo.
                    echo Next steps:
                    echo 1. Create migration completion report
                    echo 2. Update taxonomy change log (if exists)
                    echo 3. Test critical workflows
                    echo.
                    echo See full prompt Part 3, Phase 8 for post-migration documentation.
                ) else (
                    echo   [ERROR] Directory still exists - deletion may have failed partially
                )
            ) else (
                echo   [ERROR] Deletion failed! Error code: %errorlevel%
                echo   You may need to delete manually.
            )
        ) else (
            echo.
            echo Deletion cancelled (confirmation did not match).
        )
    ) else (
        echo.
        echo Deletion cancelled by user.
    )
) else (
    echo [FAIL] Not all checks passed. DO NOT DELETE old location yet.
    echo.
    echo Failed checks: %TOTAL_CHECKS% - %CHECKS_PASSED% = %CHECKS_FAILED%
    echo.
    echo Please complete all phases and ensure all checks pass before deletion.
)

echo.
pause
goto MENU

REM ============================================================================
REM RUN ALL REFERENCE SCANS
REM ============================================================================

:RUN_ALL
echo.
echo ============================================================================
echo RUNNING ALL REFERENCE SCANS
echo ============================================================================
echo.
echo This will run all Phase 5 reference scans.
echo Results will be saved to: %OUTPUT_DIR%
echo.
pause

goto PHASE5

REM ============================================================================
REM VIEW GENERATED REPORTS
REM ============================================================================

:VIEW_REPORTS
echo.
echo Opening reports directory...
if exist "%OUTPUT_DIR%" (
    explorer "%OUTPUT_DIR%"
) else (
    echo [ERROR] Reports directory not found: %OUTPUT_DIR%
    echo Run Phase 5 scans first to generate reports.
)
pause
goto MENU

REM ============================================================================
REM END
REM ============================================================================

:END
echo.
echo Exiting helper script.
echo.
echo For full migration instructions, see:
echo   PROMPT_Move_Prompts_to_Departments_Shared.md
echo.
pause
