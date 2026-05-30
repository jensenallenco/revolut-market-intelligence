# Revolut Market Intelligence Engine

A production-grade, modular analytics dashboard built with Python and Streamlit to visualize and analyze official UK macroeconomic transaction indicators. This application processes real-time transaction velocity indices to extract consumer behavioral shifts and platform demographic trajectories.

🔗 **Live Interactive Dashboard:** [Insert Your Live Streamlit URL Here]

---

## Architecture Design

This repository implements a decoupled, modular design pattern rather than a monolithic script. By separating data processing, calculation engines, and user-interface layers, the codebase honors the separation of concerns, ensuring high maintainability and scalability.

```text
revolut-market-intelligence/
│
├── app.py                     # Main application entry point & UI shell
├── requirements.txt           # Active runtime dependencies
├── revolut_dataset_may2026.xlsx  # ONS time-series transaction registry
│
└── plots/                     # Isolated visualization package
    ├── __init__.py            # Package initialization marker
    ├── kpi_metrics.py         # Computational logic for top-level aggregates
    ├── age_analysis.py        # Core rendering logic for age demographics
    └── sector_analysis.py     # Core rendering logic for transaction categories
