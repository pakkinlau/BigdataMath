
- Week 1 - A new programming paradigm

### Machine learning paradigm
- [[machine learning paradigm]]



- Hello world example of neural networks
	- [[neuron]]


---

- Week 2 - Introduction to computer vision

- Fashion MNIST data
	- 70k images
	- 10 categories
	- 28x28 images
	- Can train a neural net
- Fashion MNIST is available via API of tensorflow

- Example: neural net for the task
	- NN structure 
		- `Flatten(28 x 28)`: Specifying that 28 x 28 is the shape that we should expect the data to be in. 
			- What if we don't specify?
		- `Dense(128)`: 
			- Variables of our equations. 
		- `Dense(10)`
			- Because we have a total of 10 results. 
	- Activation:
		- ReLU:
			- `max(0,x)`, which throw out negative values.
			- The propose is to introduce nonlinearity into the neural network.
			- Without nonlinearity, the NN would be limited to learning only linaer relationships between input and output.
		- Softmax:
			- The purpose is to convert the output of the neural network into a probability distribution over the output lasses. 
			- The softmax function takes as input a vector of values and outputs a vector of probabilities that sum to 1. 
```python
# Build the classification model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
```

### Normalizing the input data
- Neural networks work better with normalized data
	- So we can divide our 255 light level image by 255. Then the value becomes 0~1. Apply the same changes to training images and testing images. 

## Various kinds of outputs from `model.predict()`
- Models that has different architectures and trained for different tasks, would provide a output format that is totally different. 
- 

- Example: 
	- In linear equation example:
		- Our model was: 
			- `model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])`
		- How we compile it was: 
			- `model.compile(optimizer='sgd', loss='mean_squared_error')`
		- Our output was `19`, from `model.predict([10.0])`
	
	- In CNN classification example:
		- Our model was:
			- `model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
	
	                                    tf.keras.layers.Dense(512, activation=tf.nn.relu), # Try experimenting with this layer
	
	                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])`
		- How we compile was:
			- `model.compile(optimizer = 'adam',
	
	              loss = 'sparse_categorical_crossentropy')`
		- The output was: 
			- `[3.3436834e-05 2.6879512e-08 1.4827269e-08 1.4323167e-08 9.4394306e-07 3.1635034e-01 7.9501278e-06 6.7488924e-02 1.9092756e-06 6.1611646e-01]`

- Changing hyperparameter
	- If we increase neurons for our hidden layer
		- 1. Training takes longer, but it is more accurate
			- Adding more neurons we have to do more calculations, slowing down the process, but in this case they have a good impact -- we do get more accurate. 
			- That doesn't mean it's always a case "more is better" - we hit the law of diminishing returns very quickly.

- Normalization of data
	- If we remove the normalization step where we scale the pixel values from the range of 0-255 to 0-1, the neural network may have difficulty in training properly.
	- This is because the weight values in the neural network are initialized randomly, and the magnitude of these weight values can be quite large. When we feed large input values into the network, the large weight values cause the output values of the neurons to become very large, and this can lead to the gradients in the backpropagation step becoming very small or even vanishing, which makes it difficult for the network to learn.

- NN Structure 
	- `Flatten()` : 
		- Reshape the input data into 1-dimensional array before passing it to the dense layer. 
		- It is required because the dense layer expects 1D array as input.
		- In a dense layer, we need to perform matrix multiplication between the input data and the layer's weights. 
			- 1. If we were to pass in a 2D array directly to the dense layer, we would need to flatten it first to convert it into a 1D array. 
				- This requires additional steps and can be computationally expensive, especially for large 2D arrays.
			- 2. Working with a 1D array can be more memory efficient, since it requires less memory compared to a 2D array with the same number of elements. 
				- This can be important in applications with limited memory resources, such as embedded systems or mobile devices.
	- `Dense()`:
		- In a dense layer, each neuron is connected to all the neurons in the previous layer, and the weights between the neurons are represented as a 2D weight matrix. 
		- Each neurons in the current layer is connected to all neurons in the previous layer. To make this connection, the input to a dense layer must be a 1D array. 
	- CNN
		- If we treat an image as 1D array, the 2D contextual meaning around each pixel is lost. To address this, CNN are commonly used for image classification tasks. 
		- Pooling layer
			- The output of the Convolutional layer is then passed through a pooling layer, which reduces the spatial dimensions of the feature maps while retaining the important information. 
		- By using Convolutional and pooling layers in a CNN, the network is able to learn features that are invariant to translation and small distortions in the input image, and can capture the important contextual information around each pixel in the image.

### Tensorboard
- Prerequsite
	- 1. Define your model architecture in TensorFlow.
	- 2. Create a TensorBoard callback that will write the logs to a directory that TensorBoard can read. 
		- eg: `tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")`
	- 3. Compile and fit the model, put the callback as a parameter of `model.fit()`.
	- 4b. On notebook, display command result with:
		- eg: `%tensorboard --logdir ./logs
	- 4b. On terminal, launch tensorboard with the following command
		- eg: `tensorboard --logdir ./logs`

- Q: 
	- How can I stop training when I reach a point I want to be. Why we have to hard-code the total number of epochs? 
- A:
	- The training loop does support callbacks. 
	- Callbacks allows at the end of each epochs, having check the metrics. If passed the metric, you can cancel the training. 

- Example callback
	- This callback function stops the training when loss < 0.4.
		- with `self.model.stop_training = True`
	- It also allows the user to specifies custom behavior when that condition is triggered.
```python
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    '''
    Halts the training after reaching 60 percent accuracy

    Args:
      epoch (integer) - index of epoch (required but unused in the function definition below)
      logs (dict) - metric results from the training epoch
    '''

    # Check accuracy
    if(logs.get('loss') < 0.4):

      # Stop if threshold is met
      print("\nLoss is lower than 0.4 so cancelling training!")
      self.model.stop_training = True

# Instantiate class
callbacks = myCallback()
```
```python
# Applies the callback function
model = tf....

model.compile(...)

model.fit(x_train, y_train, epochs = 10, callbacks = [callbacks])
```

---

- Week 3 - Enhancing vision with convolution neural networks
- CNN:
	- Instead of looking single pixel and state that sample belongs to some categories. CNN has more contextual meaning obtained from the image.
	- Filter:
		- For each pixel value, we compare  immediate neighbors.
		- Multiple each neighbor with corresponding filter value, then get the new value for the pixel. 
	- Some filters can change certain features in the image get emphasized. 
		- eg: vertical lines filter
	- Tensorflow: Conv2D
		- https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D

- Number of parameters:
	- In CNN, the parameters is on the filter. 
	- The number of parameter:
		- `num_params = (filter_height * filter_width * input_channels + bias_term) * num_filters`
			- The first three terms are intuitive. 
			- Bias term: 
				- In some cases, bias terms are added to the output of each layer to ensure that the activation function has a non-zero input when the input is zero or very small. 
				- to introduce flexibility and allow the network to model more complex functions. Without bias terms, the output of a layer would be restricted to a linear transformation of the input. However, with bias terms, the output of the layer can be shifted along the activation function, allowing the network to model more complex nonlinear relationships.

- Example:
	- Determine the parameter for this convolution layer:
		- filter dimension: 3 x 3
		- input channel / filter: 3
		- output channel / filter: 16
		- number of bias: 16 (1 bias for for one filter) 
	- Calculate parameters:
		- If: Fully connected layer, 
			- we use:  (input channels, filters, output channels) are densely connected. So each block in the filter is connected to all input channels and output channels. 
			- 3 x (3 x 3) x 16 + 16 = 448
		- If: Convolutional layer,
			- For calculate the number of parameter in a convolutional layer, we use: 
				- Each filter is applied to the input tensor, over all input channels, producing a single output channel.
```python
tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3))
```
- Example:
	- Determine the parameter for this convolution layer:
		- filter: 3 x 3
		- filter / channel number: 32
```python
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
```

- Example (from Andrew Ng):
	- The first convolutional layer
		- (h x k) sized Image, with n channels
			- Say we have 150 x 150 x 3 image.
			- $n_H^{[0]} = n_w^{[0]} = 150$
			- $n_c^{[0]} = 3$
		- Say we are using 3 x 3 filter, stride = 1, no padding
			- $f^{[1]} = 3$
			- $s^{[1]} = 1$
			- $p^{[1]} = 0$
	- The second convolutional layer
		- Say we use 10 filters / channels
			- Equation: 
				- $\frac{n + 2p - f}{s} + 1$
			- 



- Pooling:
	- It is a way of compressing an image.
	- Go over the image of four pixels at a time. 
		- then 16 pixels turns into 4 pixels. 
		- Each depiction would have its own algorithm, eg: choose the biggest value from the underlying layer. 
	- That would highlighting the feature while quartering the size of the image. 
	- Limitation: 
		- The edge of the training example could not be captured. 
	- Tensorflow: MaxPool2D
		- https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D

- Example: CNN
	- The last three lines are the same. `Flatten()`, `Dense()`
	- Added parts:
		- 1. The first convolution: 
			- `64` filters for us. Filters are `3x3`. Their activations is `relu`, which means negative values will be thrown away. 
			- 64 aren't random. They start with a set of good filters
		- 2. Pooling layer:
			- It is "max pooling", because we want "for each 2x2 pixel, the biggest one will survive as shown earlier." 
		- From 1 and 2, the training data has been quartered and quartered again. 
			- The goal is to filter it to the features that determine the output.
```python
# Define the model
model = tf.keras.models.Sequential([
                                                         
  # Add convolutions and max pooling
  tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Add the same layers as before
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

```

- Say item 3,4,7 are having the same label.
	- And by trial and error (by our eyes), we think convolution number 4 (which filter vertical edge) could identify trousers. 

- `model.summary`
	- this method provides a summary of TensorFlow model's architecture. 
	- Number of trainable and non-trainable parameters in each layer, and the total number of parameters in the model.
	- It is useful for debugging and optimizing the model.
```
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 26, 26, 32)        320       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 13, 13, 32)       0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 11, 11, 32)        9248      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 5, 5, 32)         0         
 2D)                                                             
                                                                 
 flatten_1 (Flatten)         (None, 800)               0         
                                                                 
 dense_2 (Dense)             (None, 128)               102528    
                                                                 
 dense_3 (Dense)             (None, 10)                1290      
                                                                 
=================================================================
Total params: 113,386
Trainable params: 113,386
Non-trainable params: 0
_________________________________________________________________

```


---

- Week 4 - Using real-world images

### Section: Understanding ImageDataGenerator

- ImageDataGenerator
	- Function:
		- Automatically labeling the image based on the directory names.
			- Simplifies loading, preprocessing and augmenting image data for use in deep learning models.
		- Generate batches of image for efficient training.
	- How to use it:
		- Step 1: import
			- ` from tensorflow.Karas.preprocessing.image import ImageDataGenerator`
		- Step 2: Initiate a generator
		- Step 3: Specifies the parameter
			- Normalization
			- Rotation, Vertical and horizontal shifting, Shear, zoom transformation:, horizontal flip
				- Generating new training examples, to increase the robustness of the model
			- Fill missing pixels
		- Step 4: "Flow" training images in batches
			- Flow: 
				- refers to the concept of generating data on-the-fly, or in real-time, as it is needed.
				- When training deep learning model on large datasets, it is often not practical to load all the data into memory at once.  
				- Batch processing:
					- The data is loaded in smaller batches, these batches are fed into the model one at a time during training. 
			- `datagen.flow_from_directory`
				- The images are resized, batched
				- `class_node = 'categorical'`
					- While we also specify it is a multi-class classification task with mutually exclusive classes in our definition of the final layer of the neural network, it is also necessary to specify it when producing training data.
					- It is because it affect our labels.
						- When `class_node` is set to `'categorical'`, the labels are expected to be in the form of one-hot encoded vectors.

- Setting up `class_mode='categorical'` is important
	- Location: 
		- Neural network:
			- Setting it up, enables that the neural network is able to handle multi-class classification problems with mutually exclusive classes.
			- Once it is set, the neural network is trained using the categorical cross-entropy loss function, which is commonly used for multi-class classification problems.
			- The output of the final layer of the neural network is a vector of probabilities, where each element of the vector corresponds to a possible class label. 
		- Loss function:
			- It is usually `categorical_crossentropy` in tensorflow. 
			- This loss function compares the true one-hot encoded labels to the predicted probabilities output by the model for each class, and penalizes the model when the predicted probabilities are far from the true labels.


- How should we use the `ImageGenerator`
	- Point the generator at the correct directory
	- How to specify parameters, such as batch size and class node. 

```python
from tensorflow.keras.preprocessing.image
import ImageDataGenerator

# All images will be rescaled by 1./255
datagen = ImageDataGenerator(
    rescale=1./255,  # normalize pixel values to [0,1]
    rotation_range=20,  # randomly rotate images by up to 20 degrees
    width_shift_range=0.1,  # randomly shift images horizontally by up to 10%
    height_shift_range=0.1,  # randomly shift images vertically by up to 10%
    shear_range=0.2,  # randomly apply shearing transformations
    zoom_range=0.2,  # randomly zoom in on images
    horizontal_flip=True,  # randomly flip images horizontally
    fill_mode='nearest'  # fill in missing pixels with the nearest value
)

# Flow training images in batches of 128 using train_datagen generator
train_generator = datagen.flow_from_directory(
    'path/to/train/directory',  # directory containing training images
    target_size=(224, 224),  # resize images to 224x224
    batch_size=32,  # generate batches of 32 images
    class_mode='categorical'  # classify images into multiple classes
)
```

- Figure:
![[Pasted image 20230404143134.png]]


---

### Section: Defining a ConvNet to use complex images



- Example: 
	- 3 stacks of `"Conv2D + MaxPooling"` at the top, this reflects the complexity and size of the image. 
		- Determine the number of stacks of it, has no fixed rule of thumb.
		- More stacks increase the model's capacity to learn complex representations, but at the cost of increased computational resources and potential overfitting
		- As a starting point, you can use a smaller number of stacks and gradually increase them while monitoring the performance on a validation set.
		- can also try to use pre-trained models on similar tasks or datasets as a reference to see how many stacks they have used.
	- 512 dense neuron following 1 dense neuron in this model
		- 512: 
			- This number should be close to how many labels we have in our training examples. 
			- Using too few neurons may result in underfitting
			- Using too many neurons may result in overfitting
				- It is kind of memorizing the training data rather than generalizing new data, result in poor performance on the validation and test sets. 
				- In terms of combinatorics, having an oversized dense layer with 512 neurons for a problem with only 20 labels means that the model has a much larger search space to explore during training, which can make the learning more difficult and time-consuming. 
```python
model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 300x300 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

### Section: Training the ConvNet

- Compile
	- `RMSprop`:
		- adjusting the learning rate of the model
```python
from tensorflow.keras.optimizers import RMSprop

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(learning_rate=0.001),
              metrics=['accuracy'])
```
- Fit:
	- `model.fit()` looks different because we are using generator, not dataset. 
	- in this, we create `train_generator` and `validation_generator` for preparing the data.
	 - `verbose = 2`, hiding some animation in the epoch progress.  
```python
history = model.fit(
      train_generator,
      steps_per_epoch=8,  
      epochs=15,
      validation_data = validation_generator,
      validation_steps = 8,
      verbose=1)
```

- Predict
	- The line related to `google.colab.files` are related to Colab. It give me a button that you can press to pick one or more images to upload. 
		- The outcome of `for fn in uploaded.keys()` is a list of images. 
	- To predict, `classes = model.predict(images, batch_size=10)`
		- Because it is binary prediction, >0.5 = True, <0.5 = False. 

```python
import numpy as np
from google.colab import files
from tensorflow.keras.utils import load_img, img_to_array

uploaded = files.upload()

for fn in uploaded.keys():
 
  # predicting images
  path = '/content/' + fn
  img = load_img(path, target_size=(300, 300))
  x = img_to_array(img)
  x /= 255
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
    
  if classes[0]>0.5:
    print(fn + " is a human")
  else:
    print(fn + " is a horse")
```


- Q:
	- In gradient descent, how to ensure ML would not pause in a locally minimum value?
- A:
	- 1. random initialization
	- 2. adaptive learning rate
	- 3. momentum
	- 4. Batch normalization
	- 5. Stochastic gradient descent

---

### Section: Adding automatic validation to test accuracy

- 