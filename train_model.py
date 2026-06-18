import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
df = pd.read_csv("driving_data.csv")

# Features and Target
X = df[["Speed", "Terrain_Code", "Braking"]]
y = df["Efficiency"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")
print(f"MAE : {mae:.2f}")
print(f"MSE : {mse:.2f}")
print(f"R² Score : {r2:.2f}")

# Save model
with open("efficiency_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as efficiency_model.pkl")
import matplotlib.pyplot as plt

plt.scatter(y_test, predictions)
plt.xlabel("Actual Efficiency")
plt.ylabel("Predicted Efficiency")
plt.title("Actual vs Predicted Efficiency")
plt.savefig("model_performance.png")
plt.show()