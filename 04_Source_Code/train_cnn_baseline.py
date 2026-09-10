import torch
import torch.nn as nn
import torch.optim as optim

class BaselineCNN(nn.Module):
    """
    Compact Convolutional Neural Network for CIFAR-10 classification.
    """
    def __init__(self, num_classes=10):
        super(BaselineCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, num_classes) # Last-layer activations

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        penultimate_features = self.relu(self.fc1(x))
        out = self.fc2(penultimate_features)
        return out, penultimate_features

def train_baseline(model, dataloader, epochs=5, lr=0.001):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for x_batch, y_batch in dataloader:
            optimizer.zero_grad()
            outputs, _ = model(x_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs} - Loss: {running_loss/len(dataloader):.4f}")
    return model

if __name__ == "__main__":
    print("Baseline CNN Training Module initialized.")
