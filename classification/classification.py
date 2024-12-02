import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
salesdata = pd.read_csv(r"C:\Users\Masha\Downloads\data.csv")
label_encoder = LabelEncoder()
salesdata['Gender'] = label_encoder.fit_transform(salesdata['Gender'])
X = salesdata[['Gender', 'Age', 'Quantity', 'Price per Unit']]
y = salesdata['Product Category']
df_features = pd.DataFrame(X, columns=['Gender', 'Age', 'Quantity', 'Price per Unit'])  
df_features['Product Category'] = y 



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(probability=True),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier()
}
results = []


for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')  # Для многоклассовой классификации
    recall = recall_score(y_test, y_pred, average='weighted')  # Для многоклассовой классификации
    
    results.append({
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall
    })
results_df = pd.DataFrame(results).T
print(results_df)

script_dir = os.path.dirname(os.path.realpath(__file__))


results_path = os.path.join(script_dir, "classification_results.csv")


results_df.to_csv(results_path, index=False)
print(f"Результаты сохранены в файл: {results_path}")