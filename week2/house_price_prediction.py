import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# --- STEP 1: LOAD DATA ---
# Ensure Housing.csv is in the same folder as this script
try:
    df = pd.read_csv('Housing.csv')
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'Housing.csv' not found. Please ensure the file is in the same folder.")
    exit()

# --- STEP 2: PREPROCESSING ---
print("Processing data...")

# Map Yes/No to 1/0
binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
def binary_map(x):
    return x.map({'yes': 1, 'no': 0})
df[binary_cols] = df[binary_cols].apply(binary_map)

# One-Hot Encoding for 'furnishingstatus'
status = pd.get_dummies(df['furnishingstatus'], drop_first=True)
df = pd.concat([df, status], axis=1)
df.drop(['furnishingstatus'], axis=1, inplace=True)

# --- STEP 3: SPLITTING ---
# Target (y) is price, Features (X) is everything else
y = df.pop('price')
X = df

# 70% Training, 30% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=100)

# --- STEP 4: TRAINING ---
print("Training model...")
lm = LinearRegression()
lm.fit(X_train, y_train)

# --- STEP 5: EVALUATION ---
print("Evaluating model...")
y_pred = lm.predict(X_test)

# Calculate Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
# Mean Relative Error (MRE) - manually calculated
mre = np.mean(np.abs((y_test - y_pred) / y_test))

# --- STEP 6: PRINT REPORT ---
print("\n" + "="*30)
print("   MODEL PERFORMANCE REPORT   ")
print("="*30)
print(f"R² Score (Accuracy): {r2:.4f}  (Target: ~0.67)")
print(f"MAE  (Avg Error):    {mae:,.2f}")
print(f"MSE  (Squared Err):  {mse:,.2f}")
print(f"RMSE (Root MSE):     {rmse:,.2f}")
print(f"MRE  (Relative Err): {mre:.2%}")
print("="*30)

print("\nKey Factors (Coefficients):")
coeffs = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print(coeffs.sort_values(by='Coefficient', ascending=False).head(5))