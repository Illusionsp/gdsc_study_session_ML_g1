# House Price Prediction (Linear Regression)

## 📌 Project Overview
This project involves building a **Linear Regression model** to predict house prices using the `Housing.csv` dataset. The analysis is performed in a **Jupyter Notebook**, allowing for step-by-step visualization of data, preprocessing, and model evaluation.

## 📂 Dataset
The dataset contains 545 entries with the following key features:
- **Target:** `price` (in currency units)
- **Features:** Area, Bedrooms, Bathrooms, Stories, Parking, etc.
- **Categorical Variables:** Mainroad, Guestroom, Basement, Hotwaterheating, Airconditioning, Prefarea, Furnishingstatus.

## ⚙️ Methodology
The notebook follows these steps:
1. **Preprocessing:** - Binary mapping (Yes/No $\rightarrow$ 1/0)
   - One-Hot Encoding for `furnishingstatus`.
2. **Visualization:** Analyzing correlations (e.g., Price vs. Area).
3. **Model:** Linear Regression using Scikit-Learn.
4. **Split:** 70% Training / 30% Testing.

## 📊 Results & Evaluation
The model was evaluated on the test set with the following performance metrics:

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **R² Score** | **0.6730** | The model explains **67.3%** of the variance in prices. |
| **MAE** | **835,899.47** | Average error in price prediction. |
| **MSE** | **1.284e+12** | Mean Squared Error. |
| **RMSE** | **1,133,123.90** | Root Mean Squared Error. |
| **MRE** | **19.19%** | The predictions are typically within **~19%** of the actual price. |

### 🔑 Key Factors
According to the model coefficients, these features add the most value:
1.  **Bathrooms** (+1.1M)
2.  **Hot Water Heating** (+980k)
3.  **Air Conditioning** (+772k)
4.  **Preferred Area** (+686k)
