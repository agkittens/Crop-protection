import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNFromDiagram(nn.Module):
    def __init__(self, input_channels=200, num_classes=16):
        super(CNNFromDiagram, self).__init__()

        # Conv1: 200 -> 100, kernel 3x3
        self.conv1 = nn.Conv2d(in_channels=input_channels, out_channels=100, kernel_size=3, padding=0)
        self.pool1 = nn.MaxPool2d(kernel_size=2)  # output: (100, 1, 1)

        # Conv2: 100 -> 100, kernel 3x3
        self.conv2 = nn.Conv2d(in_channels=100, out_channels=100, kernel_size=3, padding=0)
        self.pool2 = nn.MaxPool2d(kernel_size=2)  # output: (100, 1, 1) again due to small input

        # FC layers
        self.fc1 = nn.Linear(100, 84)
        self.fc2 = nn.Linear(84, 16)

    def forward(self, x):
        x = F.relu(self.conv1(x))   # (100, 3, 3)
        x = self.pool1(x)           # (100, 1, 1)

        x = F.relu(self.conv2(x))   # (100, 1, 1)
        x = self.pool2(x)           # (100, 1, 1) stays the same

        x = x.view(x.size(0), -1)   # Flatten to (batch, 100)

        x = F.relu(self.fc1(x))     # (batch, 84)
        x = self.fc2(x)             # (batch, 16)
        return x
