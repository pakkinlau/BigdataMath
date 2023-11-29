---
alias: [ANN, artificial neural network, neural net]
---

- 5-10-2022: created

- Superset: [[predictor]]

- Types:
	- [[Deep]]
	- [[Recurrent]]
	- [[Convolutional]]

Intuition of a neural network 
	- 1. inputs $x$ --> [[neuron]] --> Output $y$
		- where neurons could be either linear or non-linear functions
	- 2. A larger neural network is 
		- formed by taking many of the single neurons
		- stacking them together. 

- Training of neural network
	- It can be modelled as an [[optimization]] problem:
	- $\theta^* = \arg\min_{\theta} J(\theta)$, where $J(\theta) = \frac{1}{N} \sum_{i=1}^{N} (f(x_i; \theta) - y_i)^2$
		- $J$: objective function matrix
		- $\theta$: parameter matrix of the network
		- $x_i$: certain feature of data $i$
		- $y_i$: true label of data $i$ 


- What is neural network?
	- [[neuron]]:
		- Perform computation
			- the neurons themselves are responsible for performing computations on this information.
				- the output of each neuron is computed by some non-linear function of the sum of its inputs.
		- Initial state variable
			- Each neuron receives inputs from one or more other neurons, and computes an output based on its internal state variables and the strength of those inputs. 
			- Example of initial state variable
				- neuron's activation level or output value, that are updated based on the inputs it receives from other neurons.
		- Determining the overall connections of the neural network.
			- The number and arrangement of neurons in a network can have a significant impact on its ability to learn and generalize from data.
	- Edge:
		- Connection between neurons
		- In a neural network, the parameters are typically associated with the connections between neurons, not with the neurons themselves. 
		- Each connection between neurons has an associated weight, which represents the strength of the connection between those two neurons.
	- Weights:
		- Neurons and edges typically have a weight that adjusts as learning proceeds. 
		- The weight increases or decreases the strength of the signal at a connection. 
		- Neurons may have a threshold such that a signal is sent only if the aggregate signal crosses that threshold.
	- Layer:
		- Typically, neurons are aggregated into layers. Different layers may perform different transformations on their inputs.
		- Possibly traversing the layers multiple times.

![[Pasted image 20231106155333.png]]
- One layer network
	- Consider a linear mapping, 
	- $AX = Y$
		- where it is similar to linear regression / linear algebra problems
		- $AX$ represents the set of predictions (+1 / -1)
		- $Y$ represents the actual value of the labels
	- Our goal of this problem is to find $A$
		- The simplest solution is [[Pseudo-inverse matrix|Pseudo-inverse]] of the data matrix: $A = YX^\dagger$
		- Also can be solved in various ways, such as LASSO

- Design considerations: 
	- input $x_j$ to the output $y_j$ 
	- How many layers
	- Dimension of each layer
	- How to design the output layer
	- Filly or partially connected layer
	- The mapping between layer
		- [[linearity]]




---
### Reference
- [[(Course) Nerual network and deep learning, 1 of 5 of Deep learning specialization]]