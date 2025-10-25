# NanoSim Deployment Guide - Week 1

## Quick Start Checklist

Follow these steps to get everything set up for Week 1:

### ✅ Step 1: Push Code to GitHub (5 minutes)

```bash
cd D:\NanoSim

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial project setup with landing page and documentation"

# Add remote (your repo already exists)
git remote add origin https://github.com/xiaojunyang0805/NanoSim.git

# Push to GitHub
git push -u origin main
```

### ✅ Step 2: Deploy Landing Page to GitHub Pages (10 minutes)

#### Option A: Deploy from main branch (Recommended)

1. **Move landing page files to root** (for easier GitHub Pages deployment):
   ```bash
   # Copy landing page files to root
   copy landing-page\index.html index.html
   copy landing-page\styles.css styles.css
   copy landing-page\script.js script.js
   copy landing-page\CNAME CNAME

   # Commit changes
   git add index.html styles.css script.js CNAME
   git commit -m "Add landing page to root for GitHub Pages"
   git push
   ```

2. **Enable GitHub Pages:**
   - Go to: https://github.com/xiaojunyang0805/NanoSim/settings/pages
   - Under "Source", select "Deploy from a branch"
   - Select branch: `main`
   - Select folder: `/ (root)`
   - Click "Save"

#### Option B: Use gh-pages branch

```bash
# Create gh-pages branch
git checkout -b gh-pages

# Keep only landing page files
git rm -rf --cached .
git add landing-page/*
git commit -m "Landing page for GitHub Pages"
git push -u origin gh-pages

# Switch back to main
git checkout main
```

Then in GitHub settings, select `gh-pages` branch as source.

### ✅ Step 3: Configure Custom Domain (15 minutes)

#### At Your Domain Provider (seenano.nl DNS settings)

Add a CNAME record:

```
Type: CNAME
Name: nanosim
Value: xiaojunyang0805.github.io
TTL: 3600 (or Auto)
```

**Example for common providers:**

**Cloudflare:**
1. Login to Cloudflare dashboard
2. Select your domain (seenano.nl)
3. Go to DNS → Records
4. Click "Add record"
5. Type: CNAME
6. Name: nanosim
7. Target: xiaojunyang0805.github.io
8. Proxy status: DNS only (gray cloud)
9. Save

**Other providers (GoDaddy, Namecheap, etc.):**
- Similar process, look for "DNS Management" or "Advanced DNS"

#### At GitHub

1. Go to: https://github.com/xiaojunyang0805/NanoSim/settings/pages
2. Under "Custom domain", enter: `nanosim.seenano.nl`
3. Click "Save"
4. Wait for DNS check (5 minutes to 48 hours, usually ~1 hour)
5. Once verified, check "Enforce HTTPS"

**Verify DNS:**
```bash
# Wait 5-10 minutes, then check:
nslookup nanosim.seenano.nl

# Should return: xiaojunyang0805.github.io
```

### ✅ Step 4: Set Up Email Capture (20 minutes)

#### Option A: Buttondown (Recommended - Free & Simple)

1. **Sign up:**
   - Go to: https://buttondown.email/register
   - Create account (free for first 100 subscribers)

2. **Get embed code:**
   - After signup, go to Settings → Embedding
   - Copy your unique URL (looks like: `https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME`)

3. **Update landing page:**
   Open `index.html` (or `landing-page/index.html`) and find the form:

   ```html
   <!-- Replace this line: -->
   <form id="signup-form" class="signup-form" action="https://buttondown.email/api/emails/embed-subscribe/nanosim" method="post" target="_blank">

   <!-- With your actual Buttondown URL: -->
   <form id="signup-form" class="signup-form" action="https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME" method="post" target="_blank">
   ```

4. **Commit and push:**
   ```bash
   git add index.html
   git commit -m "Configure Buttondown email capture"
   git push
   ```

5. **Create welcome email in Buttondown:**
   - Go to Dashboard → Emails → New Email
   - Subject: "Welcome to NanoSim! 🧬"
   - Use the template from `Implementation_Plan_Month1.md` (Week 1 section)
   - Schedule as automated welcome email

#### Option B: Mailchimp

1. Sign up at https://mailchimp.com (free up to 500 subscribers)
2. Create new audience
3. Create embedded form
4. Get form code and replace form section in `index.html`

### ✅ Step 5: Set Up Analytics (15 minutes)

#### Option A: Google Analytics (More features)

1. **Create account:**
   - Go to: https://analytics.google.com
   - Sign in with Google account
   - Create new property for "nanosim.seenano.nl"

2. **Get Measurement ID:**
   - After creating property, you'll get an ID like: `G-XXXXXXXXXX`
   - Copy this ID

3. **Update landing page:**
   Open `index.html` and replace both instances of `GA_MEASUREMENT_ID`:

   ```html
   <!-- Find these lines: -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
   <script>
       window.dataLayer = window.dataLayer || [];
       function gtag(){dataLayer.push(arguments);}
       gtag('js', new Date());
       gtag('config', 'GA_MEASUREMENT_ID');  <!-- Replace here too -->
   </script>
   ```

   Replace `GA_MEASUREMENT_ID` with your actual ID (both places)

4. **Commit and push:**
   ```bash
   git add index.html
   git commit -m "Configure Google Analytics"
   git push
   ```

#### Option B: Plausible (Privacy-focused, Paid after trial)

1. Sign up at https://plausible.io
2. Add your domain: nanosim.seenano.nl
3. Replace Google Analytics script in `index.html` with:
   ```html
   <script defer data-domain="nanosim.seenano.nl" src="https://plausible.io/js/script.js"></script>
   ```

### ✅ Step 6: Set Up Local Development Environment (30 minutes)

```bash
# Navigate to project
cd D:\NanoSim

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

# Create requirements files
```

**Create `requirements.txt`:**
```bash
echo numpy>=1.24.0 > requirements.txt
echo pyyaml>=6.0 >> requirements.txt
echo fastapi>=0.104.0 >> requirements.txt
echo uvicorn>=0.24.0 >> requirements.txt
echo click>=8.1.0 >> requirements.txt
```

**Create `requirements-dev.txt`:**
```bash
echo -r requirements.txt > requirements-dev.txt
echo black==23.12.1 >> requirements-dev.txt
echo ruff==0.1.9 >> requirements-dev.txt
echo mypy==1.8.0 >> requirements-dev.txt
echo pytest==7.4.3 >> requirements-dev.txt
echo pytest-cov==4.1.0 >> requirements-dev.txt
echo pre-commit==3.6.0 >> requirements-dev.txt
```

**Install dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements-dev.txt
```

**Set up pre-commit hooks:**
```bash
pre-commit install
```

### ✅ Step 7: Create Initial Project Structure (15 minutes)

```bash
# Create directory structure
mkdir src\nanosim
mkdir src\nanosim\core
mkdir src\nanosim\engines
mkdir src\nanosim\bridges
mkdir src\nanosim\utils
mkdir src\nanosim\orchestrator
mkdir tests\unit
mkdir tests\integration
mkdir docker
mkdir examples\liposome_her2
mkdir docs
mkdir docs\tutorials

# Create __init__.py files
type nul > src\nanosim\__init__.py
type nul > src\nanosim\core\__init__.py
type nul > src\nanosim\engines\__init__.py
type nul > src\nanosim\bridges\__init__.py
type nul > src\nanosim\utils\__init__.py
type nul > src\nanosim\orchestrator\__init__.py

# Create empty test files
type nul > tests\__init__.py
type nul > tests\unit\__init__.py
type nul > tests\integration\__init__.py

# Commit structure
git add .
git commit -m "Create project directory structure"
git push
```

### ✅ Step 8: Verify Everything Works (10 minutes)

**Test landing page:**
1. Wait 2-5 minutes after pushing
2. Visit: https://nanosim.seenano.nl (or https://xiaojunyang0805.github.io/NanoSim if domain not ready)
3. Test email signup form
4. Check that all links work

**Test analytics:**
1. Visit your landing page
2. Wait 5-10 minutes
3. Check Google Analytics dashboard for real-time visitors

**Test local development:**
```bash
# Activate venv
venv\Scripts\activate

# Run Python
python
>>> import nanosim
>>> print("Setup successful!")
```

## Week 1 Complete Setup Summary

After completing all steps, you should have:

✅ GitHub repository with all code
✅ Landing page live at nanosim.seenano.nl
✅ Email capture working (Buttondown/Mailchimp)
✅ Analytics tracking visitors
✅ Local development environment ready
✅ Project structure initialized

## Next Steps (Week 2)

1. **Reddit Content Creation:**
   - Write first educational post on multi-scale simulation
   - Post to r/nanotech and r/bioinformatics

2. **Start Docker Containers:**
   - Research OpenFOAM, GROMACS, AutoDock Docker images
   - Begin Dockerfile creation

3. **Core Architecture:**
   - Implement base classes in `src/nanosim/core/`
   - Set up configuration schema

## Troubleshooting

### Landing page not showing
- Check GitHub Pages is enabled in settings
- Verify CNAME file exists in repository root
- Wait up to 10 minutes for deployment
- Check GitHub Actions for build errors

### Custom domain not working
- Verify DNS CNAME record is correct
- Wait 1-48 hours for DNS propagation (usually ~1 hour)
- Try accessing via xiaojunyang0805.github.io/NanoSim temporarily
- Clear browser cache

### Email form not submitting
- Check form action URL is correct
- Verify email service (Buttondown/Mailchimp) is configured
- Test in different browser
- Check browser console for errors

### Analytics not tracking
- Verify Measurement ID is correct in both places
- Disable ad blockers for testing
- Wait a few hours for data to appear
- Check in "Real-time" view first

### Local environment issues
- Make sure Python 3.11+ is installed
- Try deleting venv folder and recreating
- Run as administrator if permission errors
- Check Python is in system PATH

## Support

If you encounter issues:
1. Check this troubleshooting section
2. Review implementation plan: `Implementation_Plan_Month1.md`
3. Check GitHub Pages documentation
4. Contact support@seenano.nl

## Time Estimate

- Total setup time: ~2-3 hours
- Can be done in one session or split across multiple days
- Most time spent waiting for DNS propagation and deployments

## Success Metrics - End of Week 1

- [ ] Landing page live and accessible
- [ ] Email capture functional (test with your email)
- [ ] Analytics tracking visitors
- [ ] GitHub repository fully organized
- [ ] Local development environment working
- [ ] All documentation in place

**Congratulations! Week 1 foundation is complete! 🎉**
