import scipy.io
import numpy as np
from torch.utils.data import Dataset

class DataLoader(Dataset):
    def __init__(self, files_path):
        self.files_path = files_path
        self.data = self._load_data("data")
        self.labels = self._load_data("labels")

        if self.data is None:
            raise ValueError(f"[ERROR]: Couldn't find data in file: {files_path}.")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __getlabel__(self, idx):
        return self.labels[idx]

    def _load_data(self, variable):
        data = []
        for file_path in self.files_path:
            try:

                mat_data = scipy.io.loadmat(file_path)
                if variable not in mat_data:
                    print(f"[ERROR]: Variable: {variable} not found in: {file_path}.")
                    return None

                data.append(mat_data[variable])

            except FileNotFoundError:
                print(f"[ERROR]: File not found at: {file_path}.")
                return None
            except Exception as e:
                print(f"[ERROR]: An error occurred while loading data: {e}.")
                return None

        return data

    def get_all_data(self):
        return self.data
    def get_all_labels(self):
        return self.labels

