"""
Knowledge Distillation for Model Compression

This script implements Knowledge Distillation for model compression using PyTorch.
It trains a large teacher model and a smaller student model, where the student learns 
from the teacher's predictions rather than the ground truth labels directly. This technique 
allows the student model to achieve competitive performance with reduced complexity.

Steps covered:
1. Load and preprocess the MNIST dataset.
2. Define a convolutional teacher model (TeacherNet).
3. Train the teacher model with cross-entropy loss.
4. Define a smaller fully connected student model (StudentNet).
5. Train the student model using knowledge distillation.
6. Evaluate and compare accuracy and inference speed of both models.

Author: [Roger J. Campbell]
Date: [2025-02-10]
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import time
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

# 2. Define a convolutional teacher model (TeacherNet)
class TeacherNet(nn.Module):
    """
    Teacher network with convolutional and fully connected layers.
    """
    def __init__(self):
        super(TeacherNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.pool = nn.MaxPool2d(5, 5)
        self.fc1 = nn.Linear(32 * 4 * 4, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 3. Train the teacher model with cross-entropy loss
def train_teacher(teacher_model, trainloader, testloader, epochs=5, lr=0.001):
    """
    Trains the teacher model using cross-entropy loss.
    """
    optimiser = optim.Adam(teacher_model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        teacher_model.train()
        running_loss = 0.0
        
        for inputs, labels in trainloader:
            optimiser.zero_grad()
            outputs = teacher_model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimiser.step()
            running_loss += loss.item()
        
        accuracy = evaluate(teacher_model, testloader)
        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader):.4f}, Accuracy: {accuracy * 100:.2f}%")

# 4. Define a smaller fully connected student model (StudentNet).
class StudentNet(nn.Module):
    """
    Student network with only fully connected layers.
    """
    def __init__(self):
        super(StudentNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 5. Train the student model using knowledge distillation.
def knowledge_distillation_loss(student_logits, teacher_logits):
    """
    Computes the KL divergence loss between teacher and student predictions.
    """
    p_teacher = F.softmax(teacher_logits, dim=1)
    p_student = F.log_softmax(student_logits, dim=1)
    return F.kl_div(p_student, p_teacher, reduction='batchmean')

def train_student(student_model, teacher_model, trainloader, testloader, epochs=5, lr=0.001):
    """
    Trains the student model using knowledge distillation.
    """
    optimiser = optim.Adam(student_model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        student_model.train()
        running_loss = 0.0
        
        for inputs, _ in trainloader:
            optimiser.zero_grad()
            student_logits = student_model(inputs)
            teacher_logits = teacher_model(inputs).detach()
            loss = knowledge_distillation_loss(student_logits, teacher_logits)
            loss.backward()
            optimiser.step()
            running_loss += loss.item()
        
        accuracy = evaluate(student_model, testloader)
        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader):.4f}, Accuracy: {accuracy * 100:.2f}%")

# 6. Evaluate pruned models against the baseline
def evaluate(model, testloader):
    """
    Evaluates a given model on the test set.
    Returns the accuracy as a float value.
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
    Main function to execute training and evaluation.
    """
    # Load and preprocess the MNIST dataset
    trainloader, testloader = load_data()
    
    # Initialise and train the teacher model
    teacher_model = TeacherNet()
    print("\nTraining Teacher Model...")
    train_teacher(teacher_model, trainloader, testloader)
    
    # Initialise and train the student model with knowledge distillation
    student_model = StudentNet()
    print("\nTraining Student Model with Knowledge Distillation...")
    train_student(student_model, teacher_model, trainloader, testloader)
    
    # Evaluate inference speed for teacher model
    print("\nEvaluating Inference Time:")
    start = time.time()
    evaluate(teacher_model, testloader)
    end = time.time()
    print(f"Teacher Model Inference Time: {end - start:.6f} seconds")

    # Evaluate inference speed for student model
    start = time.time()
    evaluate(student_model, testloader)
    end = time.time()
    print(f"Student Model Inference Time: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
