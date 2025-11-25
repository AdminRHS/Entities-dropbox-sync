#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleanup Duplicate Milestones: Remove incorrectly named duplicate milestone files
Removes files with pattern PROJ-XXX_MIL-MIL-XXX_XXX_*.json (duplicate MIL- prefix)

Created: November 25, 2025
"""

import os
from pathlib import Path

MILESTONES_DIR = Path(__file__).parent / "Milestones"


def main():
    """Remove duplicate milestone files with incorrect naming."""
    print("=" * 60)
    print("Cleanup Duplicate Milestones")
    print("=" * 60)
    
    if not MILESTONES_DIR.exists():
        print(f"Error: Milestones directory not found: {MILESTONES_DIR}")
        return
    
    # Find files with duplicate MIL- prefix pattern
    duplicate_pattern = "_MIL-MIL-"
    all_files = list(MILESTONES_DIR.glob("*.json"))
    
    duplicates = [f for f in all_files if duplicate_pattern in f.name]
    
    if not duplicates:
        print("\nNo duplicate files found.")
        return
    
    print(f"\nFound {len(duplicates)} duplicate files:")
    
    for dup_file in duplicates:
        print(f"  - {dup_file.name}")
        dup_file.unlink()
        print(f"    Deleted")
    
    print("\n" + "=" * 60)
    print(f"Removed {len(duplicates)} duplicate files")
    print("=" * 60)


if __name__ == "__main__":
    main()


