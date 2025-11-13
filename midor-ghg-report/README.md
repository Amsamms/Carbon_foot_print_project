# MIDOR Refinery GHG Inventory Report (Base Year 2025)

## Overview
This is a self-contained web-based GHG (Greenhouse Gas) inventory report for MIDOR Refinery, conformant with ISO 14064-1:2018 and GHG Protocol Corporate Standard.

## Contents
- `index.html` - Main report (20+ pages when printed to PDF)
- `assets/css/styles.css` - Styles with A4 print-ready formatting
- `assets/js/data.js` - Dummy emissions data
- `assets/js/charts.js` - ECharts visualization functions
- `assets/img/` - Images and maps
- `MIDOR activities.xlsx` - Source activity data

## How to View
1. Open `index.html` in a modern web browser (Chrome, Firefox, Edge)
2. Charts will render automatically using ECharts
3. For best results, use Chrome or Edge

## How to Print to PDF
1. Open `index.html` in Chrome or Edge
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Select "Save as PDF" as the destination
4. Set:
   - Paper size: A4
   - Margins: Default
   - Scale: 100%
   - Background graphics: ON (to preserve colors and charts)
5. Click "Save"

The resulting PDF should be 20+ pages with:
- Cover page
- 12 main sections
- 5 appendices
- Interactive charts rendered as crisp SVG graphics

## Data Status
⚠️ **IMPORTANT**: All data in this report are DUMMY PLACEHOLDERS marked "to be replaced". Before official use:
1. Replace all emission factors with actual values
2. Update activity data from MIDOR operations
3. Obtain real electricity grid emission factors
4. Collect actual product sales volumes
5. Run calculations with real data

## Updating for Next Year
1. Update `MIDOR activities.xlsx` with new activity data
2. Run the Python data allocation script to regenerate `data.js`
3. Update year references (2025 → 2026) in `index.html`
4. Print to PDF and distribute

## Technical Details
- **Standards**: ISO 14064-1:2018, GHG Protocol Corporate Standard
- **GWP Set**: IPCC AR6 (100-year)
- **Scopes**: Scope 1 (Direct), Scope 2 (Electricity), Scope 3 (Cat. 7 & 11)
- **Charts**: ECharts 5.4.3 with SVG renderer
- **Print Format**: A4 with CSS Paged Media

## Authors
- Ahmed Mohamed Sabri
- Amr Hassan Abu Mady
- Tareq Mohamed Salama
- Ahmed Adel Mabrouk

## Report Generated
November 2025 | Document Version 1.0
