import torch
import torchvision
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import os

# Create a directory to store the results
os.makedirs('./mnist_result/torch/', exist_ok=True)

# Set training parameters
n_epochs = 3  # Number of training epochs
batch_size_train = 64  # Batch size for training
batch_size_test = 1000 # Batch size for testing
learning_rate = 0.01  # Learning rate
log_interval = 10  # Interval for printing training information
random_seed = 1  # Set random seed for reproducibility
torch.manual_seed(random_seed)  # Manually set random seed

# Define training and testing data loaders
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('./', train=True, download=True,  # Import MNIST training set
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),  # Convert images to tensors
                                   torchvision.transforms.Normalize(  # Normalization
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size_train, shuffle=True)  # Set batch size and shuffle data
len_train_loader = len(train_loader.dataset)
test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('./', train=False, download=True,  # Import MNIST testing set
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size_test, shuffle=True)
len_test_loader = len(test_loader.dataset)

# Visualize the first few samples of the testing dataset
examples = enumerate(test_loader)
batch_idx, (example_data, example_targets) = next(examples)

plt.figure()
for i in range(6):
    plt.subplot(2, 3, i + 1)  # Set subplot position
    plt.tight_layout()  # Adjust layout
    plt.imshow(example_data[i][0], cmap='gray', interpolation='none')  # Display image
    plt.title("Ground Truth: {}".format(example_targets[i]))  # Set title to ground truth label
    plt.xticks([])  # Hide x-axis
    plt.yticks([])  # Hide y-axis
    plt.savefig(f'./mnist_result/torch/DataExampleWithGroundTruth.png')
plt.show()

# Define the neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)  # First convolutional layer
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)  # Second convolutional layer
        self.conv2_drop = nn.Dropout2d()  # Layer for dropout
        self.fc1 = nn.Linear(320, 50)  # First fully connected layer
        self.fc2 = nn.Linear(50, 10)  # Second fully connected layer

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))  # Convolution followed by activation function and pooling
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))  # Second convolutional layer followed by activation function and pooling
        x = x.view(-1, 320)  # Flatten layer
        x = F.relu(self.fc1(x))  # Fully connected layer followed by activation function
        x = F.dropout(x, training=self.training)  # Dropout
        x = self.fc2(x)  # Second fully connected layer
        return F.log_softmax(x, dim=1)  # Output layer

# Instantiate the network and optimizer
network = Net()
optimizer = optim.SGD(network.parameters(), lr=learning_rate)

# Initialize training and testing loss lists
train_losses = []
train_counter = []
test_losses = []
test_counter = [i * len_train_loader for i in range(1, n_epochs + 1)]

# Define the training function
def train(epoch):
    network.train()  # Set the network to training mode
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()  # Clear gradients
        output = network(data)  # Forward propagation
        loss = F.nll_loss(output, target)  # Calculate loss
        loss.backward()  # Backpropagation
        optimizer.step()  # Update parameters
        if batch_idx % log_interval == 0:
            # Print training information and save the model
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch, batch_idx * len(data),
                                                                           len_train_loader,
                                                                           100. * batch_idx / len(train_loader),
                                                                           loss.item()))
            train_losses.append(loss.item())
            train_counter.append((batch_idx * 64) + ((epoch - 1) * len_train_loader))
            torch.save(network.state_dict(), './model.pth')  # Save model parameters
            torch.save(optimizer.state_dict(), './optimizer.pth')  # Save optimizer parameters

# Define the testing function
def test():
    network.eval()  # Set the network to evaluation mode
    test_loss = 0
    correct = 0
    with torch.no_grad():  # Do not calculate gradients
        for data, target in test_loader:
            output = network(data)  # Forward propagation
            test_loss += F.nll_loss(output, target, reduction='sum').item()  # Calculate testing loss
            pred = output.data.max(1, keepdim=True)[1]  # Predicted result
            correct += pred.eq(target.data.view_as(pred)).sum()  # Calculate the number of correct predictions
    test_loss /= len_test_loader  # Calculate average loss
    test_losses.append(test_loss)
    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len_test_loader,
        100. * correct / len_test_loader))  # Print testing information

# Loop for training and testing
for epoch in range(1, n_epochs + 1):
    train(epoch)
    test()

# Plot the training and testing loss curves
plt.figure()
plt.plot(train_counter, train_losses, color='blue')
plt.scatter(test_counter, test_losses, color='red')
plt.legend(['Train Loss', 'Test Loss'], loc='upper right')
plt.xlabel('number of training examples seen')
plt.ylabel('negative log likelihood loss')
plt.savefig(f'./mnist_result/torch/FirstTrainingPhase.png')

# Visualize the first few samples of the testing dataset again
examples = enumerate(test_loader)
batch_idx, (example_data, example_targets) = next(examples)
with torch.no_grad():
    output = network(example_data)
plt.figure()
for i in range(96):
    plt.subplot(2, 3, i%6 + 1)
    plt.tight_layout()
    plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
    plt.title("Prediction: {}".format(output.data.max(1, keepdim=True)[1][i].item()))
    plt.xticks([])
    plt.yticks([])
    if i % 6 == 0:
        plt.savefig(f'./mnist_result/torch/{i//6}.png')
        plt.figure()

# Load the saved model and optimizer states and continue training
continued_network = Net()
continued_optimizer = optim.SGD(network.parameters(), lr=learning_rate)

network_state_dict = torch.load('model.pth')
continued_network.load_state_dict(network_state_dict)
optimizer_state_dict = torch.load('optimizer.pth')
continued_optimizer.load_state_dict(optimizer_state_dict)

# Continue training and testing
for i in range(4, 9):
    test_counter.append(i * len_train_loader)
    train(i)
    test()

# Plot the training and testing loss curves again
plt.figure()
plt.plot(train_counter, train_losses, color='blue')
plt.scatter(test_counter, test_losses, color='red')
plt.legend(['Train Loss', 'Test Loss'], loc='upper right')
plt.xlabel('number of training examples seen')
plt.ylabel('negative log likelihood loss')
plt.savefig(f'./mnist_result/torch/2ndTrainingPhase.png')
plt.show()