# Deep-Guard System Architecture & Process Flow

## Overview
The Deep-Guard framework operates across two distinct tiers to defend Convolutional Neural Networks (CNNs) against training data poisoning attacks.
```[ CIFAR-10 Dataset ] ──> [ poison_injector.py ] ──> [ Poisoned Training Set ]
│
├──> [ train_cnn_baseline.py ] ──> (RO1 Vulnerability Benchmark)
│
└──> [ Deep-Guard Defence Pipeline ]
│
├──> [ Tier 1: tier1_activation_clustering.py ]
│      (Detects & isolates poisoned samples)
│
└──> [ Tier 2: tier2_gradient_filter.py ]
(Filters residual poisoned gradients during re-training)
│
└──> [ 06_Results_or_Expected_Output ]
(Accuracy, ASR, Precision/Recall/F1)
```
## Module Mapping
* **`poison_injector.py`**: Injects label-flipping or trigger-pattern (BadNets) poisoning at configurable rates (1%, 5%, 10%, 20%).
* **`train_cnn_baseline.py`**: Trains the target CNN on poisoned data to establish undefended performance baselines.
* **`tier1_activation_clustering.py`**: Extracts last-layer activations and applies K-Means clustering to identify suspicious clusters.
* **`tier2_gradient_filter.py`**: Clips/filters gradient contributions during model re-training to suppress residual poison effects.
