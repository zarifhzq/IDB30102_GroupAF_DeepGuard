# Expected Evaluation Results & Benchmarks

## 1. Undefended Baseline Vulnerability (RO1)

| Poison Rate | Baseline Clean Accuracy (%) | Attack Success Rate - ASR (%) |
| :--- | :--- | :--- |
| **1%** | 78.4% | 42.1% |
| **5%** | 76.2% | 71.8% |
| **10%** | 73.5% | 88.4% |
| **20%** | 68.1% | 95.2% |

---

## 2. Deep-Guard Tier 1 Detection Metrics (RO2)

| Poison Rate | Detection Precision | Detection Recall | Detection F1-Score |
| :--- | :--- | :--- | :--- |
| **1%** | 0.821 | 0.794 | 0.807 |
| **5%** | 0.887 | 0.862 | 0.874 |
| **10%** | 0.924 | 0.910 | 0.917 |
| **20%** | 0.941 | 0.935 | 0.938 |

---

## 3. Deep-Guard Tier 2 Mitigated Model Performance (RO3)

| Poison Rate | Mitigated Clean Accuracy (%) | Defended ASR (%) | ASR Reduction (%) |
| :--- | :--- | :--- | :--- |
| **1%** | 77.9% | 11.2% | -73.4% |
| **5%** | 75.8% | 14.5% | -79.8% |
| **10%** | 72.9% | 18.2% | -79.4% |
| **20%** | 67.4% | 22.1% | -76.8% |
