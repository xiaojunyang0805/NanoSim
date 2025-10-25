# NanoSim Week 1 - Quick Start Checklist

## 🚀 Get Your Landing Page Live in 30 Minutes

### Step 1: Push to GitHub (5 minutes)

```bash
# Open terminal in D:\NanoSim
cd D:\NanoSim

# Initialize and push
git init
git add .
git commit -m "Initial setup: landing page and documentation"
git remote add origin https://github.com/xiaojunyang0805/NanoSim.git
git push -u origin main
```

### Step 2: Deploy Landing Page (10 minutes)

**Copy files to root for GitHub Pages:**
```bash
copy landing-page\index.html index.html
copy landing-page\styles.css styles.css
copy landing-page\script.js script.js
copy landing-page\CNAME CNAME

git add index.html styles.css script.js CNAME
git commit -m "Add landing page to root for GitHub Pages"
git push
```

**Enable GitHub Pages:**
1. Go to: https://github.com/xiaojunyang0805/NanoSim/settings/pages
2. Source: `main` branch, `/ (root)` folder
3. Click Save
4. Your site will be live in 2-5 minutes at: https://xiaojunyang0805.github.io/NanoSim

### Step 3: Custom Domain (5 minutes setup + wait for DNS)

**Add DNS Record at your domain provider:**
```
Type: CNAME
Name: nanosim
Value: xiaojunyang0805.github.io
```

**At GitHub:**
1. Repository Settings → Pages
2. Custom domain: `nanosim.seenano.nl`
3. Save
4. Wait for DNS check (✓ mark appears when ready)
5. Enable "Enforce HTTPS"

⏰ DNS takes 1-48 hours (usually 1 hour)

### Step 4: Email Capture (10 minutes)

1. **Sign up:** https://buttondown.email/register
2. **Get URL:** Settings → Embedding
3. **Update form** in `index.html` line 248:
   ```html
   action="https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME"
   ```
4. **Push changes:**
   ```bash
   git add index.html
   git commit -m "Configure email capture"
   git push
   ```

### Step 5: Analytics (Optional - 10 minutes)

1. **Create:** https://analytics.google.com
2. **Get ID:** Will look like `G-XXXXXXXXXX`
3. **Replace** in `index.html` (lines 17 and 22):
   Replace `GA_MEASUREMENT_ID` with your actual ID
4. **Push:**
   ```bash
   git add index.html
   git commit -m "Add Google Analytics"
   git push
   ```

---

## ✅ Verification (5 minutes)

1. Visit your site: https://nanosim.seenano.nl (or GitHub Pages URL)
2. Test email signup with your email
3. Check all navigation links work
4. View on mobile device
5. Check analytics dashboard (may take a few hours)

---

## 🎯 Week 1 Complete Setup (2-3 hours total)

After the quick start above, continue with:

### 6. Local Development (30 minutes)

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Create requirements.txt
echo numpy>=1.24.0 > requirements.txt
echo pyyaml>=6.0 >> requirements.txt
echo fastapi>=0.104.0 >> requirements.txt

# Create requirements-dev.txt
echo -r requirements.txt > requirements-dev.txt
echo pytest==7.4.3 >> requirements-dev.txt
echo black==23.12.1 >> requirements-dev.txt
echo ruff==0.1.9 >> requirements-dev.txt

# Install
pip install -r requirements-dev.txt
```

### 7. Project Structure (15 minutes)

```bash
# Create directories
mkdir src\nanosim src\nanosim\core src\nanosim\engines
mkdir src\nanosim\bridges src\nanosim\utils
mkdir tests\unit tests\integration
mkdir docker examples\liposome_her2 docs

# Create __init__.py files
type nul > src\nanosim\__init__.py
type nul > src\nanosim\core\__init__.py
type nul > src\nanosim\engines\__init__.py

# Commit
git add .
git commit -m "Create project structure"
git push
```

---

## 📋 Week 1 Checklist

### Must Have (Minimum Viable)
- [ ] Landing page live on GitHub Pages
- [ ] Email capture working
- [ ] GitHub repository public
- [ ] Basic documentation in place

### Should Have (Ideal)
- [ ] Custom domain configured (nanosim.seenano.nl)
- [ ] Analytics tracking
- [ ] Local development environment
- [ ] Project structure created

### Nice to Have
- [ ] Welcome email automated
- [ ] Reddit account ready
- [ ] First blog post drafted

---

## 🆘 Quick Troubleshooting

**Landing page not showing?**
- Wait 5 minutes after pushing
- Check GitHub Actions tab for errors
- Visit GitHub Pages URL first: https://xiaojunyang0805.github.io/NanoSim

**Custom domain not working?**
- Check DNS record is correct
- Wait 1 hour minimum
- Use `nslookup nanosim.seenano.nl` to verify
- Try in incognito mode (clear cache)

**Email form not working?**
- Verify Buttondown URL is correct
- Test in different browser
- Check browser console (F12) for errors

---

## 📚 Full Documentation

For detailed instructions, see:
- **DEPLOYMENT_GUIDE.md** - Complete deployment steps
- **WEEK1_SUMMARY.md** - Week 1 overview
- **Implementation_Plan_Month1.md** - Full month plan

---

## 🎉 Success!

When your landing page is live:
1. Share it with a friend for feedback
2. Test email signup yourself
3. Check mobile responsiveness
4. Bookmark your analytics dashboard
5. Start Week 2 tasks!

---

**Questions?** Email: support@seenano.nl
**Issues?** GitHub: https://github.com/xiaojunyang0805/NanoSim/issues

**Next:** Continue with Week 2 content creation and Docker setup!
