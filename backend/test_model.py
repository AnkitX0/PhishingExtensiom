import joblib

model = joblib.load("model/random_forest_model.pkl")
features = joblib.load("model/feature_names.pkl")

print("Model loaded")
print("Features:", len(features))
print(features)