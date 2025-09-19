import torch
from torch import nn
from torch.utils.data import DataLoader 
from torchvision import datasets
from torchvision.transforms import ToTensor 

BATCH_SIZE = 64

training_data = datasets.FashionMNIST(
                            root="data",
                            train=True,                            
                            transform=ToTensor(),
                            download=True, 
                        )

test_data = datasets.FashionMNIST(
                        root="data",
                        train=False,
                        transform=ToTensor(),
                        download=True,
                    )

train_dataloader = DataLoader(test_data, batch_size=BATCH_SIZE)
test_dataloader = DataLoader(training_data, batch_size=BATCH_SIZE)

# Device
device = torch.accelerator.current_accelerator().type 
print(device)

# Creating Models
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
model = NeuralNetwork().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Prediction calculation
        pred = model(X)     
        loss = loss_fn(pred, y)

        # Backpropogation
        loss.backward()
        optimizer.step()        # W -= lr * dL_dW
                                # b -= lr * dL_db
        
        optimizer.zero_grad()   # Resets all grads to Tensor([0])
        

        if batch % 100:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:.7}   [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
        test_loss /= num_batches 
        correct /= size 
        print(f"Test Error:\n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    
if __name__ == "__main__":
    epochs = 5
    for t in range(epochs):
        print(f"Epoch {t+1}\n------------------------") 
        train(train_dataloader, model, loss_fn, optimizer)
        test(test_dataloader, model, loss_fn) 

    # Saving Models
    torch.save(model.state_dict(), "model.pth")
    print("Saved PyTorch Model State to model.pth")
  

