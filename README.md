# WasteWise Impact Calculator

Tool developed for the **Hult Prize** to measure the impact of PET recycling in Thailand.

## Overview
- Calculates **environmental benefits** (CO₂ avoided) from PET collected.  
- Projects **financial performance** (revenues, costs, EBIT, net income) for 10 years.  
- Models **investment impact** on Thailand’s GDP and SDG Index.

## Assumptions
- 2.0 kg CO₂ avoided per kg of PET recycled.  
- Growth: +27%/year for transactions & revenue, +12%/year for trash revenue.  
- Investment multipliers: GDP and SDG improvements per THB invested.

## Inputs
- Yearly data (transactions, PET collected, revenues, costs, taxes).  
- Investment scenario (USD amount, exchange rate, GDP/SDG multipliers).

## Outputs
- **Per year:** CO₂ avoided, revenues, EBIT, net income.  
- **Investment:** GDP increase (%), SDG score improvement (%).

## Quick Start
```bash
python impact_calculator.py
```

## Example
```python
from impact_calculator import EnvironmentalImpactCalculator

calc = EnvironmentalImpactCalculator(data_dictionary, 49_276_000_000_000, 74.67)
calc.prepare_and_calculate()
calc.calculate_sdg_gdp_impact(1_000_000, 33.69, 0.01, 0.0001)
```
