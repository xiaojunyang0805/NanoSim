@echo off
echo ============================================
echo NanoSim - Initial Git Setup and Push
echo ============================================
echo.

echo Step 1: Copying landing page files to root for GitHub Pages...
copy landing-page\index.html index.html
copy landing-page\styles.css styles.css
copy landing-page\script.js script.js
copy landing-page\CNAME CNAME
echo Done!
echo.

echo Step 2: Initializing Git repository...
git init
echo.

echo Step 3: Adding all files...
git add .
echo.

echo Step 4: Creating initial commit...
git commit -m "Initial project setup: landing page, documentation, and project structure"
echo.

echo Step 5: Adding remote origin...
git remote add origin https://github.com/xiaojunyang0805/NanoSim.git
echo.

echo Step 6: Pushing to GitHub...
git push -u origin main
echo.

echo ============================================
echo Deployment Complete!
echo ============================================
echo.
echo Next Steps:
echo 1. Enable GitHub Pages at:
echo    https://github.com/xiaojunyang0805/NanoSim/settings/pages
echo.
echo 2. Configure DNS CNAME record:
echo    Type: CNAME
echo    Name: nanosim
echo    Value: xiaojunyang0805.github.io
echo.
echo 3. Set up Buttondown email capture at:
echo    https://buttondown.email
echo.
echo 4. Configure Google Analytics at:
echo    https://analytics.google.com
echo.
echo See DEPLOYMENT_GUIDE.md for detailed instructions
echo.
pause
