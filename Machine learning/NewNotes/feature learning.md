---
category: []
alias: [representation learning]
tags: []
---

- 24-10-2022 15:08: created

- Prior paradigm:
	- Using manmade features. Machine conversion is mainly for pre-processing data. 
- Current paradigm:
	- Machine conversion is the main task.

- What is representation learning?
	- In machine learning, feature learning or representation learning is a set of techniques that allows a system to automatically discover the [[representation]] needed for feature detection or [[classification]] from raw data. This replaces manual [[feature engineering]] and allows a machine to both learn the features and use them to perform a specific [[tasks|task]].
	- Feature learning is motivated by the fact that [[machine learning]] [[tasks]] such as [[classification]] often require input that is mathematically and computationally convenient to process. 
	- However, real-world data such as images, video, and sensor data has not yielded to attempts to algorithmically define specific features. An alternative is to discover such features or representations through examination, without relying on explicit algorithms.

- My writing:
	- [[machine learning]] is solving a couple of problem -- 
		- Perspective 1:  Finding a way to determine the decision boundary
		- Perspective 2: Finding a way to find a presentation that are easier to be discovered and allocate orders.

- Notation:
	- [[graph]] $G = (V,E)$ with associated binary adjacency matrix $A$. Assume the method can make use of real-valued matrix of node attributes $X \in R^{m \times |V|}$ (eg: representing text or metadata associated with nodes).
	- The goal is to use the information in $A$ and $X$ to map each node, or a subgraph, to a vector $z \in R^d$, where $d << |V|$.  ([[Compress]] involved)

- Techniques that generate features
	- [[Deep|deep neural network]]: 

- Feature learning can be either [[supervised learning|supervised]], [[Unsupervised learning|unsupervised]], or [[Self-supervised learning|self-supervised]]
	- In [[supervised learning]], 
		- [[feature]] are learned using [[label|labeled]] input [[Data]]. [[label|labeled]] data includes input-label pairs where the input is given to the [[model]] and it must produce the ground truth label as the correct answer.
		- This can be leveraged to generate feature representations with the model which result in high label prediction accuracy.
		- eg: supervised neural networks, multilayer perception, and supervised [[dictionary learning]]. [[multilayer perception]]
	- In [[Unsupervised learning]], 
		- [[feature]] are learned with unlabeled input data by analyzing the relationship between points in the dataset.
			- eg: [[dictionary learning]], [[independent component analysis]], [[Matrix factorization]], and various forms of [[clustering]], [[local linear embedding]]
	- In [[Self-supervised learning]], 
		- [[feature]] are learned using unlabeled data like [[Unsupervised learning|unsupervised]] learning, however input-label pairs are constructed from each data point, which enables learning the structure of the data through supervised methods such as [[Gradient descent]]. 
			- eg: [[Word representation|word embedding]]
			- eg: [[autoencoder]]
			- eg: The use of [[Deep]] [[neural network]] auch as [[Convolutional|CNNs]] and [[Transformer]].

---
## Reference

1. Wikipedia
2. [[(Paper) Representation learning on graphs -- Methods and applications]]