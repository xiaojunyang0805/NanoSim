# NanoSim Landing Page Image Strategy

**Date:** October 29, 2025
**Purpose:** Plan visual content to enhance landing page engagement and clarity

---

## 🎯 Image Strategy Overview

### Goals:
1. **Educate** - Help visitors understand complex simulation concepts
2. **Engage** - Make the page visually appealing and professional
3. **Illustrate** - Show real examples of what NanoSim does
4. **Build Trust** - Demonstrate scientific credibility

### Image Style:
- **Scientific but accessible** - Not overly technical
- **High quality** - Professional, crisp, well-lit
- **Consistent aesthetic** - Similar color schemes and styles
- **Optimized** - Fast loading (WebP format, properly sized)

---

## 📸 Image Placement Plan

### 1. Hero Section - Background or Side Visual
**Current:** Scale boxes diagram
**Addition:** Background visualization (subtle, non-distracting)

**Recommended Images:**
- **Option A:** Abstract particle flow visualization
  - Shows particles moving through different scales
  - Blue to purple to pink gradient
  - Blurred/transparent to not compete with text

- **Option B:** Molecular structure grid
  - Grid of different scale visualizations
  - Macro (blood vessels), Meso (membrane), Micro (molecules)
  - Subtle opacity as background

**Placement:** `background-image` on `.hero` section
**Size:** 1920x1080px (Full HD banner)
**Format:** WebP with JPEG fallback

---

### 2. Problem Section - Visual Icons/Illustrations
**Current:** Emoji icons (⚠️, 📈, 💰, 🔧)
**Upgrade:** Custom illustrations or scientific images

**Recommended Images:**
- **Manual Data Transfer:** Screenshot of different simulation software UIs
- **Steep Learning Curves:** Multiple software logos/interfaces
- **High Costs:** Commercial software pricing comparisons
- **No Standard Workflow:** Diagram of fragmented workflow

**Placement:** Replace emoji with actual images in `.problem-card`
**Size:** 200x200px (icon size)
**Format:** PNG with transparency or SVG

---

### 3. Solution Section - Feature Demonstrations
**Current:** Emoji icons (🔄, 🔗, 🤖, 🌍)
**Add:** Actual screenshots or diagrams

**Recommended Images:**

#### Card 1: Adaptive Workflows
- **Image:** Side-by-side comparison of two workflow diagrams
- **Shows:** Docking-first vs MD-first paths
- **Style:** Clean diagram with arrows and scale indicators

#### Card 2: Unified Interface
- **Image:** Mock-up or wireframe of NanoSim interface
- **Shows:** Single dashboard controlling all three scales
- **Style:** Professional UI screenshot or design mockup

#### Card 3: Intelligent Routing
- **Image:** Decision tree or flowchart visualization
- **Shows:** How platform selects optimal workflow
- **Style:** Infographic style, clear and colorful

#### Card 4: Open Source
- **Image:** GitHub repository screenshot or open source community
- **Shows:** Active development, community contributions
- **Style:** Real GitHub screenshot or contributor graph

**Placement:** Above or beside text in `.solution-card`
**Size:** 400x300px (landscape)
**Format:** WebP

---

### 4. Features Section - Detailed Visualizations
**Current:** Feature numbers and text only
**Add:** Large feature illustrations

**Recommended Images:**

#### Feature 1: Bidirectional Scale Bridging
- **Image:** Detailed workflow diagram with data flow
- **Shows:** Data conversion between scales (arrows, file formats)
- **Example:** PDB → GROMACS topology → Vina input
- **Size:** 600x400px

#### Feature 2: Docker Architecture
- **Image:** Docker container diagram
- **Shows:** OpenFOAM, GROMACS, AutoDock containers
- **Style:** Technical architecture diagram
- **Size:** 600x400px

#### Feature 3: Visualization
- **Image:** 3D molecular dynamics trajectory
- **Shows:** Protein-ligand complex with trajectory overlay
- **Style:** Rendered 3D scientific visualization
- **Size:** 600x400px

#### Feature 4: Workflow Library
- **Image:** Gallery of pre-built workflow templates
- **Shows:** Different use case examples (thumbnails)
- **Style:** Grid layout of workflow cards
- **Size:** 600x400px

**Placement:** Beside or below text in `.feature-item`
**Format:** WebP

---

### 5. Use Cases Section - Real-World Examples
**Current:** Text descriptions only
**Add:** Visual representations of each use case

**Recommended Images:**

#### Use Case 1: Targeted Drug Delivery 🎯
**Image Sequence (3 images):**

1. **Macro Scale:** Blood vessel with flowing nanoparticles
   - Source: Biomedical illustration or CFD simulation screenshot
   - Shows: Red blood cells and liposomes in blood flow
   - Size: 400x300px

2. **Meso Scale:** Nanoparticle approaching tumor cell
   - Source: Molecular dynamics snapshot or scientific illustration
   - Shows: Liposome near cell membrane with receptors
   - Size: 400x300px

3. **Micro Scale:** Antibody-HER2 receptor binding
   - Source: Protein-protein docking result (PDB visualization)
   - Shows: Molecular structure with binding site highlighted
   - Size: 400x300px

#### Use Case 2: Vaccine Delivery 💉
**Image Sequence:**
1. Lipid nanoparticle structure (cross-section)
2. Cell membrane penetration (MD simulation)
3. mRNA release mechanism (molecular view)

#### Use Case 3: Gene Therapy 🧬
**Image Sequence:**
1. Viral vector in tissue (macro visualization)
2. Vector-cell interaction (meso scale)
3. DNA-protein complex (atomic detail)

**Placement:** Create image carousel or grid in `.use-case-card`
**Format:** WebP, optimized for web

---

## 📊 Specific Image Recommendations

### Category A: Molecular Docking Images
**Source Options:**
1. **Protein Data Bank (PDB)** - Download real structures
2. **PyMOL/ChimeraX screenshots** - Render your own
3. **Scientific publications** (with permission/open access)
4. **Stock science photos** - Shutterstock, iStock (paid)

**Recommended Specific Images:**
- **Protein-ligand complex** (e.g., HER2 receptor with antibody)
- **Binding pocket visualization** (surface representation)
- **Multiple docking poses** (overlaid structures)

**Tools to Create:**
- PyMOL: `fetch 3pp0` (HER2-trastuzumab complex)
- ChimeraX: Load PDB, render high-quality images
- VMD: Molecular graphics and trajectory visualization

---

### Category B: Molecular Dynamics Images
**Recommended Visualizations:**
- **Trajectory snapshot** - Protein in solvent box
- **RMSD/RMSF plots** - Show stability metrics
- **Hydrogen bond network** - Interaction visualization
- **Membrane system** - Lipid bilayer with protein

**Tools to Create:**
- VMD with Timeline plugin
- PyMOL with MD trajectory
- GROMACS built-in plotting tools (xmgrace)

---

### Category C: Computational Fluid Dynamics
**Recommended Visualizations:**
- **Velocity field** - Colored vectors showing flow
- **Particle trajectories** - Streamlines through vessels
- **Concentration map** - Heat map of nanoparticle distribution
- **Tumor vasculature** - Blood vessel network 3D rendering

**Tools to Create:**
- ParaView (OpenFOAM output visualization)
- OpenFOAM native tools
- Scientific illustration software

---

### Category D: Multi-Scale Comparison
**Composite Images Showing All Three Scales:**

**Image 1: "The NanoSim Pipeline"**
- Three panels side-by-side
- Left: Tissue-level (mm scale)
- Middle: Cell-level (μm scale)
- Right: Molecular-level (nm scale)
- Arrows connecting them
- Size: 1200x400px

**Image 2: "Scale Comparison"**
- Zooming effect showing scales
- Start with tumor tissue
- Zoom to cell membrane
- Zoom to molecular binding
- Infographic style
- Size: 800x600px

---

## 🎨 Image Sourcing Strategy

### Option 1: Create Your Own (Recommended)
**Pros:** Authentic, customizable, copyright-free
**Cons:** Time-consuming, requires software

**Steps:**
1. Download PDB structures (free from rcsb.org)
2. Visualize in PyMOL/ChimeraX (free for academic)
3. Render high-quality images
4. Add annotations in Figma/PowerPoint

**Example Workflow:**
```python
# PyMOL script for protein-ligand complex
fetch 3pp0  # HER2-trastuzumab
remove solvent
color cyan, chain A
color magenta, chain H+L
show surface, chain A
set transparency, 0.5
bg_color white
ray 1920, 1080
png output.png, dpi=300
```

---

### Option 2: Scientific Stock Images
**Sources:**
- **Science Photo Library** (paid, high quality)
- **Shutterstock** (science category)
- **Getty Images** (scientific collection)
- **Adobe Stock**

**Search Terms:**
- "molecular docking"
- "protein structure"
- "molecular dynamics simulation"
- "nanoparticle drug delivery"
- "computational fluid dynamics"
- "blood flow simulation"

**Cost:** ~$10-50 per image
**License:** Extended for web use

---

### Option 3: Open Access Publications
**Sources:**
- **PLoS ONE** (CC-BY license)
- **Nature Communications** (some open access)
- **Frontiers journals** (CC-BY license)
- **bioRxiv preprints**

**Process:**
1. Search for relevant papers
2. Check license (must be CC-BY or similar)
3. Download figures from paper
4. Credit appropriately in image caption or footer

**Example Papers:**
- Drug delivery simulations
- Molecular docking studies
- MD simulation of membrane proteins

---

### Option 4: AI-Generated Scientific Illustrations
**Tools:**
- **Midjourney** - Artistic scientific illustrations
- **DALL-E 3** - Precise scientific concepts
- **Stable Diffusion** - Open source generation

**Prompts for Scientific Images:**
```
"Scientific illustration of protein-ligand docking, molecular structure
with binding site, professional medical textbook style, clean background"

"Computational fluid dynamics simulation of blood flow with nanoparticles,
colorful velocity field, scientific visualization style"

"Molecular dynamics simulation showing protein in lipid membrane,
cross-section view, scientific rendering, professional quality"
```

**Pros:** Quick, customizable, unique
**Cons:** May not be scientifically accurate, requires refinement

---

## 📐 Technical Specifications

### Image Formats:
- **Primary:** WebP (modern browsers, ~30% smaller)
- **Fallback:** JPEG (universal compatibility)
- **Transparent:** PNG (icons, overlays)
- **Vector:** SVG (diagrams, illustrations)

### Optimization:
- **Max file size:** 200KB per image (compressed)
- **Resolution:** 2x for retina displays
- **Lazy loading:** Implement for below-fold images
- **Responsive:** Multiple sizes for different viewports

### Example HTML Implementation:
```html
<picture>
  <source srcset="images/docking-example.webp" type="image/webp">
  <source srcset="images/docking-example.jpg" type="image/jpeg">
  <img src="images/docking-example.jpg"
       alt="Molecular docking of ligand to protein binding site"
       loading="lazy"
       width="600"
       height="400">
</picture>
```

---

## 🗂️ Suggested File Structure

```
landing-page/
└── assets/
    └── images/
        ├── hero/
        │   ├── background-particles.webp
        │   └── background-particles.jpg
        ├── scales/
        │   ├── macro-blood-flow.webp
        │   ├── meso-membrane.webp
        │   └── micro-docking.webp
        ├── features/
        │   ├── bidirectional-workflow.webp
        │   ├── docker-architecture.webp
        │   ├── visualization-example.webp
        │   └── workflow-library.webp
        ├── use-cases/
        │   ├── drug-delivery-macro.webp
        │   ├── drug-delivery-meso.webp
        │   ├── drug-delivery-micro.webp
        │   ├── vaccine-delivery.webp
        │   └── gene-therapy.webp
        ├── icons/
        │   └── [custom icons if needed]
        └── composite/
            ├── three-scales-comparison.webp
            └── nanosim-pipeline.webp
```

---

## ✅ Implementation Checklist

### Phase 1: High Priority Images
- [ ] Hero background (subtle particle flow)
- [ ] Three-scale comparison (macro-meso-micro)
- [ ] Docking example (HER2-antibody)
- [ ] MD simulation snapshot
- [ ] CFD flow visualization

### Phase 2: Feature Enhancements
- [ ] Bidirectional workflow diagram
- [ ] Docker architecture illustration
- [ ] 3D trajectory visualization
- [ ] Workflow template gallery

### Phase 3: Use Case Visuals
- [ ] Targeted drug delivery sequence (3 images)
- [ ] Vaccine delivery visualization
- [ ] Gene therapy example

### Phase 4: Polish
- [ ] Optimize all images (WebP conversion)
- [ ] Add lazy loading
- [ ] Create responsive versions
- [ ] Test loading performance

---

## 🎯 Priority Recommendations

### Must Have (Week 1):
1. ⭐ **Three-scale comparison image** (hero or features section)
   - Shows macro → meso → micro visually
   - Single composite image, easiest to understand

2. ⭐ **HER2-antibody docking visualization** (use case section)
   - Real scientific example
   - Directly relevant to your test case

3. ⭐ **Workflow diagram** (features section)
   - Shows bidirectional capability
   - Can be created in Figma quickly

### Should Have (Week 2):
4. MD trajectory snapshot
5. CFD blood flow simulation
6. Docker architecture diagram

### Nice to Have (Future):
7. Custom icon set (replacing emojis)
8. Interactive 3D molecular viewer
9. Animated transitions between scales

---

## 💡 Quick Start Guide

### Immediate Action Plan:

1. **Download PDB Structure** (5 minutes)
   ```
   Visit: https://www.rcsb.org/structure/3pp0
   Download: PDB format
   ```

2. **Visualize with PyMOL** (15 minutes)
   ```
   Load structure
   Style as surface + cartoon
   Add colors (cyan/magenta)
   Render high-quality image
   ```

3. **Create in Figma** (30 minutes)
   ```
   Three-panel layout
   Add downloaded images
   Add labels and arrows
   Export as WebP
   ```

4. **Integrate into Landing Page** (15 minutes)
   ```
   Add to /assets/images/
   Update HTML <picture> tags
   Add alt text
   Test loading
   ```

**Total Time:** ~1 hour for first professional images!

---

## 📝 Image Attribution

If using external sources, add attribution in footer:

```html
<div class="image-credits">
  <p>Scientific visualizations: Created using PyMOL, structures from
  RCSB Protein Data Bank. Workflow diagrams: Original work by NanoSim team.</p>
</div>
```

---

## 🚀 Next Steps

1. **Review this strategy** - Prioritize which images to create first
2. **Choose creation method** - DIY, stock, or AI-generated
3. **Create image folder** - Set up file structure
4. **Generate/source 3-5 key images** - Focus on high-priority items
5. **Integrate into HTML** - Update landing page code
6. **Optimize and test** - Ensure fast loading

---

**Ready to start?** I recommend beginning with the **three-scale comparison image**
and **HER2-antibody docking example** as they're most impactful and directly
relevant to your platform! 📸✨

---

**Author:** NanoSim Team
**Last Updated:** October 29, 2025
**Status:** Ready for Implementation
