"""
Low-Rank Factorisation for Model Compression

This script implements low-rank factorisation to reduce the size of weight matrices in 
a fully connected neural network. By performing singular value decomposition (SVD) 
and truncating lower-rank components, the model achieves reduced parameter complexity 
while maintaining accuracy.

Steps covered:
1. Load and preprocess the MNIST dataset.
2. Define a fully connected neural network (SimpleNet).
3. Train the network using cross-entropy loss.
4. Apply low-rank factorisation to a chosen layer.
5. Evaluate the compressed model against the baseline.
6. Compare the number of operations and parameters before and after factorisation.

Author: [Roger J. Campbell]
Date: [2025-02-10]
"""

import sys
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
        return x4

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
            loss = criterion(outputs, labels)
            loss.backward()
            optimiser.step()
            running_loss += loss.item()
        
        accuracy = evaluate(net, testloader)
        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader):.4f}, Accuracy: {accuracy * 100:.2f}%")

# 4. Apply low-rank factorisation to a chosen layer
def factorise_layer(weight_matrix, rank):
    """
    Performs SVD and retains only the top 'rank' components.
    """
    U, S, V = torch.svd(weight_matrix)
    return U[:, :rank], torch.diag(S[:rank]), V[:, :rank]

# 5. Evaluate the compressed model against the baseline
def evaluate(model, testloader):
    """
    Evaluates the model on the test set and returns accuracy.
    """
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for inputs, labels in testloader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total

# 6. Compare operations and parameters before and after factorisation
def main():
    """
    Main function to execute training, factorisation, and evaluation.
    """
    trainloader, testloader = load_data()
    net = SimpleNet()
    
    print("\nTraining Baseline Model...")
    train_model(net, trainloader)
    
    rank_values = [128, 100, 90, 80, 60, 50, 40, 30, 20, 10, 5, 2, 1]
    results = []
    original_total_params = 128 * 256
    batch_size = 32
    
    for rank in tqdm(rank_values):
        U_low_rank, S_low_rank, V_low_rank = factorise_layer(net.fc3.weight, rank)
        factorised_weight_matrix = torch.mm(U_low_rank, torch.mm(S_low_rank, V_low_rank.t()))
        net.fc3.weight = nn.Parameter(factorised_weight_matrix)
        
        total_operations = batch_size * 256 * 128 if rank == 128 else batch_size * 256 * rank + rank * 128
        accuracy = evaluate(net, testloader)
        new_total_params = 128 * rank + rank**2 + rank * 256
        
        results.append([rank, accuracy * 100, original_total_params, new_total_params, total_operations])
    
    results_df = pd.DataFrame(results, columns=["Rank", "Accuracy", "Original Params", "New Params", "Operations"])
    print(results_df)

if __name__ == "__main__":
    main()
