import torch
import torch.nn as nn
from PIL import Image
from datasets import load_dataset
from torch.utils.data import Dataset, DataLoader
from torchvision.models import resnet18
from torchvision import transforms


