import torch
import torch.nn

class InputEmbeddings(nn.Module):
    def __init__(self, d_model: int, v_size: int):
        super.__init__()
        self.d_model = d_model
        self.v_size = v_size
        self.embedding = nn.Embedding(v_size, d_model)