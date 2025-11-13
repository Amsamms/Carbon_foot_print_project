# MIDOR GHG Inventory — MAGAZINE QUALITY EDITION ✨

## 🎨 What's Different?

This is a **professional magazine-style** redesign of the MIDOR GHG inventory report, inspired by Adobe InDesign layouts.

### Key Features:
- ✅ **Landscape A4** orientation (297mm × 210mm)
- ✅ **Minimal margins** (10mm) - maximum content density
- ✅ **Full-bleed backgrounds** with overlay effects
- ✅ **Multi-column text layouts** (2-3 columns)
- ✅ **Dense data visualizations** (charts, infographics, cards)
- ✅ **Colored callout boxes** (orange circles, blue sidebars)
- ✅ **Magazine-style typography** (mix of sans-serif and serif)
- ✅ **No wasted white space** - every mm counts!
- ✅ **Professional color-coded sections**

## 📁 Files

- `index-magazine.html` - Main magazine-style report
- `assets/css/styles-magazine.css` - Magazine layout CSS
- `assets/js/data.js` - Emissions data
- `assets/img/MIDPR_map.PNG` - Site map (full-bleed cover)

## 🖥️ How to View

**Option 1: Direct Open**
```bash
cd /home/amsamms/projects/Carbon_foot_print_project/midor-ghg-report
xdg-open index-magazine.html
```

**Option 2: Browser**
Open `index-magazine.html` in Chrome or Firefox

## 🖨️ Print to PDF (RECOMMENDED)

1. Open `index-magazine.html` in **Chrome** (best results)
2. Press `Ctrl+P` or `Cmd+P`
3. **CRITICAL Settings:**
   - **Paper size:** A4 Landscape (297mm × 210mm)
   - **Margins:** Custom → Set to **Minimum** or **None**
   - **Scale:** 100%
   - **Background graphics:** ✅ ON (MUST enable!)
   - **Headers and footers:** ❌ OFF (optional)
4. **Destination:** Save as PDF
5. Click **Save**

### Expected Result:
- 6-7 pages of **dense, beautiful** magazine-quality content
- Full-color charts, diagrams, data cards
- Professional typography and layouts
- Ready for printing or distribution

## 📊 Page Breakdown

1. **Cover** - Full-bleed refinery map with title overlay
2. **Executive Summary** - Hand-drawn heading, orange callouts, scope diagram, sidebar
3. **Introduction** - 2-column spread with background, boundaries, methodology
4. **Scope 1** - Charts + data cards grid layout
5. **Scope 2 & 3** - Side-by-side comparison with tables and charts
6. **Mitigation Roadmap** - Timeline with colored year badges
7. **Credits & Standards** - Team info and conformance details

## 🎯 Design Philosophy

This report follows **magazine/brochure design principles**:
- Every page is **visually rich** with data, charts, text, colors
- **No boring white space** - content fills the page
- **Dense information architecture** - maximum data per square mm
- **Visual hierarchy** - large numbers, colored blocks, section badges
- **Professional aesthetics** - looks like it was designed in InDesign

## 🔄 Updating for Next Year

1. Update `MIDOR activities.xlsx` with 2026 data
2. Regenerate `data.js` with Python script
3. Replace "2025" with "2026" in `index-magazine.html`
4. Update cover year badge
5. Print to PDF

## 🆚 Comparison: Old vs New

**Old Design (index.html):**
- Portrait A4, lots of white space
- Basic tables, minimal charts
- Looks like "HTML printed to PDF"
- 20+ pages with sparse content

**New Design (index-magazine.html):**
- Landscape A4, minimal margins
- Dense charts, data cards, infographics
- Looks like **professional magazine**
- 6-7 pages packed with content

## 💡 Pro Tips

- Use **Chrome** for best print results
- **ALWAYS enable background graphics** when printing
- Set margins to **minimum** for full-bleed effect
- View on **large screen** for best experience
- For presentations: print to PDF, then share the PDF

## 📝 Future Enhancements

To add more pages:
1. Copy a `.page` div structure
2. Use grid layouts: `grid-2col`, `grid-3col`, `grid-asymmetric`
3. Add charts with ECharts (see existing examples)
4. Use colored callout boxes and data cards
5. Keep fonts small (8-10pt) to fit more content

---

**Created:** November 2025
**Version:** 1.0 Magazine Edition
**Authors:** Ahmed Mohamed Sabri, Amr Hassan Abu Mady, Tareq Mohamed Salama, Ahmed Adel Mabrouk
