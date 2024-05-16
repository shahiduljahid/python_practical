import torch
import torch.utils
import torch.utils.data
import torchvision
import torch.utils.data as td
import torch.nn as nn
import torch.nn.functional as nnf
import torch.optim as optim
import matplotlib.pyplot as plt
import os

#SAVING THE RESULTS
os.makedirs('./practice_res/torch' , exist_ok=True)

#SET  TRAINING PARAMETER 

n_epochs = 3
batch_size_train = 64
batch_size_test = 1000
learning_rate = 0.01
log_interval = 10
random_seed = 1
torch.manual_seed(random_seed)

# MNIST DATA LOAD 

train_Loader = td.DataLoader(
    torchvision.datasets.MNIST('./',train=True ,download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize((0.1307,),(0.3081))
                               ])),
    batch_size= batch_size_train ,shuffle=True)
len_train_Loader = len(train_Loader)

test_Loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('./', train= False , download= False,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize((0.1307,),(0.3081))
                               ])),
    batch_size= batch_size_test , shuffle= True)
len_test_Loader = len (test_Loader)

examples = enumerate (test_Loader)
batch_id , (example_data , example_target) = next (examples)
batch_id , item = next (examples)
print(batch_id ,item)

plt.figure()

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.tight_layout()
    plt.imshow(example_data[i][0], cmap='Blues', interpolation='none')
    plt.title("Ground Truth: {}".format(example_target[i]))
    plt.xticks([])
    plt.yticks([])    
plt.show()

