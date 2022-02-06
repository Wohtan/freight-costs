**Important:**
 - This app uses 2022 Rates for customs agent and international freight costs
 - The exchange rates should be updated every 3 months

# Variables definition
For this web application we need to define two variable types for the lookups: weight related and customs-value related. So, let's begin:

 **Weight related:**
 - International freight (Customs independent)
 - Handling
 - Maneuvers
 - Additional handling (Surcharge)
 - Storage (Surcharge)
 
**Customs-value related:**
 - Guarding (Surcharge)
 - Complementary services
  
  Since the app is delimited up to 50 kilos cargo, some variables become **constant values**:
 - Additional handling -> 656 MXN
 - Storage -> 604 MXN
 - Maneuvers -> 322 MXN
 
 Also there is **DHL management surcharge**  that takes a fixed value of 448.28 MXN.

The customs agent has a table of fixed surcharges as it follows:

|Surcharge| Value MXN  |
|--|:--:|
| Importation request and validation |135 |
|Previous inspection|345|
|Previous validation|250 |
|MV and HC|120|
|**TOTAL**|850|

Summarizing, we have a fixed-costs table as follows:
|Item| Value MXN |
|--|--|
| Customs agent fixed surcharges | 850 |
| Additional handling | 656 |
| Storage  | 604 |
| Maneuvers  | 322 |
| DHL management surcharge | 448.28 |

**Surcharge for non-free storage:**
The application considers that one day of non-free storage is going to be applied, e.g, goods that arrive on friday. This concept results from the sum of:

 - Additional handling
 - Keeping
 - Storage

**Maneuvers total:**
This is the sum of:

 - Handling
 - Maneuvers

# Exchange rates

The app uses three exchange rates obtained from a third party. The average rate of the last three months is employed. A 5% "factor of safety" is applied to cover sudden fluctuations.

 Again, these rates should be updated every three months!

**Used rates**

| Rate | Value | Safe value |
|------|:-------:|:------------:|
| USD to MXN | 20.758  |21.8  |
| CHF to MXN | 22.546  |23.67 |
| EUR to MXN | 23.522  |24.69 |

***Last updated: 05/02/2022**


# How it works:

The user inputs weight and dimensions of the cargo, as well as the EXW/FCA value (Currency needs to be specified). Also the user has to specify the percentage of taxes that should be applied: 0%, 5%, 10% or 15%. Default tax rate is 5%.

 Next steps as follows:

 1. Volumetric weight is calculated by multiplying all the dimensions and dividing by 5000.
 
 2. The highest value between input-weight and volumetric-weight is used for calculations. 

 3. Weight-related values are retrieved performing lookups on tables:

	 - International freight
	 - Handling
	 
 4. Customs value is calculated by adding the EXW/FCA value and the international freight cost.

 5. Customs-value related surcharges are retrieved performing, guess what? lookups for sure:
	 - Guarding (Surcharge)
	 - Complementary services

 6. DTA is calculated as 0.8% of the customs value.

 7. IGI calculated according to the percentage chosen by the user. This is applied to the customs value.

 8. **Agent's fee calculation**:
 First, we sum these values:
 
	 - Customs value
	 - DTA
	 - IGI
	 - Government's validation -> 278 MXN
	 - Maneuvers total
	 - Surcharge for non-free storage
	 - DHL management surcharge

	Then we apply the 16% of VAT and multiply by 0.4%. **The minimum value is 1000 MXN.**
	
9. Fixed surcharges are added and this will result in the final calculation returned to the user.
