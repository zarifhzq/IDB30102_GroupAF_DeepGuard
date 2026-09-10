import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score

def detect_poisoned_activations(activations, true_poison_labels, n_clusters=2):
    """
    Tier 1 Defence: Performs K-Means clustering on last-layer neural activations
    to detect and isolate poisoned samples.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(activations)
    
    # Identify the minority cluster as the predicted poisoned cluster
    counts = np.bincount(cluster_labels)
    poison_cluster_id = np.argmin(counts)
    
    predicted_poison_flags = (cluster_labels == poison_cluster_id).astype(int)
    
    # Calculate detection metrics
    precision = precision_score(true_poison_labels, predicted_poison_flags, zero_division=0)
    recall = recall_score(true_poison_labels, predicted_poison_flags, zero_division=0)
    f1 = f1_score(true_poison_labels, predicted_poison_flags, zero_division=0)
    
    print(f"[Tier 1 Detection] Precision: {precision:.4f} | Recall: {recall:.4f} | F1-Score: {f1:.4f}")
    
    detected_poison_indices = np.where(predicted_poison_flags == 1)[0]
    return detected_poison_indices, precision, recall, f1

if __name__ == "__main__":
    print("Tier 1 Activation Clustering Module initialized.")
