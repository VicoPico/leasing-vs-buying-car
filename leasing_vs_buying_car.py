import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# --- Time value helpers ---
def annual_to_monthly_rate(annual_rate: float) -> float:
    """Convert an annual discount rate to an equivalent monthly rate."""
    return (1 + annual_rate) ** (1 / 12) - 1


def npv_with_monthly_flows(
    initial_cashflow: float, monthly_flows, annual_rate: float
) -> float:
    """Calculate NPV with an initial cashflow at t=0 and a sequence of monthly flows."""
    monthly_rate = annual_to_monthly_rate(annual_rate)
    present_value = initial_cashflow
    if monthly_rate == 0:
        return present_value + float(np.sum(monthly_flows))
    for month, cashflow in enumerate(monthly_flows, start=1):
        present_value += cashflow / ((1 + monthly_rate) ** month)
    return present_value


# --- Core model ---
def calculate_buy_vs_lease_costs(
    purchase_price=35000,
    lease_payment_monthly=400,
    lease_term_months=36,
    horizon_years=5,
    resale_value=15000,
    discount_rate_annual=0.03,
    maintenance_buy_annual=1000,
    maintenance_lease_annual=300,
    insurance_buy_annual=1200,
    insurance_lease_annual=1300,
    lease_acquisition_fee=500,
    lease_disposition_fee=500,
):
    """Return (PV_buy, PV_lease) using monthly cashflows and lease cycles."""

    total_months = int(round(horizon_years * 12))

    # --- Buying costs ---
    monthly_buy_cost = (maintenance_buy_annual + insurance_buy_annual) / 12.0
    buy_cashflows = [-monthly_buy_cost] * total_months
    if total_months > 0:
        buy_cashflows[-1] += resale_value
    pv_buy = npv_with_monthly_flows(
        initial_cashflow=-purchase_price,
        monthly_flows=buy_cashflows,
        annual_rate=discount_rate_annual,
    )

    # --- Leasing costs ---
    monthly_lease_cost = (
        lease_payment_monthly
        + (maintenance_lease_annual + insurance_lease_annual) / 12.0
    )
    lease_cashflows = [-monthly_lease_cost] * total_months

    for month in range(1, total_months + 1):
        if (month - 1) % lease_term_months == 0:
            lease_cashflows[month - 1] -= lease_acquisition_fee
        if month % lease_term_months == 0:
            lease_cashflows[month - 1] -= lease_disposition_fee

    pv_lease = npv_with_monthly_flows(
        initial_cashflow=0.0,
        monthly_flows=lease_cashflows,
        annual_rate=discount_rate_annual,
    )

    return pv_buy, pv_lease


# --- Sweep over horizons & utility helpers ---
def compare_costs_over_time(max_horizon_years=10, **kwargs) -> pd.DataFrame:
    results = []
    for years in range(1, max_horizon_years + 1):
        pv_buy, pv_lease = calculate_buy_vs_lease_costs(horizon_years=years, **kwargs)
        results.append(
            {
                "Years": years,
                "PresentValue_Buy": pv_buy,
                "PresentValue_Lease": pv_lease,
                "LeaseMinusBuy": pv_lease - pv_buy,
            }
        )
    df = pd.DataFrame(results)
    return df


def find_breakeven_year(costs_df: pd.DataFrame):
    """Return the earliest integer year where leasing becomes cheaper (<= 0)."""
    for idx, row in costs_df.iterrows():
        if row["LeaseMinusBuy"] <= 0:
            return int(row["Years"])
    return None


def plot_cost_comparison(
    costs_df: pd.DataFrame, title="Car: Lease vs Buy Over Time", show_breakeven=True
):
    plt.figure(figsize=(8, 5))
    plt.plot(costs_df["Years"], costs_df["PresentValue_Buy"], marker="o", label="Buy")
    plt.plot(
        costs_df["Years"], costs_df["PresentValue_Lease"], marker="o", label="Lease"
    )
    if show_breakeven:
        breakeven = find_breakeven_year(costs_df)
        if breakeven is not None:
            plt.axvline(
                breakeven,
                linestyle="--",
                alpha=0.6,
                label=f"Breakeven ≈ Year {breakeven}",
            )
    plt.xlabel("Time Horizon (Years)")
    plt.ylabel("Present Value Cost ($)")
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df_costs = compare_costs_over_time(
        max_horizon_years=10,
        purchase_price=35000,
        lease_payment_monthly=400,
        lease_term_months=36,
        resale_value=15000,
        discount_rate_annual=0.03,
        maintenance_buy_annual=1000,
        maintenance_lease_annual=300,
        insurance_buy_annual=1200,
        insurance_lease_annual=1300,
        lease_acquisition_fee=500,
        lease_disposition_fee=500,
    )
    print(df_costs.to_string(index=False))
    print("Breakeven year:", find_breakeven_year(df_costs))
    plot_cost_comparison(df_costs)
