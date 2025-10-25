# Push NanoSim to GitHub - Step by Step

## Option 1: Use the Deploy Script (Easiest - 2 minutes)

1. **Open Command Prompt or PowerShell**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - Navigate to project: `cd D:\NanoSim`

2. **Run the deploy script:**
   ```bash
   deploy.bat
   ```

3. **Done!** The script will:
   - Copy landing page files to root
   - Initialize Git
   - Add all files
   - Commit everything
   - Push to GitHub

---

## Option 2: Manual Commands (5 minutes)

If you prefer to run commands manually or the script doesn't work:

### Step 1: Open Terminal in Project Folder

```bash
cd D:\NanoSim
```

### Step 2: Copy Landing Page to Root

```bash
copy landing-page\index.html index.html
copy landing-page\styles.css styles.css
copy landing-page\script.js script.js
copy landing-page\CNAME CNAME
```

### Step 3: Initialize Git and Push

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial project setup: landing page, documentation, and project structure"

# Add remote (your repo)
git remote add origin https://github.com/xiaojunyang0805/NanoSim.git

# Push to GitHub
git push -u origin main
```

**Note:** If you get an error about "main" branch not existing, try:
```bash
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### Error: "fatal: remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/xiaojunyang0805/NanoSim.git
git push -u origin main
```

### Error: "Authentication failed"

You need to authenticate with GitHub:

**Option A: Use Personal Access Token**
1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `workflow`
4. Copy the token
5. When pushing, use token as password

**Option B: Use GitHub Desktop**
1. Download: https://desktop.github.com
2. Sign in to GitHub
3. File → Add Local Repository
4. Select `D:\NanoSim`
5. Publish repository

**Option C: Configure Git Credential Manager**
```bash
git config --global credential.helper manager
git push -u origin main
```

### Error: Repository not empty

If your GitHub repo already has files:

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

Or force push (⚠️ this will overwrite GitHub repo):
```bash
git push -u origin main --force
```

---

## Verify Push Succeeded

1. Go to: https://github.com/xiaojunyang0805/NanoSim
2. You should see all files:
   - README.md
   - index.html, styles.css, script.js
   - Motivation.md, CONTRIBUTING.md, LICENSE
   - landing-page/ folder
   - All documentation files

3. Check the commit message:
   "Initial project setup: landing page, documentation, and project structure"

---

## Next Steps After Push

### 1. Enable GitHub Pages (5 minutes)

1. Go to: https://github.com/xiaojunyang0805/NanoSim/settings/pages
2. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
3. Click "Save"
4. Wait 2-5 minutes
5. Your site will be live at: https://xiaojunyang0805.github.io/NanoSim

### 2. Configure Custom Domain (5 minutes)

**At your DNS provider (for seenano.nl):**

Add CNAME record:
```
Type: CNAME
Name: nanosim
Value: xiaojunyang0805.github.io
TTL: 3600
```

**At GitHub:**
1. Repository Settings → Pages
2. Custom domain: `nanosim.seenano.nl`
3. Save
4. Wait for DNS check (green checkmark)
5. Enable "Enforce HTTPS"

### 3. Set Up Email Capture (10 minutes)

1. Sign up: https://buttondown.email
2. Get your embed URL
3. Edit `index.html` line 248:
   ```html
   action="https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME"
   ```
4. Commit and push:
   ```bash
   git add index.html
   git commit -m "Configure Buttondown email capture"
   git push
   ```

### 4. Set Up Analytics (10 minutes)

1. Create account: https://analytics.google.com
2. Get Measurement ID (G-XXXXXXXXXX)
3. Edit `index.html` lines 17 and 22
4. Replace `GA_MEASUREMENT_ID` with your ID
5. Commit and push:
   ```bash
   git add index.html
   git commit -m "Add Google Analytics tracking"
   git push
   ```

---

## Quick Test Commands

After pushing, verify everything:

```bash
# Check remote is set
git remote -v

# Check current branch
git branch

# Check status
git status

# View commit history
git log --oneline
```

---

## Git Basics for Future Updates

### Make changes and push:

```bash
# Make your changes to files

# See what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

### Pull latest changes:

```bash
git pull
```

---

## Summary

✅ **Run `deploy.bat`** or follow manual commands above
✅ **Verify** at https://github.com/xiaojunyang0805/NanoSim
✅ **Enable GitHub Pages** in repository settings
✅ **Configure DNS** for custom domain
✅ **Set up email** and analytics

**Total time:** 10-15 minutes (+ DNS wait time)

---

**Need help?**
- Check DEPLOYMENT_GUIDE.md for detailed instructions
- Check QUICKSTART.md for quick reference
- Email: support@seenano.nl

**Ready to push? Run `deploy.bat` now!** 🚀
