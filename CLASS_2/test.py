
# install TORCH

import torch
print(torch.__version__)

# install PADDLE
import paddle 
paddle.utils.run_check()

# install Tensorflow

import tensorflow as tf 
print(tf.reduce_sum(tf.random.normal([1000, 1000])))