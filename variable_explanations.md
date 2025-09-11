# Variable Explanations for leasing_vs_buying_car.py

This document explains the meaning and purpose of each variable used in the code.

## Main Variables in `calculate_buy_vs_lease_costs`

- **purchase_price**: The total cost to buy the car upfront.
- **lease_payment_monthly**: The monthly payment required for leasing the car.
- **lease_term_months**: The duration (in months) of each lease contract.
- **horizon_years**: The total time horizon (in years) over which costs are compared.
- **resale_value**: The expected value of the car at the end of the ownership period (if bought).
- **discount_rate_annual**: The annual discount rate used to calculate present value (accounts for the time value of money).
- **maintenance_buy_annual**: The estimated annual maintenance cost when buying the car.
- **maintenance_lease_annual**: The estimated annual maintenance cost when leasing the car.
- **insurance_buy_annual**: The annual insurance cost when buying the car.
- **insurance_lease_annual**: The annual insurance cost when leasing the car.
- **lease_acquisition_fee**: The fee paid at the start of each new lease contract.
- **lease_disposition_fee**: The fee paid at the end of each lease contract.

## Helper Function Variables

- **annual_rate**: The annual interest or discount rate (used in present value calculations).
- **monthly_rate**: The equivalent monthly discount rate derived from the annual rate.
- **initial_cashflow**: The initial cash outflow (e.g., purchase price or zero for leasing).
- **monthly_flows**: A sequence (list or array) of monthly cash flows (expenses or income).
- **present_value**: The sum of all discounted cash flows, representing the net present value (NPV).
- **month, cashflow**: Loop variables for iterating over each month and its associated cash flow.

## Model Output Variables

- **pv_buy**: The present value of all costs associated with buying the car.
- **pv_lease**: The present value of all costs associated with leasing the car.
- **buy_cashflows**: List of monthly cash flows for the buying scenario.
- **lease_cashflows**: List of monthly cash flows for the leasing scenario.
- **monthly_buy_cost**: The combined monthly cost of maintenance and insurance when buying.
- **monthly_lease_cost**: The combined monthly cost of lease payment, maintenance, and insurance when leasing.
- **total_months**: The total number of months in the analysis horizon.

## Output Table Columns

- `Years`: Analysis horizon in years.
- `PresentValue_Buy`: Present value of buying costs.
- `PresentValue_Lease`: Present value of leasing costs.
- `LeaseMinusBuy`: Difference between lease and buy present values.

## Analysis and Plotting Variables

- **results**: List of dictionaries storing results for each year in the time horizon.
- **df (costs_df)**: DataFrame containing the present value costs for buying and leasing over time.
- **LeaseMinusBuy**: The difference between the present value of leasing and buying (negative means leasing is cheaper).
- **breakeven**: The year when leasing becomes cheaper than buying.

If you need further clarification on any variable or function, feel free to ask!
