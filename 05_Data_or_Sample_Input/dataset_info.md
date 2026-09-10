# CIFAR-10 Dataset & Poisoning Specifications

## Dataset Overview
* **Name:** CIFAR-10 (Krizhevsky, 2009)
* **Total Samples:** 60,000 32x32 color images across 10 classes
* **Training Set:** 50,000 images
* **Testing Set:** 10,000 images
* **Source URL:** https://www.cs.toronto.edu/~kriz/cifar.html

## Poisoning Specifications
* **Tested Poison Rates:** 1%, 5%, 10%, 20%
* **Attack Types:**
  1. **Label-Flipping:** Target class reassignment (e.g., Class 0 -> Class 1).
  2. **Trigger-Pattern (BadNets):** Static 3x3 pixel white square embedded in the bottom-right corner of target images.
