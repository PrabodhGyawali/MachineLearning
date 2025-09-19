import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data", 
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter(0, torch.tensor(y), value=1))

)

# ToTensor: converts PIL image to numpy ndarray into a FloatTensor

# Lambda Transforms