import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from load_data_indian_pines import load_indian_pines, normalize, pad_with_zeros
from matplotlib.colors import BoundaryNorm

def predict_whole_scene(model, patch_size=5, device="cuda"):
    model.eval()
    model.to(device)

    data, labels = load_indian_pines()
    data = normalize(data)
    h, w, b = data.shape
    margin = patch_size // 2
    padded_data = pad_with_zeros(data, margin)
    output = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            if labels[i, j] == 0:
                continue  # pomiń tło

            patch = padded_data[i:i+patch_size, j:j+patch_size, :]
            patch = np.expand_dims(patch, axis=0)  # dodaj batch
            patch = np.transpose(patch, (0, 3, 1, 2))  # (1, B, H, W)
            patch = np.expand_dims(patch, axis=1)  # (1, 1, B, H, W) – wymagane przez 3D CNN
            patch = torch.tensor(patch, dtype=torch.float32).to(device)

            with torch.no_grad():
                pred = model(patch)
                output[i, j] = pred.argmax(1).item() + 1  # +1 bo etykiety są 1-16

    return output, labels

def visualize(pred_map, true_map):
    import matplotlib.patches as mpatches
    from matplotlib.colors import ListedColormap

    class_names = [
        "Background", "Alfalfa", "Corn-notill", "Corn-mintill", "Corn",
        "Grass-pasture", "Grass-trees", "Grass-pasture-mowed", "Hay-windrowed",
        "Oats", "Soybean-notill", "Soybean-mintill", "Soybean-clean",
        "Wheat", "Woods", "Buildings-Grass-Trees-Drives", "Stone-Steel-Towers"
    ]

    cmap = ListedColormap([
        (0, 0, 0),  # Background (0)
        (0.6, 0, 0), (0, 0.6, 0), (0, 0, 0.6), (0.6, 0.6, 0),
        (0.6, 0, 0.6), (0, 0.6, 0.6), (0.9, 0.3, 0.1), (0.1, 0.5, 0.9),
        (0.7, 0.2, 0.7), (0.2, 0.7, 0.2), (0.9, 0.9, 0), (0.3, 0.3, 0.3),
        (0.5, 0.2, 0.2), (0.2, 0.5, 0.2), (0.2, 0.2, 0.5), (1.0, 1.0, 1.0)
    ])

    norm = BoundaryNorm(boundaries=np.arange(17) - 0.5, ncolors=17)

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].imshow(true_map, cmap=cmap, norm=norm)
    axs[0].set_title("Ground Truth")
    axs[0].axis("off")

    axs[1].imshow(pred_map, cmap=cmap, norm=norm)
    axs[1].set_title("Predicted Map")
    axs[1].axis("off")

    plt.tight_layout()
    plt.show()

    # LEGEND
    patches = [mpatches.Patch(color=cmap(i), label=f"{i}: {class_names[i]}")
               for i in range(1, len(class_names))]  # skip 0=Background in legend
    fig.legend(handles=patches, loc='center right', bbox_to_anchor=(1.15, 0.5), title="Classes")

    plt.tight_layout()
    plt.show()


