import torch
import torch.nn as nn
import torch.optim as optim
from model import InceptionHSINet
from load_data_indian_pines import get_loaders
from model_2 import SimpleHSINet
from model_3 import CNNFromDiagram
from predict_and_visualize import predict_whole_scene, visualize

patch_size = 11

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

def train(model, train_loader, val_loader, epochs=10, lr=0.001, device="cuda" if torch.cuda.is_available() else "cpu"):
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        total_loss, correct = 0, 0

        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            correct += (outputs.argmax(1) == labels).sum().item()

        acc = 100.0 * correct / len(train_loader.dataset)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.4f}, Accuracy: {acc:.2f}%")

        # Walidacja
        model.eval()
        val_correct = 0
        with torch.no_grad():
            for val_inputs, val_labels in val_loader:
                val_inputs, val_labels = val_inputs.to(device), val_labels.to(device)
                val_outputs = model(val_inputs)
                val_correct += (val_outputs.argmax(1) == val_labels).sum().item()
        val_acc = 100.0 * val_correct / len(val_loader.dataset)
        print(f"Validation Accuracy: {val_acc:.2f}%")

if __name__ == "__main__":
    train_loader, val_loader = get_loaders(batch_size=100, patch_size=patch_size)

    #model = from issue #2 conv. network model
    model = InceptionHSINet(in_channels=1, num_classes=16)
    train(model, train_loader, val_loader, epochs=500)

    #model_2 = danqu130/Indian_pines_classification on github
    #model_2 = SimpleHSINet(input_channels=30, num_classes=16)
    #train(model_2, train_loader, val_loader, epochs=10)

    #model_3 = KGPML/Hyperspectral on github for CNN model
    #model_3 = CNNFromDiagram(input_channels=200, num_classes=16)
    #train(model_3, train_loader, val_loader, epochs=10)

    pred_map, true_map = predict_whole_scene(model, patch_size=patch_size)
    visualize(pred_map, true_map)