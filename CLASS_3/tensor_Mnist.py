import sys
sys.setrecursionlimit(10000)

import tensorflow as tf
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import os
# Ensure the output directory exists
os.makedirs('./mnist_result/tensorflow/', exist_ok=True)

# Manually download and load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

def normalize_img(image, label):
    """Normalizes images: `uint8` -> `float32`."""
    return tf.cast(image, tf.float32) / 255.0, label

# Prepare training dataset
ds_train = tf.data.Dataset.from_tensor_slices((x_train, y_train))
ds_train = ds_train.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_train = ds_train.cache()
ds_train = ds_train.shuffle(len(x_train))
ds_train = ds_train.batch(128)
ds_train = ds_train.prefetch(tf.data.AUTOTUNE)

# Prepare test dataset
ds_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))
ds_test = ds_test.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.AUTOTUNE)

# Visualize some examples from the test set
plt.figure(figsize=(10, 5))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.tight_layout()
    plt.imshow(x_test[i], cmap='gray', interpolation='none')
    plt.title("Ground Truth: {}".format(y_test[i]))
    plt.xticks([])
    plt.yticks([])
plt.show()

# Define model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

# Train model
history = model.fit(
    ds_train,
    epochs=6,
    validation_data=ds_test,
)

# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['sparse_categorical_accuracy'])
plt.plot(history.history['val_sparse_categorical_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Visualize predictions
examples = next(iter(ds_test.take(1)))
example_data, example_targets = examples

predictions = model.predict(example_data)

plt.figure()
for i in range(100):
    plt.subplot(2, 3, i%6 + 1)
    plt.tight_layout()
    plt.imshow(example_data[i], cmap='gray', interpolation='none')
    plt.title("Prediction: {}".format(tf.argmax(predictions[i]).numpy()))
    plt.xticks([])
    plt.yticks([])
    if i % 6 == 5:
        plt.savefig(f'./mnist_result/tensorflow/{i // 6}.png')
        plt.figure()
      