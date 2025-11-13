#!/usr/bin/env python3
"""
Script to create a copy of MIDOR activities Excel file
with dummy activity data and emission factors for calculations
"""

import pandas as pd
from pathlib import Path

# Read the original file
df_original = pd.read_excel('MIDOR activities.xlsx', sheet_name='For automation and LLM')

# Create a copy with additional columns for dummy calculations
df_dummy = df_original.copy()

# Add columns for activity data, emission factors, and calculations
df_dummy['Activity Data Value (Dummy)'] = ''
df_dummy['Activity Data Unit'] = ''
df_dummy['Emission Factor (Dummy)'] = ''
df_dummy['EF Unit'] = ''
df_dummy['Calculated Emissions (tCO2e)'] = ''

# Populate dummy data based on scope and category
for idx, row in df_dummy.iterrows():
    scope = row['Scope']
    category = row['Category']
    activity = row['Activity']

    # Scope 1 - Stationary Combustion (Fuel Gas)
    if scope == 1 and 'stationary' in str(category).lower() and 'fuel gas' in str(activity).lower():
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 50000 + (idx * 1000)  # GJ
        df_dummy.at[idx, 'Activity Data Unit'] = 'GJ'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 56.1  # kg CO2e/GJ
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/GJ'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (50000 + idx*1000) * 56.1 / 1000

    # Scope 1 - Stationary Combustion (Incinerator)
    elif scope == 1 and 'stationary' in str(category).lower() and 'Incenerator' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 25000 + (idx * 500)
        df_dummy.at[idx, 'Activity Data Unit'] = 'GJ'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 58.0
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/GJ'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (25000 + idx*500) * 58.0 / 1000

    # Scope 1 - Stationary Combustion (Fuel Oil)
    elif scope == 1 and 'stationary' in str(category).lower() and 'Fuel oil' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 15000
        df_dummy.at[idx, 'Activity Data Unit'] = 'GJ'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 77.4
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/GJ'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 15000 * 77.4 / 1000

    # Scope 1 - Stationary Combustion (Diesel)
    elif scope == 1 and 'stationary' in str(category).lower() and 'Diesel' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 5000 + (idx * 100)
        df_dummy.at[idx, 'Activity Data Unit'] = 'L'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 2.68
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/L'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (5000 + idx*100) * 2.68 / 1000

    # Scope 1 - Stationary Combustion (Flare)
    elif scope == 1 and 'stationary' in str(category).lower() and 'Flare' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 120000
        df_dummy.at[idx, 'Activity Data Unit'] = 'Nm3'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 2.1
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/Nm3'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 120000 * 2.1 / 1000

    # Scope 1 - Process Emissions (H2 production)
    elif scope == 1 and 'Process' in str(category) and 'H2' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 80000 + (idx * 2000)
        df_dummy.at[idx, 'Activity Data Unit'] = 'Nm3 H2'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 9.8
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/Nm3 H2'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (80000 + idx*2000) * 9.8 / 1000

    # Scope 1 - Process Emissions (Catalyst regeneration)
    elif scope == 1 and 'Process' in str(category) and 'Catalyst' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 45000
        df_dummy.at[idx, 'Activity Data Unit'] = 'kg catalyst'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.2
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/kg catalyst'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 45000 * 3.2 / 1000

    # Scope 1 - Process Emissions (Coke drum steaming)
    elif scope == 1 and 'Process' in str(category) and 'Coke' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 30000
        df_dummy.at[idx, 'Activity Data Unit'] = 'tons coke'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 1.5
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/ton coke'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 30000 * 1.5 / 1000

    # Scope 1 - Process Emissions (SRU)
    elif scope == 1 and 'Process' in str(category) and 'SRU' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 15000 + (idx * 500)
        df_dummy.at[idx, 'Activity Data Unit'] = 'tons sulfur'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.35
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/ton sulfur'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (15000 + idx*500) * 0.35 / 1000

    # Scope 1 - Fugitive Emissions (Storage tanks)
    elif scope == 1 and 'Fugitive' in str(category) and 'Storage' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 5000 + (idx * 200)
        df_dummy.at[idx, 'Activity Data Unit'] = 'm3 throughput'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.15
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/m3'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (5000 + idx*200) * 0.15 / 1000

    # Scope 1 - Fugitive Emissions (Loading/Unloading)
    elif scope == 1 and 'Fugitive' in str(category) and 'loading' in str(activity).lower():
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 8000
        df_dummy.at[idx, 'Activity Data Unit'] = 'm3 loaded'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.12
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/m3'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 8000 * 0.12 / 1000

    # Scope 1 - Fugitive Emissions (Waste water)
    elif scope == 1 and 'Fugitive' in str(category) and 'water' in str(activity).lower():
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 500000
        df_dummy.at[idx, 'Activity Data Unit'] = 'm3 wastewater'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.025
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/m3'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 500000 * 0.025 / 1000

    # Scope 1 - Fugitive Emissions (Refrigerant)
    elif scope == 1 and 'Fugitive' in str(category) and 'Refrigerant' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 150
        df_dummy.at[idx, 'Activity Data Unit'] = 'kg refrigerant'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 1430
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/kg refrigerant'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 150 * 1430 / 1000

    # Scope 1 - Fugitive Emissions (Fire extinguishers)
    elif scope == 1 and 'Fugitive' in str(category) and 'Fire extinguisher' in str(activity):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 200
        df_dummy.at[idx, 'Activity Data Unit'] = 'kg CO2'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 1
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/kg CO2'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 200 * 1 / 1000

    # Scope 1 - Mobile Combustion
    elif scope == 1 and 'Mobile' in str(category):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 10000 + (idx * 500)
        df_dummy.at[idx, 'Activity Data Unit'] = 'L diesel'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 2.68
        df_dummy.at[idx, 'EF Unit'] = 'kg CO2e/L'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = (10000 + idx*500) * 2.68 / 1000

    # Scope 2 - Purchased Electricity
    elif scope == 2:
        if 'Midelec' in str(row['Sub activity']):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 357600  # 80% of 447 GWh
            df_dummy.at[idx, 'Activity Data Unit'] = 'MWh'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.559  # Egypt grid EF
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/MWh'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 357600 * 0.559
        else:  # National Grid
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 89400  # 20% of 447 GWh
            df_dummy.at[idx, 'Activity Data Unit'] = 'MWh'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 0.559
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/MWh'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 89400 * 0.559

    # Scope 3 - Employee Commute
    elif scope == 3 and 'Employee' in str(category):
        df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 2500
        df_dummy.at[idx, 'Activity Data Unit'] = 'employees'
        df_dummy.at[idx, 'Emission Factor (Dummy)'] = 12  # Estimate per employee
        df_dummy.at[idx, 'EF Unit'] = 'tCO2e/employee/year'
        df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 2500 * 12

    # Scope 3 - Use of Sold Products
    elif scope == 3 and 'Use of Sold' in str(category):
        if 'LPG' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 450000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.0
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 450000 * 3.0
        elif 'gasoline' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 1200000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.15
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 1200000 * 3.15
        elif 'diesel' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 1800000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.17
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 1800000 * 3.17
        elif 'jet fuel' in str(activity) or 'kerosene' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 600000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.15
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 600000 * 3.15
        elif 'fuel oil' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 900000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.17
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 900000 * 3.17
        elif 'petroleum coke' in str(activity):
            df_dummy.at[idx, 'Activity Data Value (Dummy)'] = 250000
            df_dummy.at[idx, 'Activity Data Unit'] = 'tons'
            df_dummy.at[idx, 'Emission Factor (Dummy)'] = 3.5
            df_dummy.at[idx, 'EF Unit'] = 'tCO2e/ton'
            df_dummy.at[idx, 'Calculated Emissions (tCO2e)'] = 250000 * 3.5

# Round calculated emissions to 2 decimal places
df_dummy['Calculated Emissions (tCO2e)'] = df_dummy['Calculated Emissions (tCO2e)'].apply(
    lambda x: round(float(x), 2) if x != '' and pd.notna(x) else x
)

# Create an Excel writer with multiple sheets
output_file = Path(__file__).parent / "midor-ghg-report" / "MIDOR_activities_with_dummy_data.xlsx"

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the dummy data sheet
    df_dummy.to_excel(writer, sheet_name='Activities with Dummy Data', index=False)

    # Also include the original data for reference
    df_original.to_excel(writer, sheet_name='Original Activities', index=False)

    # Create a summary sheet
    summary_data = []
    for scope in [1, 2, 3]:
        scope_data = df_dummy[df_dummy['Scope'] == scope]
        total_emissions = scope_data['Calculated Emissions (tCO2e)'].apply(
            lambda x: float(x) if x != '' and pd.notna(x) else 0
        ).sum()
        summary_data.append({
            'Scope': f'Scope {int(scope)}',
            'Total Activities': len(scope_data),
            'Total Emissions (tCO2e)': round(total_emissions, 2)
        })

    df_summary = pd.DataFrame(summary_data)
    df_summary.to_excel(writer, sheet_name='Summary', index=False)

print(f"✓ Successfully created dummy activities file")
print(f"✓ Saved to: {output_file}")
print(f"\nFile contains 3 sheets:")
print(f"  1. Activities with Dummy Data - Full dataset with calculations")
print(f"  2. Original Activities - Original data for reference")
print(f"  3. Summary - Emissions summary by scope")
print(f"\nColumns added:")
print(f"  - Activity Data Value (Dummy)")
print(f"  - Activity Data Unit")
print(f"  - Emission Factor (Dummy)")
print(f"  - EF Unit")
print(f"  - Calculated Emissions (tCO2e)")
