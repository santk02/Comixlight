import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# 1. Generate Synthetic Data
# Create a dataset with 1000 samples and 5 features
X, y = make_classification(n_samples=1000, n_features=5, n_informative=3, 
                           n_redundant=2, random_state=42)
df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(5)])
df['Target'] = y

# 2. Data Display
print("--- First 5 Rows of Data ---")
print(df.head())

# 3. Train/Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Model Validation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")
print("\n--- Detailed Classification Report ---")
print(classification_report(y_test, y_pred))

# 6. Visualization
plt.figure(figsize=(12, 5))

# Plot 1: Feature Importance
plt.subplot(1, 2, 1)
feat_importances = pd.Series(model.feature_importances_, index=df.columns[:-1])
feat_importances.nlargest(5).plot(kind='barh', color='skyblue')
plt.title('Top Features by Importance')

# Plot 2: Confusion Matrix Heatmap
plt.subplot(1, 2, 2)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')

plt.tight_layout()
plt.show()
