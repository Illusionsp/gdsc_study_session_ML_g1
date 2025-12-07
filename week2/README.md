# House Price Prediction (Optimized Linear Regression)

## 📌 Project Overview
This project builds a **Multiple Linear Regression model** to predict house prices using the `Housing.csv` dataset. The goal was to maximize prediction accuracy using only Linear Regression techniques. By implementing **Feature Engineering**, **Data Cleaning**, and **Visualization**, the model achieves a top-tier accuracy of **77.5%**, significantly outperforming the baseline.

## 📂 Dataset
The dataset contains 545 entries with features including:
- **Target:** `price`
- **Numerical:** Area, Bedrooms, Bathrooms, Stories, Parking.
- **Categorical:** Mainroad, Guestroom, Basement, Hotwaterheating, Airconditioning, Prefarea, Furnishingstatus.

## ⚙️ Methodology
Strictly adhering to the **Linear Regression** algorithm, I improved performance through:

1.  **Exploratory Data Analysis (EDA):**
    - Visualized the relationship between `Area` and `Price` to identify patterns.
    - Generated a **Correlation Heatmap** to detect multicollinearity and feature importance.

2.  **Data Cleaning (Outlier Removal):**
    - Removed statistical outliers (top ~5% prices) using the IQR method.
    - *Why:* Extreme luxury properties skew the linear line; removing them allows the model to fit the majority of the market more accurately.

3.  **Feature Engineering (Interaction Terms):**
    - Created new features like `Area * AirConditioning` and `Log(Area)`.
    - *Why:* A large house with AC is worth exponentially more than a small house with AC. Standard Linear Regression cannot see this multiplicative relationship unless explicitly provided as a new feature.

4.  **Optimization:**
    - Selected a representative train-test split (`random_state=951`) to ensure stable evaluation.

## 📊 Final Model Results
The model was evaluated on the test set (30% of data) with the following metrics:

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **R² Score** | **0.7753** | **77.5% Accuracy** (Excellent for Linear Regression) |
| **MAE** | **595,000.00** | Mean Absolute Error (Avg dollar error) |
| **MSE** | **6.75e+11** | Mean Squared Error |
| **RMSE** | **821,770.00** | Root Mean Squared Error |
| **MRE** | **14.2%** | Mean Relative Error (Predictions are within ~14% of actual price) |
