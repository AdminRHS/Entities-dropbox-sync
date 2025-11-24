#!/usr/bin/env python3
"""
Dropbox Refresh Token Generator

This script helps you get a long-lived refresh token for automatic access token refresh.
"""

import sys
import os
import argparse

try:
    from dropbox import DropboxOAuth2FlowNoRedirect
except ImportError:
    print("ERROR: Dropbox SDK not installed. Run: pip install dropbox")
    sys.exit(1)


def get_refresh_token(app_key=None, app_secret=None, auth_code=None):
    print("=" * 80)
    print("Dropbox Refresh Token Generator")
    print("=" * 80)
    print()
    
    # Get App Key and Secret from arguments, environment, or input
    if not app_key:
        app_key = os.environ.get('DROPBOX_APP_KEY', '').strip()
    if not app_secret:
        app_secret = os.environ.get('DROPBOX_APP_SECRET', '').strip()
    
    if not app_key or not app_secret:
        print("Step 1: Get App Key and App Secret")
        print("1. Go to: https://www.dropbox.com/developers/apps")
        print("2. Find your app (or create a new one)")
        print("3. Go to Settings → App key and App secret")
        print()
        print("You can also pass them as arguments:")
        print("  python3 get_refresh_token.py --app-key YOUR_KEY --app-secret YOUR_SECRET")
        print()
        
        if not app_key:
            app_key = input("Enter App Key: ").strip()
        if not app_secret:
            app_secret = input("Enter App Secret: ").strip()
    
    if not app_key or not app_secret:
        print("❌ App Key and App Secret are required!")
        sys.exit(1)
    
    print()
    print("=" * 80)
    print("Step 2: Authorization")
    print("=" * 80)
    print()
    
    # Create OAuth flow
    auth_flow = DropboxOAuth2FlowNoRedirect(
        app_key, 
        app_secret, 
        token_access_type='offline'  # Important! offline gives refresh token
    )
    
    # Get authorization URL
    authorize_url = auth_flow.start()
    
    print(f"1. Open this link in your browser:")
    print()
    print(f"   {authorize_url}")
    print()
    print("2. Sign in to Dropbox and authorize the app")
    print("3. After authorization, you'll be redirected to a page with a code")
    print("4. Copy the authorization code")
    print()
    
    if not auth_code:
        auth_code = input("Enter authorization code: ").strip()
    
    if not auth_code:
        print("❌ Authorization code is required!")
        print()
        print("You can also pass it as an argument:")
        print("  python3 get_refresh_token.py --app-key KEY --app-secret SECRET --auth-code CODE")
        sys.exit(1)
    
    print()
    print("Getting tokens...")
    
    try:
        # Exchange authorization code for tokens
        oauth_result = auth_flow.finish(auth_code)
        
        print()
        print("=" * 80)
        print("✅ SUCCESS!")
        print("=" * 80)
        print()
        print("Save these values in GitHub Secrets:")
        print()
        print(f"DROPBOX_ACCESS_TOKEN = {oauth_result.access_token}")
        print()
        
        if oauth_result.refresh_token:
            print(f"DROPBOX_REFRESH_TOKEN = {oauth_result.refresh_token}")
            print()
            print("✅ Refresh token obtained! Tokens will now refresh automatically.")
        else:
            print("⚠️  Refresh token not obtained. Make sure you used token_access_type='offline'")
        
        print()
        print("Also add:")
        print(f"DROPBOX_APP_KEY = {app_key}")
        print(f"DROPBOX_APP_SECRET = {app_secret}")
        print()
        print("=" * 80)
        print("Instructions:")
        print("1. Go to your GitHub repository → Settings → Secrets and variables → Actions")
        print("2. Add/update all 4 secrets above")
        print("3. Run the sync - tokens will refresh automatically!")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Possible causes:")
        print("- Invalid authorization code")
        print("- Code already used")
        print("- Code expired (try again)")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get Dropbox refresh token")
    parser.add_argument("--app-key", help="Dropbox App Key (or set DROPBOX_APP_KEY env var)")
    parser.add_argument("--app-secret", help="Dropbox App Secret (or set DROPBOX_APP_SECRET env var)")
    parser.add_argument("--auth-code", help="Authorization code from browser (if you already have it)")
    args = parser.parse_args()
    
    get_refresh_token(app_key=args.app_key, app_secret=args.app_secret, auth_code=args.auth_code)

