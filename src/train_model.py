# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_curve,
    auc,
    f1_score,
    recall_score,
)
import matplotlib.pyplot as plt

# load cleaned data
df = pd.read_csv("../data/cleaned_employee_data.csv")
print("Data loaded successfully with shape:", df.shape)

# split data into training/ testing
X = df[["salary", "engagement_trend", "tenure"]]
y = df["attrition"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="binary")
recall = recall_score(y_test, predictions, average="binary")
conf_matrix = confusion_matrix(y_test, predictions)
# Generate classification report
report = classification_report(y_test, predictions)
print("Classification Report:")
print(report)

print(f"Model accuracy: {accuracy*100:.2f}% 🚀")
print(f"F1 Score: {f1:.2f}")
print(f"Recall: {recall:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

# ROC Curve
y_prob = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color="blue", label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], color="red", linestyle="--")
plt.title("Receiver Operating Characteristic (ROC) Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.show()
