🎗️ Breast Cancer Detection using Logistic Regression

This project builds a robust Machine Learning pipeline to predict whether a breast tumor is Benign or Malignant. It combines rigorous data engineering (to prevent crashes) with advanced visualization to achieve high medical-grade accuracy.
📊 Project Performance

    Test Accuracy: 96.10% 🏆

    Recall (Malignant): 96% (Catches 96% of cancer cases)

    False Negatives: ~3 (Minimizes missed diagnoses)

🚀 Key Features
1. Robust Data Engineering

The code is designed to be "crash-proof" and safe for real-world messy data:

    Safe Cleaning: Uses pd.to_numeric(errors='coerce') instead of simple casting, handling typos and garbage data gracefully.

    Standardization: Automatically maps raw class labels (2/4) to standard binary targets (0/1).

    Stratified Splitting: Maintains the exact ratio of cancer/benign cases during the train-test split to prevent bias.

2. High-Accuracy Configuration

Through testing, the optimal configuration was identified:

    Split Ratio: 70% Training / 30% Testing

    Random State: 42

    Solver: Liblinear/LBFGS (Auto-selected)

3. Advanced Visualization

    Confusion Matrix Heatmap: A clear, color-coded grid showing True Positives vs. False Negatives.

    Decision Boundary Plot: A custom visualization that projects the data into 2D to show how the model draws the line between Benign (Red) and Malignant (Green).

📸 Visualization Output

The project generates two key decision boundary plots:

    Training Set: Shows how the model learned to separate the data.

    Test Set: Shows how well the model generalizes to new patients.

📈 Results Breakdown
Metric	Value	Interpretation
Accuracy	96.10%	The model is correct 96% of the time.
Precision	0.93	When it predicts cancer, it is 93% confident.
Recall	0.96	It successfully detects 96% of all cancer cases.

🔍 Detailed Results Analysis
1. Confusion Matrix Explanation

The model was tested on 205 unseen patients. Here is the breakdown of its decisions:
Plaintext

[[128   5]   <-- Benign Rows
 [  3  69]]  <-- Malignant Rows

    128 True Negatives (TN): The model correctly identified 128 healthy patients.

    69 True Positives (TP): The model correctly identified 69 cancer patients.

    5 False Positives (FP): The model scared 5 healthy people by incorrectly saying they had cancer (Type I Error).

    3 False Negatives (FN): The model missed 3 cancer cases (Type II Error). This is the most critical number to keep low in medicine.

2. Classification Report Metrics

    Precision (0.93 for Cancer): When the model predicts cancer, it is right 93% of the time.

    Recall (0.96 for Cancer): The model successfully finds 96% of all actual cancer cases in the dataset.

    F1-Score (0.95): The balanced score between Precision and Recall. A score of 0.95 is considered excellent.

3. Visualization Explanation

The project generates Decision Boundary Plots for both Training and Test sets.

    The Grid: The background is divided into Red (Benign zone) and Green (Malignant zone).

    The Line: The straight line separating them is the "Decision Boundary." This is the mathematical limit the Logistic Regression calculated.

    The Dots:

        Red Dots: Actual Benign patients.

        Green Dots: Actual Malignant patients.

    Interpretation: Any Green dot that falls into the Red area (and vice versa) represents an error (False Positive/Negative). The visualization shows how cleanly the model can separate the two groups.