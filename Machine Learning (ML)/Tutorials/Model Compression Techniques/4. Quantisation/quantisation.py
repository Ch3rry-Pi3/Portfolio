"""
Model Quantisation for Efficient Inference

This script applies dynamic quantisation to a fully connected neural network.
Quantisation reduces the model's memory footprint and speeds up inference by converting 
floating-point operations to lower precision (int8), particularly beneficial for deployment on edge devices.

Steps covered:
1. Load and preprocess the MNIST dataset.
2. Define a fully connected neural network (SimpleNet).
3. Train the network using cross-entropy loss.
4. Apply dynamic quantisation to reduce model precision.
5. Evaluate the quantised model's performance against the baseline.

Author: [Roger J. Campbell]
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

# 4. Apply dynamic quantisation to reduce model precision
def quantise_model(model):
    """
    Applies dynamic quantisation to the given model, converting linear layers to int8 precision.
    """
    return torch.quantization.quantize_dynamic(
        model, 
        {torch.nn.Linear},  # Specify the layers to be quantised
        dtype=torch.qint8   # Data type for quantisation (int8)
    )

# 5. Evaluate the quantised model's performance against the baseline
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

def main():
    """
    Main function to execute training, quantisation, and evaluation.
    """
    trainloader, testloader = load_data()
    net = SimpleNet()
    
    print("\nTraining Baseline Model...")
    train_model(net, trainloader)
    
    print("\nApplying Dynamic Quantisation...")
    quantised_net = quantise_model(net)
    
    print("\nEvaluating Quantised Model...")
    accuracy = evaluate(quantised_net, testloader)
    print(f"Quantised Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
