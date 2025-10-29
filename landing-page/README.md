# NanoSim Landing Page

This folder contains the landing page for **nanosim.seenano.nl**.

## 📁 Structure

```
landing-page/
├── index.html          # Main HTML file
├── styles.css          # Stylesheet
├── script.js           # JavaScript for interactivity
├── CNAME              # Custom domain configuration (nanosim.seenano.nl)
├── .nojekyll          # Disables Jekyll processing
└── README.md          # This file
```

## 🚀 Deployment

The landing page is automatically deployed to GitHub Pages via GitHub Actions.

**Deployment Process:**
1. Changes pushed to `main` branch in `/landing-page` folder
2. GitHub Actions workflow triggers (`.github/workflows/deploy-landing-page.yml`)
3. Landing page deployed to https://nanosim.seenano.nl
4. Deployment typically takes 1-5 minutes

**Manual Deployment:**
You can also trigger deployment manually from the Actions tab on GitHub.

## 🔧 Local Development

To test the landing page locally:

```bash
# Option 1: Python HTTP server
cd landing-page
python -m http.server 8000
# Visit: http://localhost:8000

# Option 2: Node.js http-server
npm install -g http-server
cd landing-page
http-server
# Visit: http://localhost:8080
```

## 📝 Key Features

### Interactive Workflow Tabs
- Standard Screening (Docking-first)
- Membrane Targeting (MD-first)
- Smooth transitions and animations

### Sections
1. **Hero** - Bidirectional workflow showcase with tabs
2. **Problem** - Current challenges in nanomedicine
3. **Solution** - Adaptive workflows and competitive advantages
4. **Features** - Key platform capabilities
5. **Use Cases** - Example applications
6. **Roadmap** - Development timeline
7. **Signup** - Beta program email capture
8. **Footer** - Links and contact info

## 🎨 Customization

### Colors
Defined in `:root` variables in `styles.css`:
- `--primary-color`: Main brand color (#2563eb)
- `--macro-color`: Macro scale (#3b82f6)
- `--meso-color`: Meso scale (#8b5cf6)
- `--micro-color`: Micro scale (#ec4899)

### Content Updates
- **Hero text**: Edit `index.html` lines 45-49
- **Features**: Edit sections starting at line 189
- **Roadmap**: Update timeline items starting at line 266

### Analytics
Google Analytics tracking ID configured at line 16 of `index.html`.
Replace `GA_MEASUREMENT_ID` with your actual ID.

## 🔗 Links

- **Live Site**: https://nanosim.seenano.nl
- **Main Repo**: https://github.com/xiaojunyang0805/NanoSim
- **GitHub Pages Config**: Repository Settings → Pages

## 📊 Performance

The landing page is optimized for:
- ✅ Fast loading (< 2s on 3G)
- ✅ Mobile responsive
- ✅ SEO friendly
- ✅ Accessibility compliant

## 🐛 Troubleshooting

### Deployment Not Updating
1. Check GitHub Actions tab for build status
2. Hard refresh browser: `Ctrl + Shift + R`
3. Clear browser cache
4. Wait 5-10 minutes for CDN propagation

### Local Testing Issues
- Ensure you're serving from the `landing-page/` directory
- Check browser console for JavaScript errors
- Verify all file paths are relative

## 📞 Contact

Questions about the landing page?
- Email: support@seenano.nl
- GitHub Issues: [Create Issue](https://github.com/xiaojunyang0805/NanoSim/issues)

---

**Last Updated:** October 29, 2025
**Version:** 2.0 (Bidirectional Workflows)
