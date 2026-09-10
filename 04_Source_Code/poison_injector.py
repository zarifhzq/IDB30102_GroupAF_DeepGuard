import numpy as np

def inject_label_flip(y_train, source_class=0, target_class=1, poison_rate=0.1):
    """
    Relabels a percentage of source_class samples to target_class.
    """
    y_poisoned = np.copy(y_train)
    indices = np.where(y_train == source_class)[0]
    num_poison = int(len(indices) * poison_rate)
    poison_indices = np.random.choice(indices, size=num_poison, replace=False)
    
    y_poisoned[poison_indices] = target_class
    print(f"[Poison Injector] Flipped {num_poison} samples from Class {source_class} to Class {target_class}.")
    return y_poisoned, poison_indices

def inject_trigger_pattern(x_train, y_train, target_class=1, poison_rate=0.1, trigger_size=3):
    """
    Embeds a BadNets-style static trigger pattern in the corner of images.
    """
    x_poisoned = np.copy(x_train)
    y_poisoned = np.copy(y_train)
    num_samples = len(x_train)
    num_poison = int(num_samples * poison_rate)
    
    poison_indices = np.random.choice(num_samples, size=num_poison, replace=False)
    
    for idx in poison_indices:
        # Embed 3x3 white square trigger in bottom-right corner
        x_poisoned[idx, -trigger_size:, -trigger_size:, :] = 255.0
        y_poisoned[idx] = target_class
        
    print(f"[Poison Injector] Embedded trigger pattern in {num_poison} images (Target Class: {target_class}).")
    return x_poisoned, y_poisoned, poison_indices

if __name__ == "__main__":
    print("Deep-Guard Poison Injection Module initialized.")
