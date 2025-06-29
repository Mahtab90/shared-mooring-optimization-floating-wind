# 2025_Shared_Mooring_Optimization_Floating_Wind  
AI-Assisted Evaluation of Shared Mooring Systems in Deepwater Floating Wind Farms

*This repository hosts the technical resources and analysis results for a demonstration project focused on optimizing mooring configurations for floating offshore wind farms (FOWFs). The project compares baseline vs. shared anchor-line systems through a simulation-driven, AI-supported framework.*

---


## Objective

The primary goal of this project is to develop a simulation-based, data-driven system to compare **baseline mooring systems** (independent anchors per turbine) with **shared mooring configurations** (interconnected lines and shared anchors) in **deepwater floating offshore wind farms (FOWFs)**.

The project investigates cost-efficiency, environmental impact, dynamic coupling behavior, and failure resilience, aiming to provide actionable recommendations for next-generation FOWF development.

---

## ⚙Technical Overview

### Problem Statement

Mooring systems account for a substantial portion of FOWF costs. Traditional configurations are often redundant and environmentally intensive. However, shared mooring systems—while potentially more efficient—introduce complexity due to platform coupling and non-linear dynamics.

This project simulates both configurations under standardized assumptions and uses AI-inspired scoring metrics to evaluate:

- Total system cost  
- Anchor and line requirements  
- Seabed disturbance footprint  
- Coupling penalty and risk  
- Scalability and resilience trade-offs

---

## Technical Solution: Key Highlights

- Two configurations modeled:
  - **Baseline:** 3 lines + 3 anchors per turbine  
  - **Shared:** 1.5 lines + 1.5 anchors per turbine  
- Key metrics calculated:
  - Total Estimated Cost  
  - Seabed Footprint (m²)  
  - Dynamic Coupling Penalty  
  - ⚠Risk Index (1 to 5 scale)  
- Outputs:
  - CSV file of results (`mooring_comparison.csv`)  
  - Plots: `cost_comparison.png`, `footprint_comparison.png`

---

## Input Parameters

| Variable               | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| `NUM_TURBINES`         | Number of turbines in the FOWF (default: 10)                      |
| `WATER_DEPTH`          | Water depth in meters (default: 600 m)                            |
| `estimated_cost_per_unit` | Cost per turbine mooring system (M USD)                     |
| `anchors_per_turbine`  | Average number of anchors per turbine                             |
| `lines_per_turbine`    | Average number of mooring lines per turbine                       |
| `installation_complexity` | Qualitative flag: High / Moderate                            |
| `failure_resilience`   | Qualitative flag: High / Medium                                   |
| `dynamic_coupling`     | Boolean: Yes (Shared) / No (Baseline)                             |

---

## Workflow Summary (Step-by-Step)

- **Start**
- ➤ Define Inputs: turbine count, depth, mooring parameters
- ➤ Preprocessing: validation + result folder creation
- ➤ Run Simulation: calculate cost, anchors, footprint, risk
- ➤ Compile Results: convert to DataFrame + CSV export
- ➤ Generate Plots: bar charts for cost and footprint
- ➤ Print Output: console report with metrics
- **End**


## Simulation Workflow

1. **Input Setup:** User specifies turbine count and mooring configurations  
2. **Preprocessing:** Validates values, initializes results directory  
3. **Simulation Loop:** For each configuration:
   - Calculates cost, anchor usage, and footprint  
   - Assesses coupling penalty and risk index  
4. **Data Compilation:** Results stored in structured Pandas DataFrame  
5. **Output Generation:** Saves `.csv` and generates bar plots  
6. **Console Report:** Prints summary for quick inspection  

---

## Output Examples

| Configuration | Lines/Turbine | Anchors/Turbine | Cost (M USD) | Footprint (m²) | Coupling Penalty | Risk Index |
|---------------|----------------|------------------|--------------|----------------|-------------------|------------|
| Baseline      | 3.0            | 3.0              | 30.0         | 600.0          | 0.0               | 4          |
| Shared        | 1.5            | 1.5              | 20.0         | 300.0          | 0.3               | 2          |

---

## Technical Architecture

| Module                      | Function                                                                 |
|-----------------------------|--------------------------------------------------------------------------|
| **Input Handler**           | Reads turbine parameters and mooring config                             |
| **Risk Scorer**             | Assigns a qualitative risk index (1–5) based on resilience/complexity   |
| **ARM-Inspired Simulator**  | Calculates total cost, anchors, lines, and penalties                    |
| **Result Compiler**         | Aggregates data into CSV and visual plots                               |
| **Plot Generator**          | Saves charts to `results/` directory                                    |

---

## Future Potential

- Real-time simulation engine (cloud/serverless ready)  
- Integration with floating platform simulators (e.g., OpenFAST, FAST.Farm)  
- Environmental scoring integration (e.g., seabed mapping overlays)  
- Optimization routines for multi-turbine layouts  
- Web dashboard for design teams or project engineers

---

## Lessons Learned

- Shared mooring systems offer substantial material and cost savings, but introduce new failure modes.  
- Simple cost models can provide fast pre-evaluation for layout planning.  
- Dynamic behavior and environmental data need to be integrated for full-scale deployment.  
- A hybrid of rule-based and AI-assisted logic supports better scalability than generic scripts.

---
