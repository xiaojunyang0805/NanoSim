# NanoSim Landing Page Images

This directory contains scripts to generate scientific visualizations for the NanoSim landing page.

## 📁 Directory Structure

```
images/
├── features/              # Feature section images (600x400px)
├── use-cases/            # Use case examples (400x300px)
├── scales/               # Multi-scale comparisons (1200x400px)
├── hero/                 # Hero section backgrounds (1920x1080px)
├── generate_diagrams.py  # Generate diagrams with matplotlib
├── generate_pymol_images.py # Generate molecular structures
├── convert_to_webp.py    # Convert to WebP format
└── README.md             # This file
```

## 🚀 Quick Start

### Option 1: Generate Diagrams (No special software needed)

```bash
# Install dependencies
pip install matplotlib numpy pillow

# Generate all diagrams
cd landing-page/images
python generate_diagrams.py

# Convert to WebP
python convert_to_webp.py
```

**Generates:**
- ✅ Three-scale comparison diagram
- ✅ Bidirectional workflow diagram
- ✅ Particle flow background
- ✅ Scale icons (macro, meso, micro)

**Time:** ~2 minutes

---

### Option 2: Generate Molecular Structures (Requires PyMOL)

```bash
# Install PyMOL
pip install pymol-open-source
# OR download from: https://pymol.org/

# Generate molecular images
python generate_pymol_images.py

# Convert to WebP
python convert_to_webp.py
```

**Generates:**
- ✅ HER2-antibody complex (2 views)
- ✅ Protein-ligand docking example
- ✅ Membrane protein visualization

**Time:** ~5 minutes (includes downloading PDB structures)

---

### Option 3: Download Pre-made Images

If you don't want to generate images, you can:

1. **Use stock photos** from:
   - Science Photo Library
   - Shutterstock (search: "molecular docking")
   - Unsplash (search: "science visualization")

2. **Use AI-generated images** from:
   - Midjourney
   - DALL-E 3
   - Stable Diffusion

3. **Use scientific figures** from open-access papers:
   - PLoS ONE (CC-BY license)
   - Frontiers journals
   - Always provide attribution

---

## 📊 Image Specifications

### Size Requirements

| Type | Dimensions | Format | Max Size | Purpose |
|------|-----------|--------|----------|---------|
| Hero BG | 1920x1080 | WebP | 300KB | Background image |
| Feature | 600x400 | WebP | 150KB | Feature illustrations |
| Use Case | 400x300 | WebP | 100KB | Example scenarios |
| Icons | 200x200 | PNG | 50KB | Scale indicators |
| Composite | 1200x400 | WebP | 200KB | Multi-panel comparisons |

### Color Scheme

Use NanoSim brand colors:
- **Macro Blue:** `#3b82f6`
- **Meso Purple:** `#8b5cf6`
- **Micro Pink:** `#ec4899`
- **Primary:** `#2563eb`

---

## 🎨 Generated Images

### Diagrams (matplotlib)

1. **three-scale-comparison.png** (1200x400px)
   - Three panels showing macro, meso, micro scales
   - Visual representation of each scale
   - Color-coded by scale type

2. **bidirectional-workflow.png** (1000x800px)
   - Standard workflow (docking-first)
   - Membrane workflow (MD-first)
   - Shows both paradigms

3. **particle-flow-background.png** (1920x1080px)
   - Subtle particle flow visualization
   - For hero section background
   - Low opacity for text readability

4. **Scale icons** (200x200px each)
   - macro-icon.png
   - meso-icon.png
   - micro-icon.png

### Molecular Structures (PyMOL)

1. **her2-antibody-docking.png** (1200x800px)
   - HER2 receptor with trastuzumab antibody
   - Shows binding interface
   - Relevant to NanoSim test case

2. **her2-antibody-side-view.png** (1200x800px)
   - Alternative view of same complex
   - Better shows overall structure

3. **protein-ligand-docking.png** (1200x800px)
   - Generic docking example
   - HIV protease with inhibitor
   - Shows binding pocket clearly

4. **membrane-protein.png** (1200x800px)
   - Membrane protein visualization
   - Shows meso-scale context

---

## 💻 Script Details

### generate_diagrams.py

**Purpose:** Create scientific diagrams and visualizations

**Dependencies:**
```bash
pip install matplotlib numpy
```

**Functions:**
- `generate_three_scale_comparison()` - Multi-scale diagram
- `generate_workflow_diagram()` - Bidirectional workflows
- `generate_particle_flow()` - Hero background
- `generate_scale_icons()` - Scale indicator icons

**Customization:**
Edit these variables in the script:
```python
DPI = 300                    # Image resolution
COLOR_MACRO = "#3b82f6"      # Macro scale color
COLOR_MESO = "#8b5cf6"       # Meso scale color
COLOR_MICRO = "#ec4899"      # Micro scale color
```

---

### generate_pymol_images.py

**Purpose:** Generate molecular structure visualizations

**Dependencies:**
```bash
pip install pymol-open-source
# OR download from https://pymol.org/
```

**Functions:**
- `generate_her2_antibody_docking()` - HER2 complex
- `generate_protein_ligand_complex()` - Generic docking
- `generate_membrane_protein()` - Membrane protein

**Customization:**
Edit these variables:
```python
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 800
DPI = 300
```

**Note:** Requires internet connection to download PDB structures

---

### convert_to_webp.py

**Purpose:** Convert PNG/JPG images to WebP for optimization

**Dependencies:**
```bash
pip install pillow
```

**Features:**
- Converts all PNG/JPG files in directory
- Preserves original files
- Shows file size savings
- Typically 30% smaller than PNG

**Usage:**
```bash
python convert_to_webp.py
```

---

## 🔧 Troubleshooting

### PyMOL Installation Issues

**Problem:** `pip install pymol-open-source` fails

**Solutions:**
1. Download pre-built binary from https://pymol.org/
2. Use conda: `conda install -c conda-forge pymol-open-source`
3. Skip PyMOL and use diagrams only

---

### Matplotlib Display Issues

**Problem:** "No display found" error

**Solution:** Add at the top of script:
```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
```

---

### WebP Conversion Issues

**Problem:** Pillow doesn't support WebP

**Solution:** Install with WebP support:
```bash
pip uninstall pillow
pip install pillow --global-option="build_ext" --global-option="--enable-webp"
```

Or use online tools:
- Squoosh.app
- CloudConvert.com

---

## 📝 Integration into Landing Page

### HTML Template

```html
<picture>
  <source srcset="assets/images/scales/three-scale-comparison.webp" type="image/webp">
  <source srcset="assets/images/scales/three-scale-comparison.png" type="image/png">
  <img src="assets/images/scales/three-scale-comparison.png"
       alt="Comparison of macro, meso, and micro simulation scales"
       loading="lazy"
       width="1200"
       height="400">
</picture>
```

### Where to Use Images

1. **Hero Section**
   - Background: `hero/particle-flow-background.webp`
   - Opacity: 0.1-0.2 (very subtle)

2. **Features Section**
   - Feature 1: `features/bidirectional-workflow.webp`
   - Add below feature text

3. **Use Cases**
   - Drug Delivery: `use-cases/her2-antibody-docking.webp`
   - Create gallery with 3 images per use case

4. **New Section** (Optional)
   - Add "How It Works" section
   - Use: `scales/three-scale-comparison.webp`

---

## ✅ Checklist

### Initial Setup
- [ ] Install Python dependencies: `pip install matplotlib numpy pillow`
- [ ] Install PyMOL (optional): `pip install pymol-open-source`
- [ ] Create subdirectories (done automatically by scripts)

### Generate Images
- [ ] Run `python generate_diagrams.py`
- [ ] Run `python generate_pymol_images.py` (if PyMOL available)
- [ ] Run `python convert_to_webp.py`

### Optimization
- [ ] Verify all WebP files created
- [ ] Check file sizes (should be <200KB each)
- [ ] Test images display correctly

### Integration
- [ ] Add images to HTML
- [ ] Update alt text descriptions
- [ ] Test on different screen sizes
- [ ] Run Google Lighthouse performance test

---

## 📊 Expected Results

After running all scripts, you should have:

```
images/
├── scales/
│   ├── three-scale-comparison.png (+ .webp)
│   ├── macro-icon.png (+ .webp)
│   ├── meso-icon.png (+ .webp)
│   └── micro-icon.png (+ .webp)
├── features/
│   └── bidirectional-workflow.png (+ .webp)
├── hero/
│   └── particle-flow-background.png (+ .webp)
└── use-cases/
    ├── her2-antibody-docking.png (+ .webp)
    ├── her2-antibody-side-view.png (+ .webp)
    ├── protein-ligand-docking.png (+ .webp)
    └── membrane-protein.png (+ .webp)
```

**Total Images:** 12 PNG + 12 WebP = 24 files
**Total Size:** ~2-3 MB (before WebP), ~1.5-2 MB (after WebP)

---

## 🎯 Next Steps

1. **Generate core images** (diagrams - no PyMOL needed)
2. **Convert to WebP** for optimization
3. **Test locally** in landing page
4. **Add to Git** and deploy
5. **Measure impact** with analytics

---

## 📞 Support

**Issues with scripts?**
- Check Python version: `python --version` (need 3.8+)
- Check dependencies: `pip list`
- Read error messages carefully

**Need different images?**
- Edit script functions
- Adjust colors, sizes, layouts
- Re-run scripts

**Questions?**
- See `IMAGE_STRATEGY.md` for detailed guidelines
- See `IMAGE_QUICK_GUIDE.md` for quick reference

---

**Last Updated:** October 29, 2025
**Scripts Version:** 1.0
**Status:** Ready to use
