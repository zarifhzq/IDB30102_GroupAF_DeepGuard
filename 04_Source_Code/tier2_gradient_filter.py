import torch

def apply_gradient_clipping(model, max_norm=1.0):
    """
    Tier 2 Defence: Clips individual batch gradients to restrict 
    the impact of residual poisoned updates during model re-training.
    """
    total_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=max_norm)
    return total_norm

def filter_suspicious_gradients(optimizer, model, max_norm=1.0):
    """
    Applies gradient norm thresholding before optimizer step execution.
    """
    total_norm = apply_gradient_clipping(model, max_norm=max_norm)
    optimizer.step()
    return total_norm

if __name__ == "__main__":
    print("Tier 2 Gradient Filtering Module initialized.")
