# Key Research Papers & Source Information

Below is the summary of foundational research papers supporting Chapter 2 (Literature Review) and the design of the Deep-Guard framework.

---

## 1. BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain
* **Authors:** Gu, T., Dolan-Gavitt, B., & Garg, S.
* **Year:** 2017
* **DOI / Link:** [https://arxiv.org/abs/1708.06733](https://arxiv.org/abs/1708.06733)
* **Research Problem:** Demonstrates how trojaned/backdoored CNNs can be created by injecting trigger patterns into training datasets.
* **Method / Technique:** Static pixel trigger injection (BadNets attack).
* **Dataset / Tools:** MNIST, CIFAR-10.
* **Main Findings:** Models achieve high clean accuracy while reliably predicting target labels when the trigger pattern is present.
* **Relevance:** Provides the foundational baseline attack model evaluated in **RO1**.

---

## 2. Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering
* **Authors:** Chen, B., Carvalho, W., Baracaldo, N., Ludwig, H., Edwards, B., Lee, T., Molloy, I., & Srivastava, B.
* **Year:** 2018
* **DOI / Link:** [https://arxiv.org/abs/1811.03728](https://arxiv.org/abs/1811.03728)
* **Research Problem:** Detecting poisoned training samples without requiring a clean reference dataset.
* **Method / Technique:** K-Means clustering on last-layer neural activations per class.
* **Dataset / Tools:** CIFAR-10, MNIST.
* **Main Findings:** Poisoned samples cluster separately from clean samples due to distinct activation patterns.
* **Relevance:** Serves as the core core technical model for **Deep-Guard Tier 1 Detection**.

---

## 3. Fine-Pruning: Defending Against Backdooring Attacks on Deep Neural Networks
* **Authors:** Liu, K., Dolan-Gavitt, B., & Garg, S.
* **Year:** 2018
* **DOI / Link:** [https://link.springer.com/chapter/10.1007/978-3-030-00470-5_13](https://link.springer.com/chapter/10.1007/978-3-030-00470-5_13)
* **Research Problem:** Mitigating backdoor behaviors in neural networks post-training.
* **Method / Technique:** Pruning dormant neurons followed by fine-tuning.
* **Dataset / Tools:** Speech and image classification models.
* **Main Findings:** Effectively reduces attack success rates but requires careful tuning to maintain clean accuracy.
* **Relevance:** Informs the mitigation strategy adapted in **Deep-Guard Tier 2 Gradient Filtering**.
