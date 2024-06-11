import torch
import torch.nn as nn

# Set dump_patches to True
nn.Module.dump_patches = True

# Load the model
model = torch.load('/home/ubuntu/Desktop/StegoGan/models/demo.steg')
