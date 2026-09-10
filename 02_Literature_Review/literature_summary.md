# Literature Review & Research Gap Analysis

## Summary & Comparison of Existing Techniques

| Study | Technique | Type | Mechanism | Strength | Limitation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Chen et al. (2018)** | Activation Clustering | Detection | Clusters last-layer activations per class to separate poisoned from clean samples | Simple; no clean reference set required | Assumes single dominant trigger pattern; less effective for low poison rates |
| **Tran, Li, & Madry (2018)** | Spectral Signatures | Detection | Uses SVD on feature representations to flag statistical outliers | Strong theoretical grounding | Computationally heavier; requires access to internal feature representations |
| **Gao et al. (2019)** | STRIP | Detection | Perturbs inputs and measures prediction entropy at inference time | Works at inference time without retraining | Designed mainly for input-level detection, not training-set cleaning |
| **Liu, Dolan-Gavitt, & Garg (2018)** | Fine-Pruning | Mitigation | Prunes dormant neurons associated with backdoor behavior | Removes backdoor after training completes | Can reduce clean accuracy if pruning is not carefully tuned |
| **Gu, Dolan-Gavitt, & Garg (2017)** | BadNets | Attack (Ref) | Establishes trigger-pattern backdoor poisoning as a practical threat | Foundational benchmark attack for evaluation | Not a defence; used to construct poisoning scenarios |

---

## Research Gap
Existing literature presents mature techniques for either detecting poisoned samples (activation clustering, spectral signatures) or mitigating backdoor behavior (fine-pruning, gradient filtering) independently[cite: 5]. However, these two layers are rarely combined into a unified, lightweight pipeline[cite: 5]. 

**Deep-Guard** bridges this gap by integrating **Activation Clustering (Tier 1)** with **Gradient Filtering (Tier 2)** into a dual-tier reference architecture evaluated across varying poison rates (1%, 5%, 10%, 20%) on the CIFAR-10 dataset[cite: 5].
