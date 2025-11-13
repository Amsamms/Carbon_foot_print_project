#!/usr/bin/env python3
"""
Script to extract all dummy data from index-magazine.html
and save it to an Excel file for easy modification
"""

import pandas as pd
from pathlib import Path

# Define all dummy data extracted from index-magazine.html
dummy_data = [
    # Executive Summary Data
    {"Definition": "Total GHG emissions (Million tCO2e)", "Value": "37.05"},
    {"Definition": "Scope 1 emissions (Million tCO2e)", "Value": "1.80"},
    {"Definition": "Scope 2 emissions (Million tCO2e)", "Value": "0.25"},
    {"Definition": "Scope 3 emissions (Million tCO2e)", "Value": "35.0"},
    {"Definition": "Operational footprint Scope 1+2 (Million tCO2e)", "Value": "2.05"},
    {"Definition": "Operational footprint percentage of total", "Value": "5.5%"},
    {"Definition": "Intensity metric - tCO2e per kiloton crude", "Value": "702"},
    {"Definition": "Intensity metric - tCO2e per GJ fired duty", "Value": "0.031"},

    # Scope 1 Breakdown
    {"Definition": "Scope 1 - Stationary Combustion (tCO2e)", "Value": "1170000"},
    {"Definition": "Scope 1 - Process Emissions (tCO2e)", "Value": "324000"},
    {"Definition": "Scope 1 - Fugitive Emissions (tCO2e)", "Value": "216000"},
    {"Definition": "Scope 1 - Mobile Combustion (tCO2e)", "Value": "90000"},
    {"Definition": "Scope 1 - Stationary Combustion percentage", "Value": "65%"},
    {"Definition": "Scope 1 - Process Emissions percentage", "Value": "18%"},
    {"Definition": "Scope 1 - Fugitive Emissions percentage", "Value": "12%"},
    {"Definition": "Scope 1 - Mobile Combustion percentage", "Value": "5%"},

    # Scope 2 Data
    {"Definition": "Scope 2 - Total electricity emissions (tCO2e)", "Value": "250000"},
    {"Definition": "Scope 2 - MIDELEC emissions (tCO2e)", "Value": "200000"},
    {"Definition": "Scope 2 - National Grid emissions (tCO2e)", "Value": "50000"},
    {"Definition": "Scope 2 - MIDELEC percentage", "Value": "80%"},
    {"Definition": "Scope 2 - National Grid percentage", "Value": "20%"},
    {"Definition": "Annual electricity consumption (GWh)", "Value": "447"},
    {"Definition": "Electricity intensity (MWh per kiloton crude)", "Value": "153"},

    # Scope 3 Category 11 - Use of Sold Products
    {"Definition": "Scope 3 Cat 11 - Total emissions (tCO2e)", "Value": "34970000"},
    {"Definition": "Scope 3 Cat 11 - Diesel percentage", "Value": "35.0%"},
    {"Definition": "Scope 3 Cat 11 - Gasoline percentage", "Value": "30.0%"},
    {"Definition": "Scope 3 Cat 11 - Fuel Oil percentage", "Value": "15.0%"},
    {"Definition": "Scope 3 Cat 11 - Jet Fuel percentage", "Value": "10.0%"},
    {"Definition": "Scope 3 Cat 11 - LPG percentage", "Value": "8.0%"},
    {"Definition": "Scope 3 Cat 11 - Other Products percentage", "Value": "2.0%"},
    {"Definition": "Scope 3 Cat 11 - Percentage of total footprint", "Value": "94.4%"},

    # Scope 3 Category 7 - Employee Commuting
    {"Definition": "Scope 3 Cat 7 - Employee Commuting (tCO2e)", "Value": "30000"},

    # Operational Data
    {"Definition": "Refinery capacity (BPSD)", "Value": "160000"},
    {"Definition": "Base year", "Value": "2025"},
    {"Definition": "Reporting period start", "Value": "01/01/2025"},
    {"Definition": "Reporting period end", "Value": "31/12/2025"},

    # Energy Efficiency
    {"Definition": "Potential energy savings from EMS", "Value": "5-10%"},
    {"Definition": "Operational control emissions percentage", "Value": "100%"},
    {"Definition": "Decarbonization potential estimate", "Value": "~1.4%"},

    # Uncertainty Analysis
    {"Definition": "Uncertainty - Stationary Combustion", "Value": "±8%"},
    {"Definition": "Uncertainty - Process Emissions", "Value": "±12%"},
    {"Definition": "Uncertainty - Fugitive Emissions", "Value": "±30%"},
    {"Definition": "Uncertainty - Mobile Combustion", "Value": "±10%"},
    {"Definition": "Uncertainty - Scope 1 Total", "Value": "±10%"},
    {"Definition": "Uncertainty - Scope 2 Electricity", "Value": "±5%"},
    {"Definition": "Uncertainty - Scope 3 Cat 11", "Value": "±15%"},

    # Uncertainty Ranges - Lower Bound
    {"Definition": "Stationary Combustion - Lower bound (tCO2e)", "Value": "1076400"},
    {"Definition": "Process Emissions - Lower bound (tCO2e)", "Value": "285120"},
    {"Definition": "Fugitive Emissions - Lower bound (tCO2e)", "Value": "151200"},
    {"Definition": "Mobile Combustion - Lower bound (tCO2e)", "Value": "81000"},
    {"Definition": "Scope 1 Total - Lower bound (tCO2e)", "Value": "1620000"},
    {"Definition": "Scope 2 Electricity - Lower bound (tCO2e)", "Value": "237500"},
    {"Definition": "Scope 3 Cat 11 - Lower bound (tCO2e)", "Value": "29724500"},

    # Uncertainty Ranges - Upper Bound
    {"Definition": "Stationary Combustion - Upper bound (tCO2e)", "Value": "1263600"},
    {"Definition": "Process Emissions - Upper bound (tCO2e)", "Value": "362880"},
    {"Definition": "Fugitive Emissions - Upper bound (tCO2e)", "Value": "280800"},
    {"Definition": "Mobile Combustion - Upper bound (tCO2e)", "Value": "99000"},
    {"Definition": "Scope 1 Total - Upper bound (tCO2e)", "Value": "1980000"},
    {"Definition": "Scope 2 Electricity - Upper bound (tCO2e)", "Value": "262500"},
    {"Definition": "Scope 3 Cat 11 - Upper bound (tCO2e)", "Value": "40215500"},

    # Quality Improvements
    {"Definition": "Target uncertainty - Stationary after fuel gas GC", "Value": "±5%"},
    {"Definition": "Target uncertainty - Fugitives after LDAR/OGI", "Value": "±15%"},

    # Base Year Recalculation Threshold
    {"Definition": "Base year recalculation threshold", "Value": "5%"},
    {"Definition": "Materiality threshold percentage", "Value": ">5%"},

    # Flare System
    {"Definition": "Flare destruction efficiency (DRE)", "Value": "99.9%"},
    {"Definition": "Flare DRE decimal", "Value": "0.999"},

    # Mass Balance
    {"Definition": "Expected mass balance closure tolerance", "Value": "±2%"},
    {"Definition": "YoY comparison investigation threshold", "Value": ">20%"},

    # GWP Values (IPCC AR6)
    {"Definition": "GWP - CO2", "Value": "1"},
    {"Definition": "GWP - CH4", "Value": "29.8"},
    {"Definition": "GWP - N2O", "Value": "273"},

    # Energy Input Total
    {"Definition": "Total energy input (GJ)", "Value": "58400000"},
    {"Definition": "Energy intensity calculation numerator (tCO2e)", "Value": "1800000"},
    {"Definition": "Energy intensity result (tCO2e/GJ)", "Value": "0.0308"},
]

# Create DataFrame
df = pd.DataFrame(dummy_data)

# Save to Excel
output_file = Path(__file__).parent / "midor-ghg-report" / "dummy_data_extracted.xlsx"
df.to_excel(output_file, index=False, sheet_name="Dummy Data")

print(f"✓ Successfully extracted {len(dummy_data)} data points")
print(f"✓ Saved to: {output_file}")
print(f"\nFile contains two columns:")
print(f"  - Definition: Description of each data point")
print(f"  - Value: The actual dummy value")
print(f"\nYou can now edit the 'Value' column to replace with real data.")
