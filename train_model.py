
# Model Training Script

# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load data
df = pd.read_csv("data/user_data.csv")

# Features and target
feature_names = ['age', 'weight', 'calories', 'sleep_hrs', 'steps', 'workout_mins', 'mood']
X = df[feature_names]
y = df['progress']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)

"""
Creates a Random Forest classifier, a type of ensemble machine learning model
n_estimators=100: Uses 100 decision trees (more trees generally = better performance)
random_state=42: Ensures reproducible results (same split, same model each time)
"""


model.fit(X_train, y_train)

"""
Fit the model to the training data
This trains the model on the training data, learning patterns and relationships between features and target variable
The model learns to make predictions based on the training data

X_train: The input features (like weight, calories, sleep, etc.)

y_train: The target labels (1 = on track, 0 = not on track)
"""


# Save model
os.makedirs("model", exist_ok=True)
"""
Saves the trained model to a file so it can be used later for predictions
model: The trained model
"model/fitness_model.pkl": The file path where the model is saved
joblib.dump: A function that saves the model to a file
"""
#Ensures the model/ directory exists.
#exist_ok=True: Prevents an error if the folder already exists.

joblib.dump(model, "model/fitness_model.pkl")

"""
Saves the trained model to a file called fitness_model.pkl.
joblib is used because it efficiently stores large NumPy/scikit-learn objects.
"""

print("Model trained and saved.")
