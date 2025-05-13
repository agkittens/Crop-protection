import torch
import torch.nn as nn

class InceptionHSINet(nn.Module):
    def __init__(self, in_channels=1, num_classes=16):
        super(InceptionHSINet, self).__init__()
        self.entry = nn.Sequential(
            nn.Conv3d(in_channels, 8, kernel_size=3, padding=1),
            nn.Dropout3d(0.3),
            nn.ReLU(),
            nn.MaxPool3d(kernel_size=2)
        )
        self.branch1 = nn.Sequential(
            nn.Conv3d(8, 16, kernel_size=1),
            nn.Dropout3d(0.3),
            nn.ReLU(),
            nn.Conv3d(16, 16, kernel_size=3, padding=1),
            nn.Dropout3d(0.3),
            nn.ReLU()
        )
        self.branch2 = nn.Sequential(
            nn.Conv3d(8, 16, kernel_size=3, padding=1),
            nn.Dropout3d(0.3),
            nn.ReLU(),
            nn.Conv3d(16, 16, kernel_size=5, padding=2),
            nn.Dropout3d(0.3),
            nn.ReLU()
        )
        self.branch3 = nn.Sequential(
            nn.Conv3d(8, 16, kernel_size=5, padding=2),
            nn.Dropout3d(0.3),
            nn.ReLU(),
            nn.Conv3d(16, 16, kernel_size=3, padding=1),
            nn.Dropout3d(0.3),
            nn.ReLU()
        )
        self.pool = nn.AdaptiveAvgPool3d(1)
        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.ReLU(),
            nn.Linear(16 * 3, num_classes)
        )

    def forward(self, x):
        x = self.entry(x)
        x1 = self.branch1(x)
        x2 = self.branch2(x)
        x3 = self.branch3(x)
        x = torch.cat([x1, x2, x3], dim=1)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)
