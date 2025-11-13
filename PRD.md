Project: MIDOR Refinery — Organizational GHG Inventory (Base Year 2025)
Authors (credits page): Ahmed Mohamed Sabri, Amr Hassan Abu Mady, Tareq Mohamed Salama, Ahmed Adel Mabrouk
Standards: ISO 14064-1:2018 (org-level), ISO 14069:2013 (guidance), GHG Protocol Corporate Standard
Language: English
Assurance: None (for now; include placeholder section)
Reporting approach: Operational Control
Scopes in scope:

Scope 1 (all direct sources in refinery boundary)

Scope 2 (purchased electricity only; suppliers: MIDELEC and National Grid)

Scope 3 (Category 11 – Use of sold products only)
GWP set: IPCC AR6, 100-year
Map image placeholder: assets/img/MIDPR_map.PNG (geographical hero image)
Activities list: parse and use MIDOR activities.xlsx to drive categories/sections/sub-charts

0) Output & packaging

Produce a self-contained web project:

index.html

assets/css/styles.css

assets/js/charts.js

assets/img/ (placeholders for icons, hero images, map)

The HTML must be A4 print-ready (CSS Paged Media): margins, headers/footers with page numbers, automatic page breaks, high-DPI/SVG charts that print crisply.

No interactive dashboards are required; charts should render SVG (ECharts renderer = SVG). If any interactivity is present, ensure graceful, nice-looking print.

Provide figure/table captions and cross-references.

Ensure 20+ pages when printed to PDF. Keep pages aesthetically dense but readable.

1) Visual design (match the “beautiful unstructured report” vibe)

Use a vague/soft background image on section openers (hero banners) with high-contrast, modern sans typography (clean sustainability look).

Palette: calm, modern sustainability (mix of teals/blues with warm accent). Use consistent color coding for Scopes (S1=amber, S2=blue, S3=navy), and for facilities.

Components to mimic the examples:

“Organizational boundaries” tiles with icons (Farming/Manufacturing style → adapt to refinery complexes).

Big segment ribbons for Scope 1/2/3 with their shares.

Timeline/roadmap row for targets & initiatives.

Full-bleed banner images with semi-transparent overlays for key messages.

All charts must be vector/SVG and print-legible.

2) Data model (dummy but realistic)

Total dummy figures (refinery scale):

Scope 1: 1.80 MtCO₂e

Scope 2: 0.25 MtCO₂e (split between MIDELEC and National Grid placeholders)

Scope 3 (Cat. 11 use of sold fuels): 35.0 MtCO₂e

Within each Scope, sub-allocate using the activities parsed from MIDOR activities.xlsx. If a listed activity doesn’t map 1:1, assign a reasonable share and label as “dummy placeholder (to be replaced)”.

Electricity grid factors: create two placeholders (to be replaced later):

EF_MIDELEC = 0.55 tCO₂e/MWh (dummy)

EF_NationalGrid = 0.60 tCO₂e/MWh (dummy)
Show location-based results prominently; include a small note that market-based can be added if instruments become available.

Intensity metrics to calculate and chart:

tCO₂e / kton crude input

tCO₂e / GJ fired duty
Provide dummy denominators that yield believable values; display equations and placeholders clearly.

3) Methods register & equations (show the audit trail)

Create a compact “Methods Register” table auto-generated from activities, containing per-source:

Method type (e.g., fuel gas carbon balance; CH₄/N₂O defaults; flares with DRE 99.9% and CH₄ slip; mobile by fuel; process units by mass balance or stack test placeholders).

Activity data source (meters, DCS/PI, invoices, lab GC).

Emission factors (reference placeholders: API Compendium/EPA/DEFRA/IPCC).

Equations (explicit):

CO₂ = Fuel × Carbon_fraction × (44/12) × Oxidation_factor

CH₄ & N₂O = Fuel × EF_gas × GWP (AR6)

Scope 2 = ∑(MWh_supplier × EF_supplier)

Scope 3 Cat.11 = ∑(Product_sold × Use-phase EF_product)

Gases: CO₂, CH₄, N₂O, (HFCs/PFCs/SF₆/NF₃ if any). Convert all to CO₂e using AR6 100-yr GWPs; display a small GWP table with source/date.

4) Structure & page plan (minimum 20 pages)

Cover

Title, base year, hero image, MIDOR logo, subtle background.

Tagline: “Organizational GHG Inventory — Base Year 2025 (Operational Control)”.

Page 2 — About this Report

Standards, boundary summary, consolidation approach, intended users, disclaimer (no assurance yet).

Team credits: “Prepared by Ahmed Mohamed Sabri, Amr Hassan Abu Mady, Tareq Mohamed Salama, Ahmed Adel Mabrouk.”

Section 1 — MIDOR at a Glance (2–3 pages)

Map tile (MIDPR_map.PNG) with site footprint.

Throughput (160,000 BPSD), main products (LPG, Gasoline, Jet/Kerosene (exported), Diesel (ULSD portion exported), Coke, Sulfur), electricity sources (MIDELEC primary, National Grid backup).

Organizational chart tiles for complexes/areas (e.g., Crude/Vacuum, CCR/Platformer, Penex/Isomerization, Hydrotreating, H₂ Plant/SMR, Sulfur/Amine, Utilities, Flare/Offsites, Marine Terminal, Tank Farm). Use icons.

Section 2 — Principles & Governance (1–2 pages)

Relevance, Completeness, Consistency, Accuracy, Transparency.

Roles & responsibilities (Inventory Management Plan summary).

Data flow schematic.

Section 3 — Boundaries (2 pages)

Organizational boundary (Operational Control) visual tiles.

Operational boundary: Scope 1, 2, 3—what’s in/out.

Explicit note: Scope 2 = purchased electricity only; Scope 3 = Category 11 only.

Exclusions placeholder list.

Section 4 — Methods & Factors (2–3 pages)

Methods register table and icons by source type.

AR6 GWP table, electricity EF placeholders.

Missing data and QC/QA notes.

Section 5 — Results Overview (2 pages)

Big “chevrons” showing shares: Scope 1, 2, 3 (like your example).

Total footprint callout and year badge (2025).

Section 6 — Scope 1 Details (3–4 pages)

Stacked bars/pie by category (stationary combustion, flares, process, fugitives, mobile, wastewater, F-gases—use only categories present in the Excel).

Facility-level mini-charts and a heat-map tile grid to show top sources.

Gas split (CO₂, CH₄, N₂O).

Section 7 — Scope 2 Details (1–2 pages)

Supplier split (MIDELEC vs National Grid) with EF note.

Location-based total highlighted; market-based placeholder note.

Section 8 — Scope 3 (Cat. 11 Use of Sold Products) (2–3 pages)

Product slate tiles (gasoline, diesel, jet/kerosene, LPG, fuel oil, coke, asphalt, sulfur—use what’s in Excel).

Waterfall from sales to use-phase CO₂e with EF note.

Section 9 — Intensities & Trends (1–2 pages)

Two KPI cards with sparklines: tCO₂e/kton crude; tCO₂e/GJ fired duty.

Explain denominators and caveats.

Section 10 — Base Year & Recalculation Policy (1 page)

2025 = Base year; list triggers for restatement; simple flowchart.

Section 11 — Uncertainty & Quality (2 pages)

Table with ±% (95% CI) by category (use reasoned dummy values).

Qualitative ratings (H/M/L) and improvement actions (e.g., GC frequency for fuel gas, flare flow metering, LDAR upgrades).

Section 12 — Mitigation Roadmap (1–2 pages)

Attractive ribbon/timeline: energy management system, PV capacity, waste-to-energy, solar water heaters, EV/elec fleet, real-time monitoring (use your example style with icons).

Placeholders for estimated tCO₂e abatement (not netted against totals).

Appendices

A: Glossary & abbreviations.

B: Equations & factors (with “to be replaced” tags).

C: Activity-to-method mapping (from Excel).

D: Data sources & QC checks.

E: “For future assurance” placeholder page for adding a verifier statement.

5) Charts & components (use ECharts, SVG)

Library: ECharts with SVG renderer for print sharpness.

Provide reusable functions in assets/js/charts.js:

makeChevronShare(scopeData)

makeStackedByCategory(data)

makeSupplierSplit(data)

makeHeatTiles(facilityData)

makeWaterfall(series)

makeSparkKPI(series)

Ensure charts auto-fit A4 width, with font sizes bumped for print (min 9–10pt).

Provide fallback <img> (base64 PNG) tags if JS disabled (pre-render small thumbnails).

6) Accessibility & print rules

High contrast ratios, alt text on all figures.

CSS: @page { size: A4; margin: 16mm; } fixed header/footer with page number, doc title, and section.

Force page breaks at logical section boundaries; avoid orphan headings.

7) Dummy data generation rules

From MIDOR activities.xlsx, list activities under each scope. Allocate the Scope 1 total (1.80 Mt) proportionally across those activities with realistic refinery weights (e.g., fired heaters/boilers 45–60%, flares 5–12%, process 10–25%, fugitives 3–8%, mobile <2%, wastewater <1%, F-gases if present <1%).

Break Scope 2 (0.25 Mt) by supplier (e.g., 80% MIDELEC / 20% National Grid) unless Excel says otherwise.

Scope 3 Cat.11 (35.0 Mt) apportion by product energy content and regional end-use assumptions; show a clear “placeholder” watermark below tables.

8) Compliance cues (text blocks the agent must include)

Statement of conformance with ISO 14064-1 & GHG Protocol.

Organizational boundary method: Operational Control.

Gases included: CO₂, CH₄, N₂O (others if present).

GWP source/date: IPCC AR6, 100-yr.

Scope 2 method: location-based (market-based TBD).

Base year: 2025; recalculation triggers listed.

Exclusions: listed with justifications.

Uncertainty: quantitative (±% at 95% CI) and/or qualitative per category; overall inventory uncertainty.

Inventory Management Plan summary (roles, data systems, QC/QA, document retention, change control).

9) File names & build notes

Keep semantic HTML sections.

All diagrams, icons, and color tokens centralized in CSS variables.

Use system fonts or embed a modern sans stack; ensure printable without web access.

Include a small “How to update this report next year” note at the end (swap Excel file, rerun script/build).

Deliver exactly these artifacts

index.html, assets/css/styles.css, assets/js/charts.js, assets/img/ (with MIDPR_map.PNG placeholder).

The HTML prints to a minimum of 20 pages A4 with clean pagination, headers/footers, numbered figures/tables, and crisp SVG charts.

All numbers clearly labeled “dummy / to be replaced” in footers of data tables.

Windows CMD one-liner to zip the project (put in the parent folder)

powershell -NoP -C "Compress-Archive -Path .\midor-ghg-report -DestinationPath .\MIDOR_GHG_Report_2025.zip -Force"

Notes for the agent

If any activity in MIDOR activities.xlsx is ambiguous, still place it visibly under the closest category with a clear “classification pending” tag.

Keep the credits on Page 2 (“About this Report”), not inside any assurance statement, to stay aligned with ISO/GHG Protocol tone.

Avoid revealing raw emission factor numbers in the main body unless needed; keep detailed EF placeholders in Appendix B with clear citations/“to be replaced” labels.