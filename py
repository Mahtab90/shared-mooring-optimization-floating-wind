# ---------------------------------------------
# Shared vs. Baseline Mooring System Comparison
# Author: Mahtab Shahin
# Purpose: Analyze cost, environmental impact, and risk of mooring systems
# Output: CSV table + bar plots
# ---------------------------------------------

import pandas as pd
import os
import matplotlib.pyplot as plt

# -------------------------------
# SECTION 1: INPUT DEFINITIONS
# -------------------------------

# Number of turbines in the floating wind farm
NUM_TURBINES = 10

# Assumed water depth (can be used in future for dynamic loading models)
WATER_DEPTH = 600  # meters

# Define two configurations: Baseline and Shared Mooring
baseline = {
    "type": "Baseline",
    "lines_per_turbine": 3,
    "anchors_per_turbine": 3,
    "estimated_cost_per_unit": 3.0,  # in million USD
    "material_efficiency": "Medium",
    "installation_complexity": "High",
    "dynamic_coupling": False,
    "failure_resilience": "Medium"
}

shared = {
    "type": "Shared",
    "lines_per_turbine": 1.5,
    "anchors_per_turbine": 1.5,
    "estimated_cost_per_unit": 2.0,  # in million USD
    "material_efficiency": "High",
    "installation_complexity": "Moderate",
    "dynamic_coupling": True,
    "failure_resilience": "High"
}

# -------------------------------
# SECTION 2: PREPROCESSING
# -------------------------------

# Create output directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Function to validate configuration input (can be expanded for YAML/JSON loading)
def validate_config(config):
    assert "lines_per_turbine" in config
    assert config["lines_per_turbine"] > 0
    assert config["anchors_per_turbine"] > 0
    assert config["estimated_cost_per_unit"] > 0

# Apply validation
for cfg in [baseline, shared]:
    validate_config(cfg)

# -------------------------------
# SECTION 3: SIMULATION ALGORITHM
# -------------------------------

def calculate_total_cost(config, num_turbines):
    """Estimate total cost for entire wind farm based on unit cost per turbine."""
    return round(config["estimated_cost_per_unit"] * num_turbines, 2)

def estimate_seabed_footprint(config, num_turbines):
    """Estimate the disturbed seabed area based on number of anchors used."""
    total_anchors = config["anchors_per_turbine"] * num_turbines
    footprint_per_anchor = 20  # m² assumption
    return round(total_anchors * footprint_per_anchor, 2)

def calculate_coupling_penalty(config):
    """Add modeling complexity if turbines are dynamically coupled."""
    return 0.3 if config["dynamic_coupling"] else 0.0

def compute_risk_index(config):
    """
    Compute a risk index (1–5) where:
    - High resilience and moderate complexity = low risk
    - Low resilience and high complexity = high risk
    """
    base = 3
    if config["failure_resilience"] == "High":
        base -= 1
    if config["installation_complexity"] == "High":
        base += 1
    return max(1, min(5, base))

def summarize_configuration(config, num_turbines):
    """Return all evaluated indicators for a mooring configuration."""
    return {
        "Configuration": config["type"],
        "Lines/Turbine": config["lines_per_turbine"],
        "Anchors/Turbine": config["anchors_per_turbine"],
        "Material Efficiency": config["material_efficiency"],
        "Installation Complexity": config["installation_complexity"],
        "Dynamic Coupling": "Yes" if config["dynamic_coupling"] else "No",
        "Failure Resilience": config["failure_resilience"],
        "Total Estimated Cost (M USD)": calculate_total_cost(config, num_turbines),
        "Seabed Footprint (m²)": estimate_seabed_footprint(config, num_turbines),
        "Coupling Penalty": calculate_coupling_penalty(config),
        "Risk Index (1-5)": compute_risk_index(config)
    }

# -------------------------------
# SECTION 4: OUTPUT AND PLOTTING
# -------------------------------

def plot_comparison_charts(df):
    """Generate bar plots comparing cost and environmental impact."""
    # Total Cost Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["Configuration"], df["Total Estimated Cost (M USD)"], color='steelblue')
    plt.title("Total Mooring System Cost")
    plt.ylabel("Cost (Million USD)")
    plt.tight_layout()
    plt.savefig("results/cost_comparison.png")
    plt.close()

    # Seabed Footprint Chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["Configuration"], df["Seabed Footprint (m²)"], color='seagreen')
    plt.title("Seabed Footprint Comparison")
    plt.ylabel("Disturbed Area (m²)")
    plt.tight_layout()
    plt.savefig("results/footprint_comparison.png")
    plt.close()

# -------------------------------
# MAIN FUNCTION
# -------------------------------

def run_analysis():
    """Run full analysis and output results."""
    print("🔍 Starting mooring configuration simulation...\n")

    # Run simulations for both configurations
    configs = [baseline, shared]
    results = [summarize_configuration(cfg, NUM_TURBINES) for cfg in configs]

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Save as CSV
    output_file = "results/mooring_comparison.csv"
    df.to_csv(output_file, index=False)

    print(f"✅ Results saved to '{output_file}'\n")
    print("📊 Summary:\n")
    print(df.to_string(index=False))

    # Plot visual results
    plot_comparison_charts(df)
    print("📈 Charts saved in the 'results/' folder.")

# -------------------------------
# EXECUTE
# -------------------------------

if __name__ == "__main__":
    run_analysis()
