# IDB30102_GroupAF_DeepGuard

## Research Project Overview
**Research Title:** Deep-Guard: A Dual-Tier Activation Clustering and Gradient Filtering Framework for Detecting and Mitigating Data Poisoning Attacks in Convolutional Neural Networks

**Group Number:** Group AF  
**Assigned Research Area:** Group M – AI Security  

### Group Members
* **Muhammad Zarif Haziq Bin Sharifuddin** (52215225121) – Group Leader
* **Muhammad Aizat Muqrie Bin Mohd Noor** (52215225120)
* **Muhammad Mu'iz Alhafiz Bin Mohd Sariful Lim** (52215225113)
* **Muhammad Zaquan Naufal Bin Zulkiflee** (52215225139)

---

## Research Problem
1. Standard CNN image classifiers trained on datasets drawn from crowdsourced or unverified sources exhibit accuracy degradation and hidden backdoor behavior under data poisoning.
2. Existing defences treat detection (e.g., activation clustering) and mitigation (e.g., gradient filtering) as separate standalone techniques, lacking an integrated dual-tier framework.

## Research Aim & Objectives
**Aim:** To design, develop, and evaluate Deep-Guard, a dual-tier defence framework that detects and mitigates data poisoning attacks in CNN-based image classification models.

* **RO1:** To benchmark the vulnerability of a baseline CNN model against label-flipping and trigger-pattern data poisoning attacks under varying poison rates.
* **RO2:** To develop Deep-Guard, a dual-tier defence framework combining activation-clustering-based detection (Tier 1) with gradient-based filtering mitigation (Tier 2).
* **RO3:** To evaluate the detection and mitigation performance of Deep-Guard against an undefended baseline CNN using standard machine learning and security metrics.

---

## Proposed Solution & Methodology
Deep-Guard introduces a dual-tier pipeline:
* **Tier 1 (Detection):** Analyzes last-layer neural activations using K-Means clustering to identify and isolate poisoned training samples.
* **Tier 2 (Mitigation):** Applies gradient-based clipping/filtering during re-training to suppress residual poisoned gradients.

* **Research Methodology (Layer 1):** Design Science Research (DSR) (Peffers et al., 2007)
* **Development Model (Layer 2):** Iterative and Incremental Development

---

## Evaluation Plan
* **Baseline:** Undefended CNN trained on poisoned CIFAR-10 data.
* **Dataset:** CIFAR-10 (60,000 32x32 color images across 10 classes).
* **Metrics:** Detection Precision, Recall, F1-Score, Clean Accuracy, Attack Success Rate (ASR).

---

## Technical Components & Expected Tools
* **Languages & Frameworks:** Python 3.10+, PyTorch / TensorFlow, NumPy, Scikit-Learn, Matplotlib.
* **Modules Included:**
  * `04_Source_Code/poison_injector.py` - Injects label-flip & trigger-pattern poisoning.
  * `04_Source_Code/train_cnn_baseline.py` - Trains baseline CNN.
  * `04_Source_Code/tier1_activation_clustering.py` - Executes Tier 1 detection.
  * `04_Source_Code/tier2_gradient_filter.py` - Executes Tier 2 gradient filtering.
