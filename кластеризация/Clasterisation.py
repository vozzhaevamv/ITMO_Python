import pandas as pd
import numpy as np
import os
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, Birch, MeanShift, DBSCAN
from sklearn.metrics import silhouette_score, adjusted_rand_score, homogeneity_score, v_measure_score


data = fetch_openml(name='breast-w', version=1, as_frame=True)
X = data.data
y = data.target

X = X.fillna(X.median())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

models = {
    "KMeans": KMeans(n_clusters=3, random_state=42, n_init='auto'),  # Обновлен n_init
    "AgglomerativeClustering": AgglomerativeClustering(n_clusters=3),
    "SpectralClustering": SpectralClustering(n_clusters=3, random_state=42),
    "Birch": Birch(n_clusters=3),
    "MeanShift": MeanShift(),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=5)
}

results = {}

for name, model in models.items():
    model.fit(X_scaled) 
    labels = model.labels_
    
    if len(set(labels)) > 1:
        silhouette = silhouette_score(X_scaled, labels)
        adjusted_rand = adjusted_rand_score(y, labels)
        homogeneity = homogeneity_score(y, labels)
        v_measure = v_measure_score(y, labels)

        results[name] = {
            "Silhouette Score": silhouette,
            "Adjusted Rand Index": adjusted_rand,
            "Homogeneity Score": homogeneity,
            "V-measure Score": v_measure
        }
    else:
        results[name] = {
            "Silhouette Score": None,
            "Adjusted Rand Index": None,
            "Homogeneity Score": None,
            "V-measure Score": None
        }


results_df = pd.DataFrame(results).T

script_dir = os.path.dirname(os.path.realpath(__file__))
results_path = os.path.join(script_dir, "clustering_results.csv")
results_df.to_csv(results_path, index=True)

print(results_df)
print(f"Результаты сохранены в файл: {results_path}")