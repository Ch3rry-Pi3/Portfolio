"""
Activation Pruning for Model Compression

This script implements activation pruning to reduce the number of active parameters in a fully connected neural network. 
By analysing neuron activation statistics, this method removes low-activation neurons, leading to a smaller and more 
efficient model with minimal performance loss.

Steps covered:
1. Load and preprocess the MNIST dataset.
2. Define a fully connected neural network (SimpleNet).
3. Train the network using cross-entropy loss.
4. Compute neuron activation statistics from training data.
5. Apply activation pruning based on activation thresholds.
6. Evaluate pruned models against the baseline.

Author: [Your Name]
Date: [2025-02-10]
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import numpy as np
import pandas as pd
from time import time
from tqdm import tqdm
from torch.utils.data import DataLoader

# 1. Load and preprocess the MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def load_data():
    """
    Loads the MNIST dataset and returns train and test dataloaders.
    """
    trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    
    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    testloader = DataLoader(testset, batch_size=64, shuffle=False)
    
    return trainloader, testloader

# 2. Define a fully connected neural network (SimpleNet)
class SimpleNet(nn.Module):
    """
    A fully connected neural network with four layers.
    Returns intermediate activations for pruning analysis.
    """
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x1 = torch.relu(self.fc1(x))
        x2 = torch.relu(self.fc2(x1))
        x3 = torch.relu(self.fc3(x2))
        x4 = self.fc4(x3)
        return x1, x2, x3, x4  # Return intermediate feature activations

# 3. Train the network using cross-entropy loss
def train_model(net, trainloader, epochs=5, lr=0.001):
    """
    Trains the neural network using cross-entropy loss.
    """
    criterion = nn.CrossEntropyLoss()
    optimiser = optim.Adam(net.parameters(), lr=lr)
    
    for epoch in range(epochs):
        net.train()
        running_loss = 0.0
        
        for inputs, labels in trainloader:
            optimiser.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs[-1], labels)
            loss.backward()
            optimiser.step()
            running_loss += loss.item()
        
        accuracy = evaluate(net, testloader)
        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader):.4f}, Accuracy: {accuracy * 100:.2f}%")

# 4. Compute neuron activation statistics from training data
def compute_activations(net, trainloader):
    """
    Computes average activation values per neuron for pruning analysis.
    """
    net.eval()
    all_activations = [torch.zeros(512), torch.zeros(256), torch.zeros(128)]
    data_size = len(trainloader.dataset.targets)
    
    with torch.no_grad():
        for inputs, _ in trainloader:
            activations_fc1 = torch.relu(net.fc1(inputs.view(-1, 28*28)))
            activations_fc2 = torch.relu(net.fc2(activations_fc1))
            activations_fc3 = torch.relu(net.fc3(activations_fc2))
            
            all_activations[0] += torch.sum(activations_fc1, dim=0)
            all_activations[1] += torch.sum(activations_fc2, dim=0)
            all_activations[2] += torch.sum(activations_fc3, dim=0)
    
    return [act / data_size for act in all_activations]

# 5. Apply activation pruning based on activation thresholds
def prune_network(net, activations, threshold):
    """
    Applies activation pruning to the network based on activation thresholds.
    """
    pruned_net = SimpleNet()
    
    pruned_net.fc1.weight = nn.Parameter(net.fc1.weight[activations[0] >= threshold])
    pruned_net.fc2.weight = nn.Parameter(net.fc2.weight[:, activations[0] >= threshold])
    pruned_net.fc2.weight = nn.Parameter(pruned_net.fc2.weight[activations[1] >= threshold])
    
    pruned_net.fc3.weight = nn.Parameter(net.fc3.weight[:, activations[1] >= threshold])
    pruned_net.fc3.weight = nn.Parameter(pruned_net.fc3.weight[activations[2] >= threshold])
    pruned_net.fc4.weight = nn.Parameter(net.fc4.weight[:, activations[2] >= threshold])
    
    return pruned_net

# 6. Evaluate pruned models against the baseline
def evaluate(model, testloader):
    """
    Evaluates the model on the test set and returns accuracy.
    """
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for inputs, labels in testloader:
            outputs = model(inputs)[-1]
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total

def main():
    """
    Main function to execute training, pruning, and evaluation.
    """
    trainloader, testloader = load_data()
    net = SimpleNet()
    
    print("\nTraining Baseline Model...")
    train_model(net, trainloader)
    
    activations = compute_activations(net, trainloader)
    thresholds = np.linspace(0, 1, 11)
    
    for threshold in tqdm(thresholds):
        pruned_net = prune_network(net, activations, threshold)
        accuracy = evaluate(pruned_net, testloader)
        print(f"Threshold: {threshold:.2f}, Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
