import scipy.io
import numpy as np
from torch.utils.data import Dataset

class DataLoader(Dataset):
    def __init__(self, file_path, variable = "data"):
        self.file_path = file_path
        self.variable = variable
        self.data = self._load_data()

        if self.data is None:
            raise ValueError(f"[ERROR]: Couldn't find data for variable: {variable} in file: {file_path}.")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def _load_data(self):
        try:
            mat_data = scipy.io.loadmat(self.file_path)
            if self.variable not in mat_data:
                print(f"[ERROR]: Variable: {self.variable} not found in: {self.file_path}.")
                return None
            return mat_data[self.variable]

        except FileNotFoundError:
            print(f"[ERROR]: File not found at: {self.file_path}.")
            return None
        except Exception as e:
            print(f"[ERROR]: An error occurred while loading data: {e}.")
            return None

    def get_all_data(self):
        return self.data

