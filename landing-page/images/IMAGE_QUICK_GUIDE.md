# Quick Image Implementation Guide

## 🎯 Top 5 Images to Add (Priority Order)

### 1. Three-Scale Comparison (HIGHEST PRIORITY)
**Where:** Features section or new section after hero
**What:** Side-by-side showing macro, meso, micro scales
**Size:** 1200x400px
**Impact:** ⭐⭐⭐⭐⭐

**How to Get:**
- **Option A:** Create in Figma (3 panels with labels)
- **Option B:** Use AI: "Three panel scientific illustration showing blood vessels at macro scale, cell membrane at meso scale, and molecular docking at micro scale, professional medical textbook style"
- **Option C:** Find on Science Photo Library

---

### 2. Molecular Docking Visualization
**Where:** Use Cases section (Drug Delivery)
**What:** HER2 receptor with antibody bound
**Size:** 600x400px
**Impact:** ⭐⭐⭐⭐⭐

**How to Get (FREE):**
```python
# PyMOL script - Takes 5 minutes
fetch 3pp0
bg_color white
hide everything
show cartoon, chain A
show surface, chain H+L
color cyan, chain A
color magenta, chain H+L
set transparency, 0.3
orient
ray 1200, 800
png her2_antibody.png, dpi=300
```

**Download PyMOL:** https://pymol.org/ (free for education)

---

### 3. Workflow Diagram
**Where:** Features section (Bidirectional Scale Bridging)
**What:** Flowchart showing both workflow directions
**Size:** 800x500px
**Impact:** ⭐⭐⭐⭐

**How to Create:**
- **Figma/PowerPoint:** Use shapes and arrows
- **Draw.io:** Free online diagramming tool
- **Mermaid:** Generate from code (already in README)

**Quick Figma Template:**
```
3 boxes (Macro, Micro, Meso)
Arrows showing: Macro → Micro → Meso (Standard)
Arrows showing: Macro → Meso → Micro → Meso (Membrane)
Colors: Blue, Pink, Purple
Labels: "Standard Drug Discovery" and "Membrane Targeting"
```

---

### 4. MD Simulation Snapshot
**Where:** Features section (Visualization)
**What:** Protein in water box with trajectory
**Size:** 600x400px
**Impact:** ⭐⭐⭐⭐

**How to Get:**
- **VMD screenshot** (if you have MD data)
- **Stock photo:** Search "molecular dynamics simulation"
- **AI Generate:** "Molecular dynamics simulation of protein in water, colorful atoms, scientific visualization style"

---

### 5. Blood Flow Simulation
**Where:** Use Cases (Drug Delivery - Macro scale)
**What:** CFD simulation showing particle flow
**Size:** 600x400px
**Impact:** ⭐⭐⭐

**How to Get:**
- **ParaView screenshot** (if you have OpenFOAM data)
- **Stock photo:** "computational fluid dynamics blood flow"
- **Scientific paper** (with proper attribution)

---

## 📏 Image Size Requirements

| Location | Dimensions | Format | Max Size |
|----------|-----------|--------|----------|
| Hero Background | 1920x1080 | WebP | 300KB |
| Feature Images | 600x400 | WebP | 150KB |
| Use Case Images | 400x300 | WebP | 100KB |
| Icons/Small | 200x200 | PNG | 50KB |
| Composite | 1200x400 | WebP | 200KB |

---

## 💻 HTML Code Templates

### Template 1: Feature Section Image
```html
<div class="feature-item">
    <div class="feature-number">01</div>
    <div class="feature-content">
        <h3>Bidirectional Scale Bridging</h3>

        <!-- ADD IMAGE HERE -->
        <picture class="feature-image">
            <source srcset="assets/images/features/bidirectional-workflow.webp"
                    type="image/webp">
            <img src="assets/images/features/bidirectional-workflow.jpg"
                 alt="Workflow diagram showing bidirectional scale bridging"
                 loading="lazy"
                 width="600"
                 height="400">
        </picture>

        <p>Seamless data conversion in BOTH directions...</p>
    </div>
</div>
```

### Template 2: Use Case Gallery
```html
<div class="use-case-card">
    <div class="use-case-header">
        <h3>🎯 Targeted Drug Delivery</h3>
    </div>

    <!-- ADD IMAGE GALLERY HERE -->
    <div class="use-case-gallery">
        <picture>
            <source srcset="assets/images/use-cases/drug-delivery-macro.webp"
                    type="image/webp">
            <img src="assets/images/use-cases/drug-delivery-macro.jpg"
                 alt="Macro scale: Nanoparticles in blood flow"
                 loading="lazy"
                 width="400"
                 height="300">
        </picture>

        <picture>
            <source srcset="assets/images/use-cases/drug-delivery-meso.webp"
                    type="image/webp">
            <img src="assets/images/use-cases/drug-delivery-meso.jpg"
                 alt="Meso scale: Nanoparticle-cell interaction"
                 loading="lazy"
                 width="400"
                 height="300">
        </picture>

        <picture>
            <source srcset="assets/images/use-cases/drug-delivery-micro.webp"
                    type="image/webp">
            <img src="assets/images/use-cases/drug-delivery-micro.jpg"
                 alt="Micro scale: Antibody-receptor binding"
                 loading="lazy"
                 width="400"
                 height="300">
        </picture>
    </div>

    <p>Simulate liposome transport in blood vessels...</p>
</div>
```

### Template 3: Hero Background Image
```html
<!-- In styles.css -->
.hero {
    background-image:
        linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)),
        url('assets/images/hero/particle-flow-background.webp');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
```

---

## 🎨 CSS Styling for Images

Add to `styles.css`:

```css
/* Feature Images */
.feature-image {
    display: block;
    margin: var(--spacing-lg) 0;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    overflow: hidden;
}

.feature-image img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.3s ease;
}

.feature-item:hover .feature-image img {
    transform: scale(1.05);
}

/* Use Case Gallery */
.use-case-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-sm);
    margin: var(--spacing-md) 0;
}

.use-case-gallery picture {
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-md);
}

.use-case-gallery img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.3s ease;
}

.use-case-gallery picture:hover img {
    transform: scale(1.1);
}

/* Responsive */
@media (max-width: 768px) {
    .use-case-gallery {
        grid-template-columns: 1fr;
    }
}
```

---

## 🔧 Image Optimization Tools

### Free Online Tools:
1. **Squoosh.app** - Google's image optimizer
   - Upload image
   - Choose WebP format
   - Adjust quality to 80%
   - Download

2. **TinyPNG.com** - PNG/JPEG compression
   - Drag and drop
   - Automatic optimization
   - Download compressed

3. **CloudConvert.com** - Format conversion
   - Convert to WebP
   - Batch processing
   - Free tier available

### Command Line (if needed):
```bash
# Convert to WebP
cwebp input.jpg -q 80 -o output.webp

# Resize image
magick input.jpg -resize 600x400 output.jpg
```

---

## 📦 Quick Setup Instructions

### Step 1: Create Folder Structure
```bash
cd landing-page
mkdir -p assets/images/features
mkdir -p assets/images/use-cases
mkdir -p assets/images/hero
mkdir -p assets/images/scales
```

### Step 2: Add Your Images
- Place images in appropriate folders
- Name descriptively: `drug-delivery-macro.jpg`
- Include both WebP and JPG versions

### Step 3: Update HTML
- Copy code templates above
- Replace image paths
- Update alt text descriptions

### Step 4: Test
```bash
# Run local server
python -m http.server 8000
# Open: http://localhost:8000
```

---

## ✅ Implementation Checklist

### This Week:
- [ ] Create assets/images folder structure
- [ ] Generate/source HER2-antibody docking image (PyMOL)
- [ ] Create three-scale comparison (Figma)
- [ ] Add workflow diagram
- [ ] Integrate images into HTML
- [ ] Optimize all images (WebP conversion)

### Next Week:
- [ ] Add MD simulation snapshots
- [ ] Add CFD visualization
- [ ] Create use case image galleries
- [ ] Add hero background image
- [ ] Performance testing

---

## 🚨 Important Notes

### Copyright:
- ✅ Use PDB structures (public domain)
- ✅ Create your own renders
- ✅ Use CC-BY licensed images with attribution
- ❌ Don't use Google Images without checking license
- ❌ Don't use copyrighted scientific figures without permission

### Performance:
- Always include WebP + fallback
- Use `loading="lazy"` for below-fold images
- Compress images before upload
- Target: <200KB per image

### Accessibility:
- Always include meaningful alt text
- Describe what's shown, not just "image"
- Good: "Molecular docking showing antibody binding to HER2 receptor"
- Bad: "Protein image"

---

## 💡 Pro Tips

1. **Start small** - Add 2-3 key images first, then expand
2. **Test performance** - Use Google Lighthouse to check loading speed
3. **Mobile first** - Ensure images look good on small screens
4. **Consistent style** - All images should have similar aesthetic
5. **Add captions** - Brief descriptions help understanding

---

## 📞 Need Help?

**For PyMOL issues:**
- PyMOL Wiki: https://pymolwiki.org/
- Tutorial: Search "PyMOL rendering tutorial"

**For image optimization:**
- Use Squoosh.app (easiest)
- Convert to WebP for ~30% size reduction

**For HTML integration:**
- Copy templates above
- Adjust paths to your images
- Test in browser

---

Ready to add images? Start with the **HER2-antibody docking** (easiest with PyMOL)
and **three-scale comparison** (quick in Figma)! 🎨
