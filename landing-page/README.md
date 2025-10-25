# NanoSim Landing Page

This is the landing page for NanoSim, deployed via GitHub Pages.

## Setup Instructions

### 1. Deploy to GitHub Pages

1. Copy all files from this `landing-page` folder to your GitHub repository root or create a `gh-pages` branch
2. Go to your GitHub repository settings
3. Navigate to "Pages" section
4. Set source to "Deploy from a branch"
5. Select branch (main or gh-pages) and folder (/ root or /docs)
6. Click Save

### 2. Configure Custom Domain

#### Step A: DNS Configuration (at your domain provider)
Add a CNAME record for your subdomain:
```
Type: CNAME
Name: nanosim
Value: xiaojunyang0805.github.io
TTL: 3600 (or automatic)
```

#### Step B: GitHub Pages Configuration
1. In your repository settings → Pages
2. Under "Custom domain", enter: `nanosim.seenano.nl`
3. Wait for DNS check to complete (may take a few minutes to 48 hours)
4. Once verified, check "Enforce HTTPS"

### 3. Set Up Email Capture

#### Option A: Buttondown (Recommended)
1. Sign up at https://buttondown.email
2. Get your API URL from settings
3. Replace the form action in `index.html`:
   ```html
   <form action="https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME" method="post">
   ```

#### Option B: Mailchimp
1. Sign up at https://mailchimp.com
2. Create a new audience
3. Get embedded form code
4. Replace form section in `index.html`

#### Option C: Custom Backend
1. Create a simple serverless function (Netlify Functions, Vercel, or AWS Lambda)
2. Update form action to point to your endpoint
3. Store emails in a database or send to your email

### 4. Set Up Analytics

#### Google Analytics
1. Create account at https://analytics.google.com
2. Get your Measurement ID (format: G-XXXXXXXXXX)
3. Replace `GA_MEASUREMENT_ID` in `index.html` with your actual ID

#### Plausible (Privacy-focused alternative)
1. Sign up at https://plausible.io
2. Add your domain
3. Replace Google Analytics script in `index.html` with Plausible script:
   ```html
   <script defer data-domain="nanosim.seenano.nl" src="https://plausible.io/js/script.js"></script>
   ```

### 5. Test Locally

Open `index.html` in your browser or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js http-server
npx http-server

# Then visit http://localhost:8000
```

## File Structure

```
landing-page/
├── index.html          # Main HTML file
├── styles.css          # Stylesheet
├── script.js           # JavaScript for interactions
├── CNAME               # Custom domain configuration
└── README.md           # This file
```

## Customization

### Update Email Address
Replace `support@seenano.nl` in the footer and contact section

### Update GitHub Links
Replace `xiaojunyang0805/NanoSim` with your GitHub username/repo

### Add Logo
1. Add your logo image to the landing-page folder
2. Replace 🧬 emoji in navigation with:
   ```html
   <img src="logo.png" alt="NanoSim Logo" class="logo">
   ```

### Modify Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #2563eb;  /* Change to your brand color */
    --secondary-color: #0891b2;
    /* ... */
}
```

## Performance Optimization

### Before Deploying
1. Minify CSS and JS (optional but recommended for production)
2. Optimize images (use tools like TinyPNG)
3. Enable caching headers via GitHub Pages (automatic)

### Testing
- Test on multiple devices and browsers
- Check mobile responsiveness
- Verify all links work
- Test form submission
- Check page load speed (use Google PageSpeed Insights)

## Maintenance

### Regular Updates
- Update roadmap section as you progress
- Add new use cases and examples
- Update metrics and testimonials (once you have users)
- Add blog posts or news section

### Monitoring
- Check analytics weekly
- Monitor email signup rate
- Track which sections get most engagement
- A/B test headlines and CTAs

## Troubleshooting

### Custom Domain Not Working
- Wait 24-48 hours for DNS propagation
- Verify DNS settings at your domain provider
- Check GitHub Pages settings
- Try clearing browser cache

### Form Not Working
- Check form action URL
- Verify email service is configured correctly
- Test with your own email first
- Check browser console for errors

### Analytics Not Tracking
- Verify Measurement ID is correct
- Check that script loads (browser dev tools)
- Disable ad blockers for testing
- Wait a few hours for data to appear

## Next Steps

1. Deploy landing page to GitHub Pages
2. Configure custom domain
3. Set up email capture service
4. Add analytics tracking
5. Share on social media
6. Monitor signups and iterate

## Support

For issues or questions:
- GitHub Issues: https://github.com/xiaojunyang0805/NanoSim/issues
- Email: support@seenano.nl
