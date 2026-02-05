# Ride Price Estimation System

## Project Overview
This project is an end-to-end Machine Learning solution designed to estimate ride prices based on trip and contextual factors. The goal was to build a system that moves beyond fixed pricing rules by learning patterns from a custom-designed dataset.

## Repository Structure
```text
ride-price-ml/
├── data/
│   └── rides.csv               # The generated dataset with 200 trip records
├── notebook/
│   └── ride_price_model.ipynb   # Complete ML workflow (Cleaning, Regression, Classification)
└── README.md                   # Project documentation and findings
Dataset Description

The dataset was synthetically generated to simulate real-world ride-hailing dynamics.

    Size: 200 rows

    Features Used:

        distance_km: Trip length (Primary cost driver).

        duration_min: Estimated time (Accounting for traffic).

        traffic_level: Low, Medium, High (Influences price surges).

        weather: Clear, Rain, Snow (Increases demand/price).

        time_of_day: Morning, Afternoon, Night (Peak vs. Off-peak).

        is_weekend: Binary flag for day of the week.

Feature Justification

    Distance & Duration: Fundamental metrics for any transport service to cover fuel and time.

    Weather & Traffic: Chosen to simulate "Surge Pricing" models where supply/demand imbalance affects cost.

    Excluded Feature: "Driver Rating" was considered but excluded because price should be determined by trip characteristics, not individual driver performance, to ensure pricing consistency for the user.

Key Findings & Results

    Regression: Using Linear Regression, the model successfully predicted prices with a Mean Absolute Error (MAE) of approximately $3.00 - $5.00.

    Classification: Using Logistic Regression, the model achieved ~85-90% accuracy in identifying "High-Cost" rides (prices above the median).

    Top Influencer: Distance remains the most significant predictor of price.

How to Run

    Navigate to notebook/ride_price_model.ipynb.

    Open the file in Google Colab or Jupyter Notebook.

    Ensure the data path points to ../data/rides.csv.

    Run all cells to see data cleaning, model training, and performance visualizations.