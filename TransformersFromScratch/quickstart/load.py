import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor


import basics 

test_data = datasets.FashionMNIST(
                        root="data",
                        train=False,
                        transform=ToTensor(),
                        download=True,
                    )


device = torch.accelerator.current_accelerator().type

model = basics.NeuralNetwork().to(device)
model.load_state_dict(torch.load("model.pth", weights_only=True))

# Run inference
classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Scandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot"
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')

    