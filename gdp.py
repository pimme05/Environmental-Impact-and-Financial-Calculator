
import numpy as np

class EnvironmentalImpactCalculator:
    def __init__(self, data_dict, gdp, sdg_index_score):
        self.data_dict = data_dict
        self.carbon_saved_per_kg_pet = 2.0  # kg CO2 saved per kg PET recycled
        self.gdp = gdp  # Thailand's GDP in Baht
        self.sdg_index_score = sdg_index_score  # Current SDG Index Score for Thailand

    def prepare_and_calculate(self):
        for period, details in self.data_dict.items():
            transactions = int(details['transactions'])
            pet_collected_kg = float(details['trash_sold_kg'])
            
            total_pet_collected_annually = pet_collected_kg
            carbon_offset_annually = (total_pet_collected_annually * self.carbon_saved_per_kg_pet) / 1000
            
            revenue_sources = {
                'app_transaction_income': float(details.get('transaction_revenue', 0)),
                'trash_recycling_income': float(details.get('trash_revenue', 0))
            }
            
            total_income = sum(revenue_sources.values())
            fixed_cost = float(details.get('fixed_cost', 0))
            variable_cost = float(details.get('variable_cost', 0))
            ebit = float(details.get('ebit', 0))
            tax = float(details.get('tax', 0))
            total_cost = fixed_cost + variable_cost + tax
            net_income = ebit - tax
            
            print(f"Year: {period}")
            print(f"Transactions: {transactions}")
            print(f"Total PET Collected Annually: {total_pet_collected_annually:.2f} kg")
            print(f"Carbon Offset Annually: {carbon_offset_annually:.2f} tonnes")
            for source, income in revenue_sources.items():
                print(f"{source.replace('_', ' ').title()}: {income:.2f} Baht")
            print(f"Fixed Cost: {fixed_cost:.2f} Baht")
            print(f"Variable Cost: {variable_cost:.2f} Baht")
            print(f"EBIT: {ebit:.2f} Baht")
            print(f"Tax: {tax:.2f} Baht")
            print(f"Total Cost: {total_cost:.2f} Baht")
            print(f"Net Income: {net_income:.2f} Baht\n")
    
    def calculate_sdg_gdp_impact(self, investment_usd, exchange_rate, sdg_impact_factor, gdp_multiplier):
        """
        Calculates the potential impact of an investment on Thailand's SDG Index Score and GDP.
        :param investment_usd: Investment amount in USD.
        :param exchange_rate: USD to Baht exchange rate.
        :param sdg_impact_factor: Estimated SDG Index Score improvement per million Baht invested.
        :param gdp_multiplier: GDP increase per Baht invested.
        """
        investment_baht = investment_usd * exchange_rate
        
        # Calculate the potential increase in GDP
        gdp_increase = investment_baht * gdp_multiplier
        new_gdp = self.gdp + gdp_increase
        gdp_change_percentage = (gdp_increase / self.gdp) * 100
        
        # Calculate the potential improvement in SDG Index Score
        sdg_improvement = (investment_baht / 1_000_000) * sdg_impact_factor
        new_sdg_index_score = self.sdg_index_score + sdg_improvement
        sdg_change_percentage = (sdg_improvement / self.sdg_index_score) * 100
        
        print(f"Investment: {investment_usd} USD ({investment_baht:.2f} Baht)")
        print(f"Estimated GDP Increase: {gdp_increase:.2f} Baht")
        print(f"New GDP: {new_gdp:.2f} Baht")
        print(f"GDP Change Percentage: {gdp_change_percentage:.6f}%")
        print(f"Estimated SDG Index Score Improvement: {sdg_improvement:.2f}")
        print(f"New SDG Index Score: {new_sdg_index_score:.2f}")
        print(f"SDG Index Score Change Percentage: {sdg_change_percentage:.6f}%")
        
        return {
            'new_gdp': new_gdp,
            'gdp_change_percentage': gdp_change_percentage,
            'new_sdg_index_score': new_sdg_index_score,
            'sdg_change_percentage': sdg_change_percentage
        }

import numpy as np

# Data for the first 5 years (as provided)
data_dictionary = {
    "Year1": {
        'transactions': 3500,
        'transaction_revenue': 1_890_000,
        'trash_sold_kg': 2000,
        'trash_revenue': 798_000,
        'fixed_cost': 1_806_500,
        'variable_cost': 358_680,
        'ebit': 522_820,
        'tax': 104_564
    },
    "Year2": {
        'transactions': 3920,
        'transaction_revenue': 2_116_800,
        'trash_sold_kg': 2240,
        'trash_revenue': 893_760,
        'fixed_cost': 1_946_900,
        'variable_cost': 401_721,
        'ebit': 661_939,
        'tax': 132_388
    },
    "Year3": {
        'transactions': 4390,
        'transaction_revenue': 2_370_600,
        'trash_sold_kg': 2509,
        'trash_revenue': 1_001_091,
        'fixed_cost': 2_181_340,
        'variable_cost': 449_945,
        'ebit': 740_406,
        'tax': 148_081
    },
    "Year4": {
        'transactions': 4917,
        'transaction_revenue': 2_655_180,
        'trash_sold_kg': 2810,
        'trash_revenue': 1_121_190,
        'fixed_cost': 2_351_224,
        'variable_cost': 503_932,
        'ebit': 921_214,
        'tax': 184_243
    },
    "Year5": {
        'transactions': 5507,
        'transaction_revenue': 2_973_780,
        'trash_sold_kg': 3147,
        'trash_revenue': 1_255_653,
        'fixed_cost': 2_538_096,
        'variable_cost': 564_377,
        'ebit': 1_126_960,
        'tax': 225_392
    }
}

# Set growth rate for years 2 to 5
growth_rate_transaction_revenue = 0.27  # 27% growth year-on-year for transactions
growth_rate_trash_revenue = 0.12  # 12% growth year-on-year for trash revenue

# Projecting data for the next 5 years (Year 6 to Year 10)
for i in range(6, 11):  # Year 6 to Year 10
    prev_year = i - 1
    data_dictionary[f"Year{i}"] = {
        'transactions': int(data_dictionary[f"Year{prev_year}"]['transactions'] * (1 + growth_rate_transaction_revenue)),
        'transaction_revenue': data_dictionary[f"Year{prev_year}"]['transaction_revenue'] * (1 + growth_rate_transaction_revenue),
        'trash_sold_kg': int(data_dictionary[f"Year{prev_year}"]['trash_sold_kg'] * (1 + growth_rate_trash_revenue)),
        'trash_revenue': data_dictionary[f"Year{prev_year}"]['trash_revenue'] * (1 + growth_rate_trash_revenue),
        'fixed_cost': data_dictionary[f"Year{prev_year}"]['fixed_cost'] * (1 + growth_rate_transaction_revenue),
        'variable_cost': data_dictionary[f"Year{prev_year}"]['variable_cost'] * (1 + growth_rate_transaction_revenue),
        'ebit': data_dictionary[f"Year{prev_year}"]['ebit'] * (1 + growth_rate_transaction_revenue),
        'tax': data_dictionary[f"Year{prev_year}"]['tax'] * (1 + growth_rate_transaction_revenue)
    }

# Printing the projected data for Year 6 to Year 10
for year, data in data_dictionary.items():
    print(f"\n{year} Data:")
    print(f"Transactions: {data['transactions']}")
    print(f"Transaction Revenue: {data['transaction_revenue']:.2f} Baht")
    print(f"Trash Revenue: {data['trash_revenue']:.2f} Baht")
    print(f"Total Revenue: {data['transaction_revenue'] + data['trash_revenue']:.2f} Baht")
    print(f"Fixed Cost: {data['fixed_cost']:.2f} Baht")
    print(f"Variable Cost: {data['variable_cost']:.2f} Baht")
    print(f"EBIT: {data['ebit']:.2f} Baht")
    print(f"Tax: {data['tax']:.2f} Baht")
    print(f"Total Cost: {data['fixed_cost'] + data['variable_cost'] + data['tax']:.2f} Baht")
    print(f"Net Income: {data['ebit'] - data['tax']:.2f} Baht")
    print("")

# You can now use the calculator to proceed with any impact analysis or other calculations.


# Thailand's GDP in Baht (as of the latest data)
gdp_thailand = 49_276_000_000_000  # Example GDP in Baht

# Thailand's current SDG Index Score
sdg_index_score_thailand = 74.67  # As per the Sustainable Development Report 2024

# Create an instance of the calculator
calculator = EnvironmentalImpactCalculator(data_dictionary, gdp_thailand, sdg_index_score_thailand)

# Perform calculations
calculator.prepare_and_calculate()

# Parameters for the impact calculation
# Thailand's GDP in Baht (as of September 2024)
gdp_thailand = 49_276_000_000_000  # 49,276.00 billion Baht

# Parameters for the impact calculation
investment_usd = 1_000_000  # Investment amount in USD
exchange_rate = 33.69  # USD to Baht exchange rate (as per your review)
sdg_impact_factor = 0.01  # Estimated SDG Index Score improvement per million Baht invested
gdp_multiplier = 0.0001  # GDP increase per Baht invested (updated multiplier based on your review)


# Calculate the impact of the investment
calculator.calculate_sdg_gdp_impact(investment_usd, exchange_rate, sdg_impact_factor, gdp_multiplier)