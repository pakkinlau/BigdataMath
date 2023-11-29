

# Week 1 Introduction to deep learning

## Intuition of a neural network 
- 1. Structure of neural network = inputs $x$ --links to--> a set of neurons --links to-- > Output $y$
	- where neurons could be either linear or non-linear functions
	- Neural networks take in data, generates either transformed data or predictions
- 2. A larger neural network is 
	- formed by taking many of the single neurons
	- stacking them together. 
- 3. Hidden units
	- Each of them takes its input of all four input [[feature]]. 
	- Rather than claiming there is a hidden feature that is partially varies by $x_1$ and $x_2$, we tell the algorithm "you decide whatever you want this known to be". And that hidden unit will give you all four features to complete whatever you want. 
- 4. [[Perception]]
Copied to:
[[neural network]]
[[hidden unit]]


- Example of using neural network:
	- Input: 
		- Size 
		- number of bedroom
		- zip code
	- Hidden layer:
		- Family size
		- Walkability
		- School quality
	- Output:
		- Price of the house 


## Supervised Learning with Neural Networks

- Different types of NN
	- [[Recurrent|RNN]]
	- [[Convolutional|CNN]]

- Different types of data
	- Structured data
	- Unstructured
		- Audio
		- Image
		- Text

- Figure: examples of supervised learning applications
![[Pasted image 20230420145659.png|400]]

## Why is deep learning taking off?

- Figure: 
	- How performance increases as we get more data
![[Pasted image 20230420150051.png|400]]

- Should copy to:
	- [[machine learning]]


- Red line:
	- Traditional models:
		- SVM, 
		- logistic regression
		- Performance plateaus when having certain amount of data
	- Small NN
	- Medium NN
	- Large NN

- To have good NN:
	- 1. Large NN, hidden units
	- 2. Scale of the (labeled) data

- In small data regime, the ordering the algorithm is not very well defined. 

- Scale drives
	- Data
	- Computations
		- It turns out training your network is intuitive
		- Change your details of your NN and having a deployment cycle of idewa-code-experiment, in 10 minutes. 
	- Algorithms 
		- ReLU (Rectified linear unit (Gradient is less likely to gradually shrink to zero)
		- Sigmoid (learning becomes very slow)

## About this course

- Basics for NN programming
- One hidden layer neural network
- Deep neural network



# Week 2 Neural networks basics


# Logistic regression


## Binary classification

- How to use $m$ training examples?
	- Method 1: for-loop. But you actually want to process your entire training set without an explicit for loop. 
- When organizing the computation
	- Forward propagation step
	- Backward propagation step

---

### Notation will be used throughout the course
- Training examples:
	- $\{(x^{(1)}, y^{(1)}) , (x^{(2)}, y^{(2)}), \dots, (x^{(m)}, y^{(m)}) \}$
	- $(x,y)$, where $x \in \mathbb{R}^{n_x}$, $y \in \{ 0,1\}$
	-  To differentiate two sets of numbers, we write $m_{train}$, $m_{test}$
- Outputs of training set inputs:
	- $(x,y)$, where $x \in \mathbb{R}^{n_x}$, $y \in \{ 0,1\}$
	- $X = \begin{bmatrix} \vdots & \vdots & \dots & \vdots \\  x^{(1)} & x^{(2)} & \dots & x^{(m)} \\  \vdots & \vdots & \dots & \vdots \end{bmatrix}_{n \times m}$, 
		-where the number of training examples is $m_x$.
		- where the number of features is $n_x$.
		-  where $X \in R^{n \times m}$.
- Output labels $Y$:
	- $(x,y)$, where $x \in \mathbb{R}^{n_x}$, $y \in \{ 0,1\}$
	- $Y = [y^{(1)} , y^{(2)}, \dots, y^{(m)}]$
		- where $Y \in R^{1 \times m}$


- Q: Why we put each training example in each column?
- A: It is called "column-wise" or "column-major" convention. The advantages are as follow - 
	- 1. mathematical consistency:
		- It is consistent with the standard mathematical notation, where each vectors are represented as columns.
		- In linear algebra, a vector is often represented as a column matrix, with its elements stacked vertically.
	- 2. matrix operation
		- Dot products are more effective.
	- 3. Data organization
	- 4. Consistency with other conventions





## Logistic regression

- Figure: sigmoid function
![[Pasted image 20230420213030.png|400]]
- Figure: illustrating the working mechanism of sigmoid function within one neuron
![[Pasted image 20230420213408.png|400]]

- Problem specification
	- Given $x$, want $\hat y = P(y=1|x)$
	- $x \in R^{(n_x)}$
	- Parameters:
		- vector of weights $w \in \mathbb{R}^{n_x}$ 
		- vector of input features $c$,
		- bias terms $b \in \mathbb{R}$
- How logistic regression play its role here?
	- prediction $\hat y$ made by a model using "logistic regression" algorithm
	- $\sigma(\cdot)$ 
		- represents the sigmoid function $\sigma(z) = \frac{1}{1+e^{-x}}$
		- It is a common choice in logistic regression

- Output:
	- $\hat y = w^Tc + b$ 
		- Linear regression 
		- This is not a good algorithm for binary classification because you want the output to be either 0 or 1. 
		- So we add sigmoid $\sigma$
	- $\hat y = \sigma(w^Tc + b)$

- Alternatives
	- Polynomial regression

Q: Why choose linear regression over polynomial regression?
	1. Simplicity:
		1. Less complex and less computational expensive
	2. Gradient-based optimization
		- Gradient descent algorithm relies on the availability of the gradients (derivatives) to update the weights of the neural network during training. 
		- Linear regression has a constant gradient, which makes it computationally efficient to calculate and update the weights using gradient-based optimization. 
	3. Representation power
		- It still represent a wide range of functions, including many complex relationships between inputs and outputs. 
		-  A neural network with just linear activation functions can approximate any continuous function to arbitrary precision, given enough neurons and layers.
	4. Avoid overfitting
		- It might fit the data too closely and fail to generalize well to unseen data.
		- Linear regression being simpler and less prone to overfitting, which makes it more robust and generalize.
	5. Interpretability
		- Interpretable coefficients that can be easily interpretable coefficients that can be easily understood in terms of the contribution of each input features to the output.

Q: Demonstrate how a neural network composed of layers of linear regression represents any complex relationships?
```python
# Generate synthetic data
X = np.linspace(-2, 2, 100)  # Input data
y = np.exp(X)  # Ground truth outputs

# Create the neural network
model = Sequential()
model.add(Dense(units=10, activation='relu', input_dim=1))  # Input layer with ReLU activation
model.add(Dense(units=5, activation='relu'))  # Hidden layer with ReLU activation
model.add(Dense(units=1, activation='linear'))  # Output layer with linear activation

#....
#....
```
![[Pasted image 20230421190042.png|300]]
![[Pasted image 20230421190052.png|300]]








---


- [[activation]]
	- types
		- Rectified Linear Unit (ReLU)
		- Hyperbolic tangent ($tanh$)
		- Softmax
		- Sigmoid


	- Considerations when choosing an activation function: 
		- 1. Probability interpretability and explainability:
			- "Probability interpretability and explainability" means the natural interpretation of probabilities
			- sigmoid or tanh, may provide more interpretable outputs as they can be interpreted as probabilities or scaled probabilities.
		- 2. Decision threshold: 
			- It allows for the use of a decision threshold, commonly set at 0.5, to make binary decisions. 
		- 3. Gradient properties:
			- When it has a smooth and differentiable nature, which is beneficial for gradient-based optimization algorithms used during model training
		- 4. Computational efficiency:
			- eg: ReLU and its variance, such as Leaky ReLU, are computationally efficient as they involve simple element-wise operations.
			- Sigmoid:
				- The exponential operation requires more computational resources and can be slow, especially when dealing with large datasets or deep neural networks.
			- tanh:
				- also involves exponential calculations similar to the sigmoid function, and thus can be computationally expensive.
			- ReLU / leaky LeLU:
				- It defined as f(x) = max(0, x), and f(x) = max(αx, x) for leaky ReLU, where $\alpha$ is a small positive constant, is computationally efficient as it involves simple element-wise operations. It does not require any exponential or logarithmic calculations, making it faster compared to sigmoid and tanh. 
				- properties and its advantages:
					- 1. Its linear in positive domain:
					- 2. It allow ReLU to accept large positive integer values, thus it can capture and represent large positive values, which means it can capture and represent large positive values, which can be beneficial in scenarios where the input data or learned features have large variations or dynamic ranges. 
					- Q: demonstrate how layers of ReLU neurons would be beneficial to learn features with large variations
						- 1. non-linearity
							- learn non-linear relationships between input features?
						- 2. sparse activation
							- they are mostly inactive, or outputting zeros for negative inputs. 
							- this sparsity allow the neural network to focus its computation on relevant features, leading to efficient feature selection.
						- 3. depth for feature hierarchy
							- Neural network with multiple layers of ReLU can learn complex feature hierarchies, allowing the network to learn increasingly abstract and high-level feature with each subsequent layer.
						- 4. gradient propagation
						- 5. computational efficiency
			- Parametric ReLU
				- f(x) = max(αx, x), which $\alpha$ is a learnable.
				- Less computational efficient, as it involves an additional learnable parameter that needs to be updated during training. 
		- 5. Non-linearity
			- It allow the model to learn complex non-linear relationships between input features and output predictions. 
			- The non-linearity of an activation function can affect the model's capacity to learn and represent complex patterns in the data.
			- Tasks that requires non-linearity:
				- 1. Image and speech recognition:
					- Synthesis and pattern recognition involves complex patterns that cannot be effectively captured by linear models. 
					- Why?
						- ![[Pasted image 20230420223156.png|300]]
						- ![[Pasted image 20230420223211.png|300]]
				- 2. Natural language processing
				- 3. Recommender systems
		- 6. Range of output values
			- It can impact the dynamics of the neural network during training. 
			- However, Activation functions with a larger output range can lead to larger gradients and potentially faster convergence during training.
			- On the other hand, activation functions with a limited output range may help to mitigate gradient-related issues, but may also result in slower convergence.
			- Examples:
				- N-ary classification:
					- If the output can be directed interprets the label numerical value, that's compatible for N-ary classification problem.
				- Regression:
					- It is important for output values of the regression to be compatible with the target output values of the problem.
					- Say a regression problem where the target is within the range of $[0,1]$, the activation function produces value outside of the range, the predicted values may not align with the target output value.
				- Generative models
				- Anomaly detection
			- While we can still scale or shift any output range from any activation function, there are problems when we fix the problem with that:
				- 1.Numerical stability
					-  If the activation function produces very large or very small output values, it can result in numerical instability during computations, such as exponential overflow or vanishing gradients. Which leads to difficulties in training.
				- 2. Interpretability
					-  In some cases, the output values of the activation function may have a direct interpretation, such as probabilities in N-class classification problems. 
				- 3. Model behavior
					- Scaling or shifting an activation can change behavior of an activation function.
					- eg: saturation region, where the gradient is very small, and linearity region of the function, where the gradient are constant.
				- 4. Training dynamics
					- "Scaling or shifting an activation" might result in biased gradients during backpropagation, leading to slow convergence or getting stuck in local optima. 
		- 7. Robustness (???)
			- 1. Insensitivity to Small Inputs
				- Some activation functions may be more robust to input variations, such as variations in the scale or distribution of input features.
					- eg: For example, ReLU and its variants are less sensitive to input variations, while sigmoid or tanh, which can be prone to saturation or vanishing gradient issues.
			- 2. Handling outliers
				- Able to handle outliners without producing extreme output values. 
				- ReLU are more robust in this area, with are less affected by outliners. sigmoid and tanh are more prone to produce large output values for extreme data points. 
			- 3. Resilience to noisy data
				- It should be able to handle noisy or imperfect data without producing unrealistic outputs. Noisy refers to uncertain, random variations that can affect the input values fed into the activation function.
				- Activation that are less sensitive to noisy data, such as ReLU, can suppress small fluctuations in input values, thus more robust in handling noisy data. 
			- 4. Stability during Training
				- Avoid vanishing gradient or exploding gradient, which can negatively impact model convergen
		- 8. Compatibility with network architecture
			- CNNs and RNNs might require specific activation functions, that are tailored to their respective architecture. 
			- CNN:
				- Used for image recognition problem, which involves convolutional layer and then a pooling layer. 
				- Activation: 
					- ReLU - introduce non-linearity while avoiding the vanishing gradient problem.
			- RNN:
				- Used for sequential data processing tasks.
				- It have recurrent connection that allow them to maintain a memory of past inputs., making them suitable for sequential data. 
				- LSTM is a type of RNN that uses a more complex gating mechanism and requires specific activation functions to regulate the flow of information through the memory cells. 
				- Activation:
					- Tanh - squashing input values between -1 and 1, which can help mitigating the vanishing gradient problems in RNNs. 
			- Variational Autoencoders (VAEs)
				- The encoder maps input data to a latent space, and the decoder maps samples from the latent space back to the data space. 
				- eg: the input might use sigmoid function and the output might use tanh to produce values in the range of -1 and 1 for image generation.
			- Gated Recurrent Units (GRUs):
				- Similar to LSTM but different gating mechanism.
				- Activation:
					- sigmoid and tanh - control the flow of information through the hidden states and update gate. 
			- N-class classification:
				- direct interpretation of the prediction are desired

- For every neurons, the curved or bent lines are called activation functions.

- Python command:
	 - `x.shape`

- Should be copied to: 
[[classification]]

## Logistic Regression Cost Function
- $y^{(i)} = \sigma(w^Tx + b)$, where $\sigma(z^{(i)}) = \frac{1}{1+e^{-z^{(i)}}}$
- Given training examples $\{(x^{(1)}, y^{(1)}), \dots, (x^{(m)}, y^{(m)})\}$, we want $\hat y ^{(i)} = y^{(i)}$
	- which superscript parenthesis $i$ refers to data. eg: $x^{(i)}, y^{(i)}, z^{(i)}$


- Loss (error) function:
	- $L(\hat y, y) = \frac{1}{2}(\hat y - y)^2$
		- Squared error loss function is commonly used in linear regression but also in logistic regression.
		- It measures discrepancy between the predicted value and true label.
		- Issue:
			- Sensitive to outliners
			- Does not fully capture the probabilistic nature of logistic regression, as it penalizes deviations from the true labels symmetrically, regardless of whether the predicted probability is above or below the true label.
		- Square function seems reasonable, except it makes gradient descent not working well. 
	- Binary cross-entropy loss
		- $L(\hat y, y) = -[y log\hat y + (1-y)log(1 - \hat y)]$, where there are two cases $y$ could be either 0 or 1. 
			- Two cases
				- If $y = 1$, $L(\hat y) = -log\hat y$
				- If $y = 0$, $L(\hat y) = -log(1 - \hat y)$
			- Logarithm
				- $log(1) = 0$
				- How $log(x)$ behaves when approaching $1$ and $0$
					- as $\hat y$ approaches 1 in the case of $y = 1$, or $\hat y$ approaches 0 in the case of $y =0$, Loss value approaches 0.
				- Numerical stability
					- Taking the logarithm helps in numerical stability and simplifies the optimization process, as it converts the product of probabilities into a sum of log-probabilities in the log-likelihood function.
					- 

	- Discussion
		- Why this loss function make sense?
		- When using squared error, you want the squared error to be as small as possible. 
		- When using this loss function, we will also want this to be as small as possible. 

- [[Maximum likelihood estimation (MLE)]]


- Convex optimization 


## Gradient descent
- Cost function for gradient descent
	- The average discrepancy between the prediction and the actual label across all samples 
	- $J(w,b) = \frac{1}{m} \sum_{i=1}^m L(\hat y^{(i)}, y^{(i)})$
	- $\underset{w,b}{min}\ J(w,b) = \frac{1}{m} \sum_{i=1}^m \underset{\hat y^i}{argmin}\ L(\hat y^{(i)}, y^{(i)})$
	- $\underset{w,b}{min}\ J(w,b) = \frac{1}{m} \sum_{i=1}^m \underset{\hat \theta_1^{MLE},\hat \theta_2^{MLE},\hat \theta_3^{MLE}}{argmin}\ L(\hat y^{(i)}, y^{(i)}\ |\  \hat \theta_1^{MLE},\hat \theta_2^{MLE},\hat \theta_3^{MLE})$
		- Our model was $\hat y = f(\theta_1, \theta_2, \dots, \theta_n | x_1, x_2, \dots, x_n) = \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \epsilon$, where $\theta_k$ are linear hypothesis parameters. 
		- $\hat \theta_1^{MLE},\hat \theta_2^{MLE},\hat \theta_3^{MLE} = \underset{\theta_1,\theta_2,\theta_3}{argmax} \ L(\theta_1,\theta_2,\theta_3)$ 
		- $\theta$ are generalized parameters of model, instead of $w$ and $b$.
- Gradient descent algorithm: 
	- Repeat: 
		- $w = w - \alpha \frac{dJ(w)}{dw}$
		- $b= b - \alpha \frac{dJ(w)}{db}$
	- For this algorithm, the derivatives can be obtained easily if those variables are at most distant from 1 neuron.
- 


- Q: 
	- In gradient descent, why the learning rate for $w$ and $b$ is the same?
- A:
	- From chatGPT,, This is done for simplicity and convenience, as it reduce the number of hyperparameters that need to be tuned.
	- However, there are some cases where different learning rates are beneficial. This is known as adaptive learning rate, or per-parameter learning rate. This can help improve the convergence and performance of the optimization process by allowing for more fine-grained control. 
- Q:
	- As I know, hyperparameters are determined by the designer, and the neural network cannot automatically determine them. So how adaptive learning rate works?
- A: 
	- Adaptive learning rate methods are designed to automatically adjust the learning rate during the optimization process.


- Q:
	- gradient descent algorithm also works if we only train the neural network with 1 training example every time. we train the neural network in such way and then after separate neural network learned the feature, we combine those learning by taking average of those weighted neuron. what is the problem of that
- A:
	- 1. high variance on the learned features. 
		- the neural network may be too specialized to the one training example, leading poor generalization to unseen data.
	- 2. slow convergence:
		- it can result in noisy and unstable weight updates. 
	- 3. loss of statistical information:
		- in can result in a loss of statistical information about the data distribution. Neural networks can capture patterns and regularity in the data. Training with one example may not provide enough diversity in the data for the neural network to learn robust and generalizable features.
	- 4. Increased computational overhead
		- updating the weights for each example requires additional computations, such as computing the gradients and updating the weights, which can be ,pre computationally expensive compared to batch-based updates where multiples are processed together.
	- 5. difficulty in hyperparameter tuning:
		- Hyperparameter tuning, such as learning rate and regularization strength, can be more challenging with one-example-at-a-time training. The optimal hyperparameter values for batch-based updates may not be suitable for one-example-at-a-time training, and finding the right hyperparameter values can require additional experimentation and tuning.

- Q:
	- softplus versus ReLU, what's the difference in their performance?
- A:
	- 

---


- how neural network works?
	- part 1 - univariate linear equation as a part of a linear classifier
		- a neuron in a neural network change its own shape
		- In mathematics, 
			- $f(-x)$ is a reflection of the graph of $f(x)$ across $y$ axis. 
			- $-f(x)$ is a reflection of the graph of $f(x)$ across $x$ axis. 
			- $f(x+c)$ means shifting the graph without changing its shape.
		- the multiplier of the linear classifier inside the neuron is actually acting as a mirroring factor to the original input series.
		- if we have $a(wx + c)$ and say $c = 0$ for simplicity and $w = -1$, The linear classifier actually change the input domain of the activation function like how $f(-x)$ did.
		- similarly, the $c$ of the linear classifier acting as the variable that shift the activation function. say $w = 1$ for simplicity, and we plug in any $c$ before applying the activation $a$, actually it works exactly like $f(x + c)$. 
	- part 2 or 3 - adding up multiple linear classifiers to construct a more complex classifier
		- adding up multiple curly or linear function allows the neural network constructing a more complex decision boundary.
		- neurons in the next layer combines the output from multiple neurons of their previous layer.
		- however, if we just simply add up all linear classifiers, the product will always remain linear. 
		- So we need to apply activation function for 
		- theoretically, it could stimulate any smooth curve by adding them up. If the activation has non-linearity, which could makes the learning demand less resources.
	- part 2 or 3 - apply the result of linear classifier unit into a non-linear activation function
		- non-linearity allow the final output of the neuron becomes non-linear.

- Q:
	- there are some neurons has multiple dependent variables. Can we think of those linear classifier that has more than one $x$ is just a linear combination of univariate linear equation, and then those results pass into a sum gate? 

---
(the term for discussing these design options would be:)


### point-wise nonlinearity / elementwise nonlinearity
- This term refers to the fact that the nonlinearity is applied to each input feature individually, rather than to the sum of the inputs.

### weighted sum
- This term refers to the process of summing up the inputs before applying the activation function.
- This is because the inputs are first multiplied by their corresponding weights and then summed up before being passed through the activation function.


(related concept:)

### Skip connection


### Gating mechanism


### Residual connections

---


figure:
	two non linear function adding together to becomes a squiggle.
![[Pasted image 20230427031202.png|400]]


- figure: the ReLU activation, as a result, could light up for any kind of sequence of numerical values, by combining multiple layers of ReLU neurons. 
	- source: https://www.youtube.com/watch?v=68BZ5f7P94E
	- effective dosage problem -- a specific value is optimal
	- the following green line is combined by two ReLU function. 
		- one is a ReLU which is $max(0, wx-c)$ where $c$ is a positive number. So that ReLU keeps return zero until 
![[Pasted image 20230426234350.png|400]]

- Q:
	- why we need the whole layer of neurons applying the same type of activation function? me might mix up a half of the neurons using one type of activation function, and another half might use another type of activation function. 
- A:
	- Mixed activation functions can be done, but it is not a common practice. for several reasons:
		- 1. consistency / harder to interpret
			- easier to interpret and analyze the behavior of the layer as a whole.
		- 2. simplicity
			- different activation functions might have different mathematical properties, such as differentiability, which can affect the training dynamics and convergence of the network.
		- 3. backpropagation
			- using different activation function in the same layer could lead to inconsistencies in gradient descent, making it more challenging to optimize the network.
	- Recent trends in research:
		- "neural architecture search", "adaptive activation functions" explored the idea of using different activation functions for different neurons or even adaptively changing the activation function during training.


- Multiple inputs and outputs 
- Figure:
	- when we have more than 1 feature input, the neural network creates multiple curved or bent surfaces. And these are added together to make a crinkle surface. 
	- we add the y coordinates of 2 neuron to form a new surface. 
	- we scaled our training example from (min, max) to (0,1), so if Petal width = 0, actually it represent a smallest Petal width in the training dataset.
	- source: https://www.youtube.com/watch?v=83LYR-1IcjA
![[Pasted image 20230427192033.png|400]]
![[Pasted image 20230427192921.png|400]]


---
### Universal approximation theorem
- source: https://www.analyticsvidhya.com/blog/2021/06/beginners-guide-to-universal-approximation-theorem/
- 

---
- The following content will be learned in course 2

### AdaGrad
- If the gradient is large, the denominator would be large, reducing the overall magnitude of the update for the parameter.
- $w_{t+1} = w_t - \frac{\eta}{\sqrt{G_t + \epsilon} }\times g_t$
	- $\eta$: initial learning rate
	- $g_t$: the gradient of the parameter at time step $t$
	- $G_t$: 
		- the sum of squared gradients, up to time step
		- $G_t = \sum_{i=1}^t g_i^2$
- Q: 
	- How to determine the initial learning rate
- A:
	- 1. Rule of Thumb
	- 2. Grid search
	- 3. Learning rate schedules
	- 4. Cross validation

### RMSprop
- Uses a decaying average of squared gradients to adapt the learning rate
- $w_{t+1} = w_t - \frac{\eta}{\sqrt{E[g^2] + \epsilon} }\times g_t$
	- where $E[g^2]$ is the decaying exponential average of the squared gradients. 
	- where $g_t$ id the gradient of the parameter at time step $t$
- $E[g^2]_t =\alpha E[g^2]_{t-1} + ( 1 - \alpha)g_t^2$
	- $E(\cdot)$ is an exponentially weighted moving average of the squared gradient.
	- It defines how the EWMA of the squared gradients is updated at each time step
		- $E[g^2]_{t-1}$:
			- Estimate of the gradients up to time step $t-1$.
			- It is updated at each time step based on the current gradient value.
		- $\alpha E[g^2]_{t-1}$:
			- Applies exponential weighting to the previous EWMA of the squared gradient.
			- With $\alpha$ being the weighting factor.
		- $g_t^2$:
			- Squared gradient of the parameter at the current time step
		- $(1 - \alpha) g_t^2$:
			- 
	- $\alpha$ is the decay rate that controls the weighting of old and new gradients.

### Convexity
- Convexity is very important for gradient descent
- Function is convex if f''(x) > 0 for all $x \in I$


## Derivatives 
- Same as calculus




## Computation graph

### Computation graph
- Usage
	- Organize the computation with blue arrows, left to right computation.
	- Efficient computation of complex mathematical expression through parallelization and optimization technique 
	- Compute gradients during backpropagation
		- immediate connected node:
			- no cross reference needed. the gradient could be find on the node itself
		- far connected node:
			- by chain rule we can also find the inter-relationship between those variables. In most cases they are just multiplications.
- Nodes:
	- represents mathematical operations or functions
	- each node takes one or more inputs, perform a computation, and produces an output
	- can also represent parameters of the model, such as weights and biases in a neural network.
	- In machine learning, one step of BACKWARD propagation on a computation graph yields derivative of final output variable.
- Edges:
	- represent the flow of data between nodes
	- data is passed from the output of one node to the input of another node through edges.
	- they carry the intermediate results of computations between nodes.
- Computational flow
	- flow in the graph is the direction the edge following.
	- inputs to the graph are fed into the node sequentially as data flows through the graph, until the final output is produced at the end of the graph.
- Computation:
	- For our model $y = f(\theta_1, \theta_2, \dots, \theta_n | x_1, x_2, \dots, x_n) = \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \epsilon$, the derivative of the cost function $J$ in respect of each variable in $x_k \in X$ (where $x_1, x_2, \dots, x_n \in X$) (i.e. $\frac{dJ}{d x_k}$) is simply equal to the numerical value of the parameter $\theta_k$ itself. 
	- Terms 
		- One way of look at this problem, is to zoom in one of the node in the computational graphs, and we can see there are some common things.
		- Say $z = f(x,y)$, $f$ process $x$ and $y$ to produce $z$.
		- Local derivatives
			- They are internal to this node
			- $\frac{\partial z}{\partial x}$, $\frac{\partial z}{\partial y}$:
				- which tells us for each output of the node, how much is each output of the node, affected by each input of the node.
		- Upstream derivative
			- $\frac{\partial L}{\partial z}$, which receiving message from upstream in the graph.
		- Downstream derivative
- Forward propagation
	- Just simply apply the predefined function of each neuron (must probably regression function combined with activation function) and pass the output dataflow to the next neuron. Repeat until it gives a prediction value.


- Backward propagation
	- The goal of backpropagation is to take differentiation of $SSR$ (sum squared error) against every parameter $W_1, W_2, \dots, W_n$ and $b_1, b_2, \dots, b_n$ of the neural network. 
		- Remember, $SSR = \sum_{i=1}^n (\hat y_i - y_i)^2$
	- We can compute the downstream gradient of the node, by simply multiply the upstream gradient and local gradient
	- $\frac{\partial L}{\partial x}$ = $\frac{\partial z}{\partial x}$$\frac{\partial L}{\partial z}$
		- Notice the ordering in the multiplication is following the orientation in the computational graph. The former one is local gradient, and the latter one is upstream gradient.
	- Update of weights and biases would be written on "gradient descent". 



- How machine learning programs, such as TensorFlow actually execute forward and backward propagation? Do they need to calculate the upstream gradient, local gradient and downstream gradient every time they work with a mini-batch of training data?
- Q1:
	- Do Tensorflow need to calculate the upstream gradient, local gradient and downstream gradient on every epoch? the derivative seems stay the same during training process.
- A1:
	- It should be "Yes", we can imagine the agent is travel along a convex region to find the optima to minimize the loss. Because the region is convex, the gradient in each point should be different thus we need to calculate it again in each iteration.
	- Demonstration:
		- Say we have a layer of neural network, and the last neuron is always $J=y^−y$.
		- 1. To backpropagate the information, say we are focusing on the node of $\hat y$, which sends message to $J$. So in node 1 $\frac{\partial J }{\partial z}$ would have different values.
			- Say $\frac{\partial J }{\partial z} = 5$ in epoch 1.
		- 2. In node 2 we have $\frac{\partial J }{\partial x} = \frac{\partial J }{\partial z}\frac{\partial z}{\partial x}$
			- The numerical value of $\frac{\partial J }{\partial z}$ has changed, thus $\frac{\partial J }{\partial x}$ also would change.
- Q2: 
	- While I know the numerical value of the derivatives of loss function in respect to each variables will be different in each epoch, but the underlying formula to calculate those value remain unchanged, such as we can use chain rule to connect upstream and downstream derivatives. So my question is, would those programs similar to TensorFlow, would first determine the underlying formula, then the program could subsequently plug in numerical values into the underlying formula to determine those values. 
- A2:
	- You are correct.
	- In frameworks like TensorFlow, the underlying formulas for the derivatives are predefined and implemented as computational graph operations. 
- Q3:
	- How did TensorFlow compute gradient descent? For loop or anything?
- A3:
	- Automatic differentiation - 
		- TensorFlow uses a technique called automatic differentiation to compute gradients efficiently during optimization algorithms such as gradient descent. Automatic differentiation is a computational technique that allows for computing the derivatives of a function with respect to its input variables automatically, without explicitly computing and specifying the derivative formulas.
		- When you define a model using TensorFlow's APIs, it creates a computational graph, which is a directed acyclic graph (DAG) that represents the computation flow of the model. Each node in the graph represents a mathematical operation or transformation, and the edges represent the flow of data between operations.
	- Symbolic differentiation:
		- This is in contrast to "numerical differentiation," which involves approximating the derivatives using finite differences and can be computationally expensive. It allows for efficient computation of gradients for large computational graphs with many parameters, as it leverages the inherent structure and properties of the graph.
			- What is symbolic difference?
				- Say we have $f(x) = 3x^2 + 2x + 1$
				- Then by symbolic difference: $f'(x) = d/dx (3x^2) + d/dx (2x) + d/dx (1)$
			- What is numerical difference?
				- Same function, now we differentiate it by $f'(x) ≈ (f(x + h) - f(x - h)) / (2h)$
				- Choosing a small step size of $h$ and compute an approximate value of $x$ at some value.
		- TensorFlow uses a technique called "symbolic differentiation" to compute the gradients. Symbolic differentiation involves manipulating the mathematical expressions that represent the operations in the graph to compute the derivatives symbolically. 
	- Forward pass:
		- During the forward pass, TensorFlow computes the intermediate results of the model's operations and stores them in the graph. 
		- Automatic differentiation is implemented during forward pass.
	- Backward pass:
		- During the backward pass, TensorFlow uses the chain rule of calculus to automatically compute the gradients of the loss function with respect to the variables in the graph. These gradients are computed efficiently by traversing the graph in reverse order, starting from the output layer and propagating the gradients backwards to the input layer.

- Backpropagation with vectors 
	- Local Jacobian matrices
		- A local Jacobian matrix represents the partial derivatives of each element in the output vector with respect to each element in the input vector.
		-  It is a square matrix where the rows represent the derivatives of the output vector's elements with respect to a single input element, and the columns represent the derivatives of a single output element with respect to all the input elements. 
		- The diagonal of the local Jacobian matrix contains the partial derivatives of each output element with respect to its corresponding input element, and off-diagonal elements contain the partial derivatives of each output element with respect to the other input elements.
	- What matter most is the shape of each Jacobian matrices, in the computation process.

### Jacobian matrix 
- What is Jacobian matrix?
	- It is closely related to gradient and total derivative of a function.
		- gradient: ∇f = (∂f/∂x, ∂f/∂y)
		- total derivative = ∂F/∂x ∂F/∂y ∂F/∂z
	- A Jacobian matrix is a matrix of partial derivatives of a vector-valued function with respect to its input variables. It is a fundamental tool in multivariable calculus, optimization, and physics, among other fields.
		- J = (∂F₁/∂x ∂F₁/∂y ∂F₁/∂z) // (∂F₂/∂x ∂F₂/∂y ∂F₂/∂z)
	- Definition of Jacobian matrix:
		- $J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \dots & \frac{\partial f_1}{\partial x_n} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \dots & \frac{\partial f_2}{\partial x_n}\\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \dots & \frac{\partial f_n}{\partial x_n} \end{bmatrix}$
	- The Jacobian matrix gives us information about how small changes in the input variables affect the output variables of the function. In particular, the entries of the Jacobian matrix are the partial derivatives of the output variables with respect to the input variables, so they can be used to compute the gradient, the determinant, and other important properties of the function.
	- The rows of the Jacobian matrix:
		- It describe the derivatives of the components of the output vector with respect to a single input variable. 
	- The columns of the Jacobian matrix:
		- It describe the derivatives of a single output variable with respect to all of the input variables.
- we have $f(x) = x^2$ then $df/dx = 2x$
- we have $f(x,y) = x^2 y$, then $df/dx = 2xy$ and $df/dy = x^2$.
- Jacobian extends this step further.
	- Say we have $f(\begin{bmatrix} x \\ y \end{bmatrix}) = \begin{bmatrix} f_1(x,y) \\ f_2(x,y) \end{bmatrix}_{2 \times 1} = \begin{bmatrix} x^2y \\ sinx \end{bmatrix}$
	- Then Jacobian matrices store all of the derivatives for each function in a row, ordered by the variable order when it is defined inside the function notation.
	- So for our $\begin{bmatrix} x \\ y \end{bmatrix}) = \begin{bmatrix} f_1(x,y) \\ f_2(x,y) \end{bmatrix}_{2 \times 1}$, the Jacobian matrix would be $J_f(x,y) = \begin{bmatrix}\frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\ \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y}\end{bmatrix}_{2 \times 2}$
- Things that Jacobian does not cover:
	- Where is the highest and lowest location of the map? Plug in all local optima to test that out?
- Application
- 1. Multivariate equation
	- Say we have $f(x,y,z) = x^2y + 3z$
	- Recall the definition of Jacobian is $\begin{align*} J_{f(x_1, x_2, x_3)} &= \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \frac{\partial f}{\partial x_3} \end{bmatrix} \\ &= \begin{bmatrix} 2xy & x^2 & 3\end{bmatrix} \end{align*}$
 
 - 2. Neural network
		- Say we have a single feature data set, with a layer of 2 neurons, followed by another layer of 2 neurons.
		- Layer 1: 
			- $\begin{bmatrix} a_1(x) \\ a_2(x) \end{bmatrix} = \begin{bmatrix} w_1^{(1)}x + c_1^{(1)} \\ w_2^{(1)}x + c_2^{(1)} \end{bmatrix}$ 
			- This layer has 1 variable, and it has 2 functions in it.
			- $J^{(1)} = \begin{bmatrix} w_1^{(1)} \\ w_2^{(1)} \end{bmatrix}_{2 \times 1}$
		- Layer 2:
			- $\begin{bmatrix} b_1(a_1, a_2) \\ b_2(a_1, a_2) \end{bmatrix} = \begin{bmatrix} w_{11}^{(2)}a_1 + w_{21}^{(2)}a_2 +  c_1^{(2)} \\ w_{12}^{(2)}a_1 + w_{22}^{(2)}a_2 +  c_2^{(2)} \end{bmatrix}$
			- This layer has 2 variables, and it has 2 functions in it.
			- $J^{(2)} = \begin{bmatrix} w_{11}^{(2)} &  w_{21}^{(2)}  \\ w_{12}^{(2)} &  w_{22}^{(2)} \end{bmatrix}_{2 \times 2}$
	- If we have more layers and more neurons to get to $\hat y$. The total representation of the systems would grows dramatically.


- Q: 
	- when talking about Backpropagation with vectors , why we need to know about Local Jacobian matrices? what are they?
- A:
	- The local Jacobian matrices are used in backpropagation to compute the gradient of the loss function with respect to the input vector. This gradient is then used to update the parameters of the neural network during the optimization process. 
	- By computing the local Jacobian matrices, we can efficiently propagate the gradient from the output of the network back to the input, allowing for efficient optimization of the network's parameters.

- Figure:
	- source - https://youtu.be/dB-u77Y5a6A?t=2529
![[Pasted image 20230426040504.png|400]]

- Backpropagation with matrices (or tensors)
	- The local Jacobian matrices become interesting -- for each scalar elements of the input, how much does each scalar element of the output change. 

- Figure: 
	- The intuition of backprop with tensors
	- source: https://youtu.be/dB-u77Y5a6A?t=3018
![[Pasted image 20230426040850.png|400]]

---
(discussed when talking about gradient descent)

- Figure: the concept of gate
	- patterns in gradient flow in gradient descent, we have:
		- add gate, mul gate, copy gate and max gate
	- source: Lecture 6: Backpropagation https://www.youtube.com/watch?v=dB-u77Y5a6A
![[Pasted image 20230426035219.png|400]]

- More gates in ML:
	- Attention gate
		- commonly used in neural networks for tasks such as machine translation, image captioning, and sentiment analysis. 
		- Attention gates allow the model to selectively focus on different parts of the input data, assigning different weights or attention scores to different input elements. This allows the model to dynamically adjust its focus and selectively attend to relevant information during processing.
	- Dropout gates
		- a regularization technique commonly used in neural networks to prevent overfitting. 
		- Dropout gates randomly "drop out" or deactivate certain neurons during training, which helps to prevent the model from relying too heavily on specific neurons and encourages the model to learn more robust and generalized representations.
	- Update gates
		- In recurrent neural networks (RNNs) and related architectures, update gates are used to control the flow of information between hidden states at different time steps. 
		- For example, in the long short-term memory (LSTM) model, there are three types of gates - input gate, output gate, and forget gate - which regulate the flow of information through the memory cell.
		- Q: What is the relationship between update gate and forget gate?
	- Sampling gates 
		- Sampling gates are used in generative models such as variational autoencoders (VAEs) and generative adversarial networks (GANs). 
		- Sampling gates determine whether to sample from a learned distribution or to use a deterministic value during the generation process, allowing the model to introduce stochasticity and generate diverse outputs.
	- Forget gates
		- Forget gates are used in some variations of recurrent neural networks, such as the Gated Recurrent Unit (GRU).
		- Forget gates determine the amount of information from the previous time step that should be forgotten or retained in the current time step, allowing the model to selectively update its hidden state.
	- Routing gates
		- Routing gates are used in capsule networks, which are a type of neural network architecture proposed as an alternative to traditional convolutional neural networks (CNNs) for image recognition tasks. 
		-  Routing gates are used to dynamically route information between different capsules, allowing the model to learn more structured and hierarchical representations of images.
	- Control gates
		- incorporate external memory or attention mechanisms, such as the Neural Turing Machine (NTM) or the Transformer model.
		- Control gates allow the model to control the read and write operations to the external memory or attention mechanisms, facilitating flexible and dynamic interactions between different components of the model.
	- Threshold gates
		- Threshold gates are used in thresholded ReLU (ReLU) activation functions, which are variants of the popular ReLU activation function commonly used in deep neural networks. 
		- Threshold gates introduce a threshold parameter that determines the minimum value at which the activation function becomes active, allowing the model to control the sparsity and non-linearity of the activations.
	- Sigmoid gates 
		- commonly used in neural networks for tasks such as binary classification or as activation functions in certain types of layers, such as the sigmoid activation function.
		- Sigmoid gates introduce non-linearity and allow the model to capture complex relationships between input features.
	- Switching gates
	- Update-only gates 
	- Feedback gates
	- Residual gates


### Decision layer
- argmax for output, softmax for training
- Argmax
	- It is very easy to interpret
	- But there is no weights to train.
	- It is not differentiable as well, it means we can't argmax for backpropagation?

### softmax
- Softmax
	- $s_i = \frac{e^i}{\sum e_i}$
	- input matrix: $z = \begin{pmatrix} z_1 \\ z_2 \\ \vdots \\ z_n \end{pmatrix}$
	- output matrix: $s = \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix}$
	- Vector function
		- formally, softmax is a vector function, which takes a vector as input and produces a vector as output.
			- softmax: $\mathbb{R}^n \rightarrow \mathbb{R}^n$
	- Representing softmax function as a Jacobian matrix
		- Considering there are $n$ output $s_1, s_2, \dots, s_n$, and $n$ input, $z_1, z_2, \dots, z_n$. 
		- Recall
			- The rows of the Jacobian matrix:
				- It describe the derivatives of the components of the output vector with respect to a single input variable. 
			- The columns of the Jacobian matrix:
				- It describe the derivatives of a single output variable with respect to all of the input variables.
	- compute derivative softmax function, $J_{softmax}$
		- $J_{softmax} = \begin{pmatrix} \frac{\partial s_1}{\partial z_1} & \frac{\partial s_1}{\partial z_2} & \dots &\frac{\partial s_1}{\partial z_ｎ} \\  \frac{\partial s_2}{\partial z_1} & \frac{\partial s_2}{\partial z_2} & \dots &\frac{\partial s_2}{\partial z_ｎ} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial s_n}{\partial z_1} & \frac{\partial s_n}{\partial z_2} & \dots &\frac{\partial s_n}{\partial z_ｎ}\end{pmatrix}$
		- To find the value of each element, we do the following:
			- 1. Taking logarithmic derivative, 
				- $\frac{\partial}{\partial z_j} log(s_i) = \frac{1}{s_i}\frac{\partial s_i}{\partial z_j}$
				- $\frac{\partial s_i}{\partial z_j} = s_i  \cdot \frac{\partial}{\partial z_j} log(s_i)$
			- 2. Simplify $\frac{\partial}{\partial z_j} log(s_i)$
				- With  $s_i = \frac{e^i}{\sum e_i}$, we would have:
				- $\frac{\partial}{\partial z_j} log(s_i) = \frac{\partial z_i}{\partial z_j} - \frac{\partial}{\partial z_j} log(\sum_{i=1}^n e_{zi})$
				- The first term:
					- $\frac{\partial z_i}{\partial z_j} = \begin{cases} 1,\ if\ i=j \\ 0,\ otherwise \end{cases}$
				- The second term:
					- 
		- $J_{softmax} = \begin{pmatrix} s_1 \cdot (1 - s_1) & -s_1 \cdot s_2 & \dots  & -s_1 \cdot s_4 \\ -s_2 \cdot s_1 &s_2 \cdot (1 - s_2) & \dots & -s_2 \cdot s_4 \\ \vdots & \vdots & \ddots & \vdots \\  -s_n \cdot s_1 & -s_n \cdot s_2 & \dots & s_4 \cdot (1 - s_n)\end{pmatrix}$
- The problem is with Argmax we can't use it to optimize the weights and biases in the neural network.
### Derivative of softmax
- involving Jacobian matrix
- source: https://towardsdatascience.com/derivative-of-the-softmax-function-and-the-categorical-cross-entropy-loss-ffceefc081d1


## Logistic regression gradient descent
- what we need to implement logistic regression?
- recall:
	- 1. $y^{(i)} = \sigma(w^Tx + b)$
	- 2. 

# Week 3 Shallow neural networks

### Neural network representation

### Vectorized representation

### Activation functions 

### Derivatives of activation functions

### Backpropagation 

### Random initialzation