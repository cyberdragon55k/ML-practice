import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
# Scikit-learn has built-in datasets so you don't need to download a CSV.
iris = load_iris("C:/Users/adity/OneDrive/Desktop/VS code/Jupyter/iris_data.csv")
X = iris.data    # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Labels: 0 (setosa), 1 (versicolor), 2 (virginica)

# 2. Split the data
# We use 80% of the data for training and 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize the Model
# Random Forest is a powerful ensemble method.
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. Train the Model (Fit)
print("Training the model...")
model.fit(X_train, y_train)

# 5. Make Predictions
predictions = model.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# 7. (Optional) Test with a new, random sample
# Let's invent a flower with measurements [5.1, 3.5, 1.4, 0.2]
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction_index = model.predict(new_sample)
predicted_species = iris.target_names[prediction_index][0]

print(f"Prediction for sample {new_sample}: {predicted_species}")