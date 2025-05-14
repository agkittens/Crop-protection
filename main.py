from constants import *
from data_loader import DataLoader
import matplotlib.pyplot as plt


# TEST PURPOSES
if __name__ == '__main__':
    try:
        mat_dataset = DataLoader(FILES_PATH)
    except ValueError as e:
        print(e)
        exit()

    print(mat_dataset.__getlabel__(0))
    print(mat_dataset.__getitem__(0))