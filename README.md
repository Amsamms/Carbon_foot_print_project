# MIDOR Refinery GHG Inventory Report

Organizational GHG Inventory for MIDOR Refinery following ISO 14064-1:2018 and GHG Protocol Corporate Standard.

## Project Structure

```
├── midor-ghg-report/           # Main report directory
│   ├── index.html              # Standard report layout
│   ├── index-magazine.html     # Magazine-style report layout
│   ├── assets/                 # Images, CSS, and JS files
│   ├── dummy_data_extracted.xlsx    # All dummy data from report
│   └── MIDOR_activities_with_dummy_data.xlsx  # Activities with calculations
├── PRD.md                      # Product Requirements Document
├── MIDOR activities.xlsx       # Original activities template
└── extract_dummy_data.py       # Script to extract dummy data
```

## Generated Files

### 1. dummy_data_extracted.xlsx
Contains all 74 dummy data points extracted from the index-magazine.html report:
- **Definition**: Description of each data point
- **Value**: The actual dummy value used in the report

This file allows you to easily replace dummy values with real data.

### 2. MIDOR_activities_with_dummy_data.xlsx
Contains three sheets:
- **Activities with Dummy Data**: Full dataset with dummy activity data, emission factors, and calculated emissions
- **Original Activities**: Original activities structure for reference
- **Summary**: Emissions summary by scope

Includes columns for:
- Activity Data Value (Dummy)
- Activity Data Unit
- Emission Factor (Dummy)
- EF Unit
- Calculated Emissions (tCO2e)

## Base Year Information

- **Base Year**: 2025
- **Reporting Period**: January 1, 2025 - December 31, 2025
- **Total Footprint**: 37.05 Million tCO2e
  - Scope 1: 1.80 Million tCO2e
  - Scope 2: 0.25 Million tCO2e
  - Scope 3: 35.0 Million tCO2e

## Standards & Methodology

- ISO 14064-1:2018
- GHG Protocol Corporate Standard
- Operational Control Consolidation Approach
- IPCC AR6 (2021) emission factors
- API Compendium
- US EPA guidelines

## How to Use

1. **Update Dummy Data**: Open `dummy_data_extracted.xlsx` and replace values in the "Value" column with real data
2. **Update Activities**: Open `MIDOR_activities_with_dummy_data.xlsx` and update activity data and emission factors
3. **Regenerate Report**: Use updated values to regenerate the HTML reports

## Repository

- **Owner**: Ahmed Mohamed Sabri (@amsamms)
- **Created**: November 2024

## License

Proprietary - MIDOR Refinery Internal Use Only
