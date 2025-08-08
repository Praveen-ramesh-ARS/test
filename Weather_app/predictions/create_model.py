# predictions/create_model.py

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib

# Load sample dataset (for testing)
X, y = load_iris(return_X_y=True)

# Train simple model
model = LogisticRegression()
model.fit(X, y)

# Save the model to model.pkl
joblib.dump(model, "predictions/model.pkl")
print("Model saved successfully.")
