🎗️ Breast Cancer Classification using Logistic Regression
📌 Project Overview

This project implements a Machine Learning model to detect breast cancer based on cell attributes. Using the Logistic Regression algorithm, the model classifies tumors as either Benign (2) or Malignant (4).

The solution is designed with a professional Data Science workflow, including robust data preprocessing, stratified validation, comprehensive performance metrics, and decision boundary visualization.
📂 Dataset Information

The project uses the Wisconsin Breast Cancer (Original) dataset (breast_cancer_bd.csv).

    Instances: 699 patients

    Attributes: 10 features (e.g., Clump Thickness, Cell Size, Mitoses) + 1 Class label.

    Target Classes:

        2: Benign (Non-cancerous) → Mapped to 0

        4: Malignant (Cancerous) → Mapped to 1

⚙️ Methodology & Logic
1. Data Preprocessing (ETL)

    Cleaning: The dataset contained non-numeric characters (?) in the Bare Nuclei column. These rows were identified and removed to ensure mathematical stability.

    Type Conversion: The cleaned column was converted to integer format.

    Target Mapping: The original classes (2/4) were mapped to binary (0/1) to align with the Logistic Regression Sigmoid function.

2. Model Training Strategy

    Stratified Splitting: The data was split 80/20 (Train/Test). Crucially, stratify=y was used to ensure the proportion of cancer cases remained consistent between training and testing, preventing data bias.

    Feature Scaling: StandardScaler was applied to normalize all features (mean=0, variance=1), ensuring that features with larger ranges (like Cell Size) did not dominate the gradient descent optimization.

3. Evaluation Metrics

The model is evaluated using industry-standard metrics:

    Accuracy: Overall percentage of correct diagnoses.

    Confusion Matrix: A detailed breakdown of True Positives, False Positives, False Negatives, and True Negatives.

    Classification Report: Provides Precision, Recall (Sensitivity), and F1-Score for each class.

4. Visualization

   A 2D contour plot is generated to visualize the decision boundary of the logistic regression model using Clump Thickness and Uniformity of Cell Size as features.
   The background color represents the model’s predicted class, where red regions indicate Benign tumors and green regions indicate Malignant tumors.
   The boundary between the colored regions shows where the model transitions between the two predictions, while the scatter points represent the actual training samples.