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

# Exp 3
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib
# import json
# import os

# # Create output directories
# os.makedirs("outputs/model", exist_ok=True)
# os.makedirs("outputs/results", exist_ok=True)

# # Load dataset
# data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# # Features and target
# X = data.drop("quality", axis=1)
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Random Forest Regressor model
# model = RandomForestRegressor(
#     n_estimators=50,
#     max_depth=10,
#     random_state=42
# )

# # Train model
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-03: Random Forest Regressor (50 Trees, Max Depth = 10)")
# print("Model           : Random Forest Regressor")
# print("Hyperparameters : n_estimators=50, max_depth=10")
# print("Preprocessing   : None")
# print("Feature Select  : All features")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/rf_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Feature_Select": "All features",
#     "Hyperparameters": {"n_estimators": 50, "max_depth": 10}
# }

# with open("outputs/results/rf_metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)


# Exp 4
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib
# import json
# import os

# # Create output directories
# os.makedirs("outputs/model", exist_ok=True)
# os.makedirs("outputs/results", exist_ok=True)

# # Load dataset
# data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# # Correlation-based feature selection
# corr = data.corr()["quality"].abs().sort_values(ascending=False)
# selected_features = corr[corr > 0.2].index.drop("quality")

# X = data[selected_features]
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Random Forest Regressor model
# model = RandomForestRegressor(
#     n_estimators=100,
#     max_depth=15,
#     random_state=42
# )

# # Train model
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-04: Random Forest Regressor (100 Trees, Max Depth = 15) + Correlation-Based Feature Selection")
# print("Model           : Random Forest Regressor")
# print("Hyperparameters : n_estimators=100, max_depth=15")
# print("Preprocessing   : None")
# print(f"Feature Select  : Correlation-based (threshold > 0.2) -> {list(selected_features)}")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/rf_corr_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Selected_Features": list(selected_features),
#     "Hyperparameters": {"n_estimators": 100, "max_depth": 15}
# }

# with open("outputs/results/rf_corr_metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)


# Exp -05

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib
# import json
# import os

# # Create output directories
# os.makedirs("outputs/model", exist_ok=True)
# os.makedirs("outputs/results", exist_ok=True)

# # Load dataset
# data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# # Features and target
# X = data.drop("quality", axis=1)
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=1
# )

# # Standardization
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Linear Regression model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-05: Linear Regression + Standardization")
# print("Model           : Linear Regression")
# print("Hyperparameters : Default")
# print("Preprocessing   : Standardization (StandardScaler)")
# print("Feature Select  : All features")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/lr_std_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Feature_Select": "All features",
#     "Preprocessing": "Standardization"
# }

# with open("outputs/results/lr_std_metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)


# Exp-06
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Lasso
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib
# import json
# import os

# # Create output directories
# os.makedirs("outputs/model", exist_ok=True)
# os.makedirs("outputs/results", exist_ok=True)

# # Load dataset
# data = pd.read_csv("dataset/winequality-red.csv", sep=";")

# # Features and target
# X = data.drop("quality", axis=1)
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=2
# )

# # Lasso Regression model
# model = Lasso(alpha=0.01)
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-06: Lasso Regression + Feature Selection")
# print("Model           : Lasso Regression")
# print("Hyperparameters : alpha=0.01")
# print("Preprocessing   : None")
# print("Feature Select  : L1 Regularization (Implicit)")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/lasso_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Feature_Select": "L1 Regularization (Implicit)",
#     "Hyperparameters": {"alpha": 0.01}
# }

# with open("outputs/results/lasso_metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)


# Exp -07
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
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

# # Features and target
# X = data.drop("quality", axis=1)
# y = data["quality"]

# # Train-test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=9
# )

# # Ridge Regression model
# model = Ridge(alpha=5.0)
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print experiment summary
# print("EXP-07: Ridge Regression (alpha = 5.0)")
# print("Model           : Ridge Regression")
# print("Hyperparameters : alpha=5.0")
# print("Preprocessing   : None")
# print("Feature Select  : All features")
# print("Train/Test Split: 80/20")
# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R² Score              : {r2:.4f}")

# # Save model
# joblib.dump(model, "outputs/model/ridge_alpha5_model.pkl")

# # Save metrics
# metrics = {
#     "MSE": mse,
#     "R2_Score": r2,
#     "Feature_Select": "All features",
#     "Hyperparameters": {"alpha": 5.0}
# }


# Exp -08
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
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
    X, y, test_size=0.2, random_state=2
)

# Lasso Regression model
model = Lasso(alpha=0.01)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print experiment summary
print("EXP-08: Lasso Regression + Feature Selection")
print("Model           : Lasso Regression")
print("Hyperparameters : alpha=0.01")
print("Preprocessing   : None")
print("Feature Select  : L1 Regularization (Implicit)")
print("Train/Test Split: 80/20")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score              : {r2:.4f}")

# Save model
joblib.dump(model, "outputs/model/lasso_model_2.pkl")

# Save metrics
metrics = {
    "MSE": mse,
    "R2_Score": r2,
    "Feature_Select": "L1 Regularization (Implicit)",
    "Hyperparameters": {"alpha": 0.01}
}

with open("outputs/results/lasso_metrics_2.json", "w") as f:
    json.dump(metrics, f, indent=4)


with open("outputs/results/ridge_alpha5_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)


