import joblib
from pathlib import Path

model_path = Path(__file__).resolve().parent / "model.pkl"
model = joblib.load(model_path)

# Label mapping (adjust this to match your model's labels)
label_map = {
    0: "Sunny",
    1: "Rain Likely",
    2: "Poor Air Quality",
    3: "Storm Expected",
}

# def predict_weather(features):
#     X = [[
#         features["temperature"],
#         features["humidity"],
#         features["wind_speed"],
#         features["pressure"]
#     ]]
#     return model.predict(X)[0]

def predict_weather(weather_data):
    # Example: make sure the order of features matches training data
    features = [[
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["wind_speed"],
        weather_data["pressure"]
    ]]
    
    prediction = model.predict(features)[0]  # This returns a number like 0, 1, 2...

    # Convert numeric prediction to readable label
    return label_map.get(prediction, "Unknown")