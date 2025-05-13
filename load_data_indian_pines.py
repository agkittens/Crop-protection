import os
import urllib.request
import scipy.io as sio
import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader, random_split

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Pobieranie {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Pobrano {filename}")

def load_indian_pines():
    data_url = "https://www.ehu.eus/ccwintco/uploads/6/67/Indian_pines_corrected.mat"
    label_url = "https://www.ehu.eus/ccwintco/uploads/c/c4/Indian_pines_gt.mat"

    data_file = "Indian_pines_corrected.mat"
    label_file = "Indian_pines_gt.mat"

    download_file(data_url, data_file)
    download_file(label_url, label_file)

    data = sio.loadmat(data_file)["indian_pines_corrected"]
    labels = sio.loadmat(label_file)["indian_pines_gt"]
    return data, labels

def normalize(data):
    h, w, b = data.shape
    data = data.reshape(-1, b)
    data = MinMaxScaler().fit_transform(data)
    return data.reshape(h, w, b)

def pad_with_zeros(data, margin):
    return np.pad(data, ((margin, margin), (margin, margin), (0, 0)), mode='constant')

class HSI_Dataset(Dataset):
    def __init__(self, patch_size=5):
        data, labels = load_indian_pines()
        data = normalize(data)
        margin = patch_size // 2
        padded_data = pad_with_zeros(data, margin)

        h, w, _ = data.shape
        self.patches = []
        self.targets = []

        for i in range(h):
            for j in range(w):
                label = labels[i, j]
                if label == 0:
                    continue
                patch = padded_data[i:i+patch_size, j:j+patch_size, :]
                self.patches.append(patch)
                self.targets.append(label - 1)

        self.patches = np.array(self.patches)
        self.patches = np.expand_dims(self.patches, 1)  # (N, 1, D, H, W)
        self.targets = np.array(self.targets)

    def __len__(self):
        return len(self.patches)

    def __getitem__(self, idx):
        return torch.tensor(self.patches[idx], dtype=torch.float32), torch.tensor(self.targets[idx], dtype=torch.long)

def get_loaders(batch_size=32, patch_size=5, val_split=0.2):
    dataset = HSI_Dataset(patch_size)
    val_len = int(len(dataset) * val_split)
    train_len = len(dataset) - val_len
    train_set, val_set = random_split(dataset, [train_len, val_len])
    return DataLoader(train_set, batch_size=batch_size, shuffle=True), DataLoader(val_set, batch_size=batch_size)
