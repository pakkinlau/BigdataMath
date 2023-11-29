- 26-4-2023: created

- a very good source here as well:
	- https://www.youtube.com/watch?v=dJYGatp4SvA&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=2


- Lecture 5 of Michigan

- Neural network is somehow jointly learning both:
	- 1. feature representation
	- 2. a liner classifier on the top of that feature representation
	- in such a way to maximize the classification performance

- linear classifier
	- $f = Wx$, $x \in R^D$, $W \in R^{C \times D}$, where $C$ denotes the number of categories, $D$ denotes the number of input dimensions.
- 2 layer neural network'
	- $f_1 = W_1x$
	- $f_2 = W_2 max(0, W_1 x)$
		- which $ReLU(z) = max(0,z)$
		- if we build a neural network with no activation function, the whole structure would becomes a linear classifier.
	- $W_2 \in R^{C \times H}$, $W_1 \in R^{H \times D}$, $x \in R^D$, $H$ represents the number of neuron in the hidden layer.
- Generalized version
	- $f_n = W_n max(0, W_1 x)$
	- $W_n \in R^{C \times H_{n-1}}$
	- $W_{k-1} \in R^{H_{k-2} \times H_{k-3}}$
	- $W_1 \in R^{H_1 \times D}$
	- $x \in R^D$
- So we denote the set of input element as $X$, the set of hidden layer element as $h$, output elements as $s$.
	- All elements of $x$ affect all elements of $h$.
	- All elements of $h$ affect all elements of $s$.
- Fully-connected neural network also called "multi-layer perception"


- Q: 
	- why Fully-connected neural network has a special name called "multi-layer perception"?
- A:
	- This misnomer can be misleading. A MLP is not a perception in the traditional sense.
	- Perceptron originally referred to a type of neural network with a single layer that was introduced in the 1950s.

- linear classifier: one template per class?
	- My guess is, it means the neural network would learn some "eiganface" to classify between cars, planes, birds, deers etc.
- neural net:
	- the first layer is bank of templates;
	- the second layer recombines templates
- Q:
	- in the context of linear classifier in machine learning, what is the meaning of one template per class?
- A:
	- 
