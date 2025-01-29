import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error, explained_variance_score
from sklearn.model_selection import train_test_split

base_dir = os.path.dirname(os.path.abspath(__file__))
x_file = r"C:\Users\Мария\.vscode\регрессия\6_x.csv"
y_file = r"C:\Users\Мария\.vscode\регрессия\6_y.csv"

X = np.loadtxt(x_file, delimiter=',')
Y = np.loadtxt(y_file, delimiter=',')
print("Успешно загружены данные!")

# Разделение на тренировочную и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Функция для расчета метрик
def compute_metrics(model_type, true_values, predictions):
    metrics = {
        'Model': model_type,
        'R2_Score': r2_score(true_values, predictions),
        'MSE': mean_squared_error(true_values, predictions),
        'EVS': explained_variance_score(true_values, predictions)
    }
    return metrics
results = []

# Линейная регрессия 
for feature_idx in range(X.shape[1]):
    # Обучаем модель
    linear_model = LinearRegression()
    feature_X_train = X_train[:, feature_idx].reshape(-1, 1)
    feature_X_test = X_test[:, feature_idx].reshape(-1, 1)
    linear_model.fit(feature_X_train, Y_train)
    # Предсказания и метрики
    predictions = linear_model.predict(feature_X_test)
    results.append(compute_metrics(f'Linear Regression Feature {feature_idx + 1}', Y_test, predictions))
# Множественная линейная регрессия
multi_model = LinearRegression()
multi_model.fit(X_train, Y_train)
multi_predictions = multi_model.predict(X_test)
results.append(compute_metrics('Multiple Linear Regression', Y_test, multi_predictions))
# Полиномиальная регрессия для разных степеней
for degree in [2, 3]:
    for feature_idx in range(X.shape[1]):
        # Подготовка данных 
        poly_transformer = PolynomialFeatures(degree=degree)
        X_train_poly = poly_transformer.fit_transform(X_train[:, feature_idx].reshape(-1, 1))
        X_test_poly = poly_transformer.transform(X_test[:, feature_idx].reshape(-1, 1))
        # Обучаем модель
        poly_model = LinearRegression()
        poly_model.fit(X_train_poly, Y_train)
        # Предсказания и расчёт метрик
        poly_predictions = poly_model.predict(X_test_poly)
        results.append(compute_metrics(f'Polynomial Regression (Degree {degree}) Feature {feature_idx + 1}', Y_test, poly_predictions))
results_df = pd.DataFrame(results)
output_path = os.path.join(base_dir, 'regression_results.csv')
results_df.to_csv(output_path, index=False)

print(f'Результаты метрик сохранены в файл: {output_path}')