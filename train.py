# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Ridge
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib
# import json
# import os

# # Create output directories
# os.makedirs("outputs/model", exist_ok=True)
# os.makedirs("outputs/results", exist_ok=True)

# # Load dataset
# data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# # Feature selection (correlation-based)
# corr = data.corr()["quality"].abs().sort_values(ascending=False)
# selected_features = corr[corr > 0.2].index.drop("quality")

# X = data[selected_features]
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Standardization
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train Ridge Regression model
# model = Ridge(alpha=1.0)
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-02: Ridge Regression with Standardization + Correlation-Based Feature Selection")
# print("Model           : Ridge Regression")
# print("Hyperparameters : alpha=1.0")
# print("Preprocessing   : Standardization (StandardScaler)")
# print(f"Feature Select  : Correlation-based (threshold > 0.2) -> {list(selected_features)}")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/ridge_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Selected_Features": list(selected_features)
# }

# with open("outputs/results/ridge_metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)

# 3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
import os

# Create output directories
os.makedirs("outputs/model", exist_ok=True)
os.makedirs("outputs/results", exist_ok=True)

# Load dataset
data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# Features and target
X = data.drop("quality", axis=1)
y = data["quality"]

# Train-test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest Regressor model
model = RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print experiment summary
print("EXP-03: Random Forest Regressor (50 Trees, Max Depth = 10)")
print("Model           : Random Forest Regressor")
print("Hyperparameters : n_estimators=50, max_depth=10")
print("Preprocessing   : None")
print("Feature Select  : All features")
print("Train/Test Split: 80/20")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score              : {r2:.4f}")

# Save model
joblib.dump(model, "outputs/model/rf_model.pkl")

# Save metrics
metrics = {
    "MSE": mse,
    "R2_Score": r2,
    "Feature_Select": "All features",
    "Hyperparameters": {"n_estimators": 50, "max_depth": 10}
}

with open("outputs/results/rf_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)



