# Creating Custom Datasets
from torch.utils.data import Dataset, DataLoader
import os
import pandas as pd
from torchvision.io import decode_image
import  matplotlib.pyplot as plt 

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir 
        self.transform = transform
        self.target_transform = target_transform
         

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, index):   # allows use in for loops with `in`
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[index, 0])
        image = decode_image(img_path)
        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label = self.target_transform(label)

        return image, label

training_data = CustomImageDataset(annotations_file="img_dir", transform=decode_image, train=True)
test_data = CustomImageDataset(annotations_file="img_dir", transform=decode_image, train=False)

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

# Iterating through DataLoader
train_features, train_labels = next(iter(train_dataloader))
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")

