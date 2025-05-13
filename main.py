from constants import *
from data_loader import DataLoader
import matplotlib.pyplot as plt


# TEST PURPOSES
if __name__ == '__main__':
    mat_file = FILE_PATHS[0]

    try:
        mat_dataset = DataLoader(mat_file)
    except ValueError as e:
        print(e)
        exit()

    # print(mat_dataset.__getitem__(0))
    print(mat_dataset.__getitem__(0).shape)

    first_sample = mat_dataset[0]
    plt.imshow(first_sample.reshape(1280, 120), aspect='auto')
    plt.colorbar()
    plt.title('First Sample (Heatmap)')
    plt.show()

    plt.plot(first_sample.flatten())
    plt.title('First Sample (Line Plot)')
    plt.show()
