# Quick Setup Guide

## Step 1: Configure GitHub Repository

1. Create the repository `Entities-dropbox-sync` on GitHub (if not already created)
2. Go to Settings → Secrets and variables → Actions
3. Add these 4 secrets:

   - **DROPBOX_ACCESS_TOKEN**: 
     ```
     sl.u.AGKReNaphSViaecZIeAspiE7FnwWLpPi9EuwCA0jbKnZ5HNBt25GsTlVdkS6mhPZm4P447mvrezKGKoxkJF6WvBlKj7PKlgu2xVgIGBEU3-MkxCGSa-STxKpQLSogT4WUPL5ak0Sbi2dLmuZQUhldg2jYzI5fD-oKqqd2atPMR-u4rYLTy6oYQpn0UVEQhc-03GtGEAp7sKB9ElRrRUe9W5c2EHRTKuqeU-acgB33w9keq9R57zn0v107rnuattOKNBc6Be9iYIZuOAg_ACRiskbBZ7O2ADNXvRakFIrhuDMJ6HFrd_-nZaSVXgfadgYtMBFQhTmGrO8GnIdUgZxKKy8TZEDRLUEu5IDTUZruQngzzt1lZRF-F62lUSrAAFi9VGiRZbSC7mhd35jM2kfvx-U_-J8xPO3c2i9Vg9uz8Nj45D6lEAPPFtM4rC1E3Wdo76B3lKtPeyBOhI16jOImYzO6KaeshKHmJhz6l6ZekEBZPV7l4iMowRCF9WoLD98y3av2mMbNpeYDp02TfVyLzKjHnicdvckn2RWdWidVTO74xd-76tndkDoEGQMYKI05xASNTl-WLFkNEpn6F5synZOqCuafNWGzol-I-t16BLw96hykUbOpw7YMZaybs25O-TuFxXIXM-fRSJ81ClwJWc7_IhK1kDAb4Of5oQH5HId-mfzKGC4gGaK9qkkz89ZSp92L4wz681WdmM4Pnkn9_iaWogW17CjWT5V_J8_wlfRetOpBOSjfjPM6uHXC2gBzzJCLLkUjZ7ZDLgJZ3G0ST6OOYBOMTA_usm5D76tcaIIt-2PBsxa-pwwsjoUjQ3-xvZ5SkJwpZeYA7qnBqLMkPsVkz1mn-esBVkY721GWONcp9LBtVnSu7i53kRsIXLgLDVyIGENSZF-tEYt-wpCgH5Le6MRq70NXfBKyl6YCQq0BmZNKYy2uAKJmRoTarDoYT-V1zfp_1GgeVj0EO7XWTJzAGPOZO6P_By1HmABWzpi5svLBgP1A-uhE2jOhsAJrt9-_OTK2R-Ml2rbD2FJwrtfBWpw-_Jm6Yje8jjfsL3BCOJal_hN20R21-cCp9vuQDWImZSF5OUcW-pLyMD5yjIcmSt3pZ8sBa-CJwD3RSvFZmaqYFIzwNb0Fz3D-FRFxUZ-PVw-ejn0tJ5MLHfRjW3MYOivRlwDFPwfqms8IV6hfid5b4kFTaWpaglxAF3j0XMnbIgiYZVL0K3K9pU-SSJ3fEQD9qCFu53Ci32nc6CV0pZNCJKmA8batTiH7WkWy_Wq7Zk1SchKA7Ov-rpkWYbFmGn-nNvTJ2RThpB1qxa705b58FGulMHmgSRVVzoS5FYUCXWfgVJnNb-wk3ysosuOO4Xrrk4L4xWsLmT8Ixr1AHpDu5UPvw3N6qQpQ63OMUab8GnAYAmSSddNuc7U99NqkdC-4SS3M-98iaoOiPC_tQXaNUiaQJ-y5kofyVoSgWaLymKmE5_hV9yi3UNi213v
     ```
   
   - **DROPBOX_REFRESH_TOKEN**: 
     ```
     -u3ObJppx3IAAAAAAAAAAdP9dfbj3KhABcUwwj_NUkNs797tJUxPeCx7hwEiExjx
     ```
   
   - **DROPBOX_APP_KEY**: 
     ```
     z4uw3qzh5ucpnfd
     ```
   
   - **DROPBOX_APP_SECRET**: 
     ```
     kyy5jwehtb0pclm
     ```

## Step 2: Initialize Git Repository

```bash
cd /Users/nikolay/Library/CloudStorage/Dropbox/automations/entities-dropbox-sync
git init
git remote add origin git@github.com:AdminRHS/Entities-dropbox-sync.git
git add .
git commit -m "Initial commit: Dropbox sync automation"
git branch -M main
git push -u origin main
```

## Step 3: Test the Sync

1. Go to your GitHub repository: https://github.com/AdminRHS/Entities-dropbox-sync
2. Click on "Actions" tab
3. Select "Dropbox to GitHub Sync" workflow
4. Click "Run workflow" → "Run workflow" button

The sync will run and sync all files from `/ENTITIES` in Dropbox to GitHub.

## Schedule

The sync runs automatically every 24 hours at 2:00 AM UTC. You can also trigger it manually anytime from the Actions tab.

