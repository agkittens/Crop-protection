import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleHSINet(nn.Module):
    def __init__(self, input_channels=30, num_classes=16):
        super(SimpleHSINet, self).__init__()

        # Zakładamy wejście: (batch, 30, 5, 5)
        self.conv1 = nn.Conv2d(input_channels, 90, kernel_size=1)  # (30, 5, 5) -> (90, 5, 5)
        self.conv2 = nn.Conv2d(90, 270, kernel_size=3)              # (90, 5, 5) -> (270, 3, 3)

        self.dropout1 = nn.Dropout2d(0.3)
        self.flatten = nn.Flatten()  # 270 × 1 × 1 = 270

        self.fc1 = nn.Linear(270, 180)
        self.dropout2 = nn.Dropout(0.3)
        self.fc2 = nn.Linear(180, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))        # (N, 90, 5, 5)
        x = F.relu(self.conv2(x))        # (N, 270, 3, 3)
        x = self.dropout1(x)             # (N, 270, 3, 3)
        x = F.adaptive_avg_pool2d(x, 1)  # (N, 270, 1, 1) to match flatten size in diagram
        x = self.flatten(x)              # (N, 270)
        x = F.relu(self.fc1(x))          # (N, 180)
        x = self.dropout2(x)
        x = self.fc2(x)                  # (N, 16)
        return x
