# Landing Page Deployment Checklist

## Cache Busting Strategy

To prevent browser caching issues when deploying updates, follow this checklist:

### Before Every Deployment

1. **Increment Cache Version Numbers**
   - [ ] Update `CACHE VERSION` comment in `index.html` (line 5)
   - [ ] Update `styles.css?v=X` in `index.html` (line 17)
   - [ ] Update cache version comment in `styles.css` (line 5)

2. **For Image Updates**
   - [ ] Update hero background version in `styles.css` (`.hero` section, currently v=13)
   - [ ] Update logo version in `index.html` (navigation section, currently v=8)
   - [ ] Update any other image references with `?v=X` parameters

3. **Test Locally**
   - [ ] Open `index.html` in browser
   - [ ] Verify all styles are applied correctly
   - [ ] Check logo size (should be 48x48px)
   - [ ] Verify hero background displays correctly
   - [ ] Test responsive design on mobile

4. **Commit and Push**
   ```bash
   git add landing-page/
   git commit -m "Update landing page - bump cache version to vX"
   git push
   ```

5. **Verify Deployment**
   - [ ] Wait 2-3 minutes for deployment to complete
   - [ ] Visit https://nanosim.seenano.nl
   - [ ] Do a hard refresh (Ctrl+Shift+F5 or Ctrl+Shift+R)
   - [ ] Verify changes are live
   - [ ] Check in different browsers if possible

## Current Version Numbers

| Asset | Version | Location |
|-------|---------|----------|
| CSS File | v=8 | `index.html` line 17 |
| Hero Background | v=13 | `styles.css` line 167 |
| Logo Image | v=8 | `index.html` line 29 |

## Common Issues

### Issue: Old styles still showing
**Solution:** Increment the CSS version number in `index.html`

### Issue: Old images still showing
**Solution:** Increment the image version numbers in both HTML and CSS

### Issue: Changes work locally but not on deployed site
**Solution:** Check if CDN/hosting provider has caching. May need to clear CDN cache or wait longer.

## Notes

- Always increment version numbers when making visual changes
- The version number should be the same across the main CSS and HTML references
- Individual assets (like images) can have their own version numbers
- When in doubt, increment all version numbers by 1
