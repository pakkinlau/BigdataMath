---
category: []
alias: [GCN]
tags: []
---

- 26-10-2022 15:35: created

- Subset: 
	- [[Relational Graph Convolutional Networks]]

- What is GCN?
	- A Graph Convolutional Network, or GCN, is an approach for semi-supervised learning on graph-structured data. It is based on an efficient variant of convolutional neural networks which operate directly on graphs. (R1)
	- The layers of a GCN are a generalization of [[convolutional]] layers in a [[Convolutional|CNN]] where the data can have a dynamic number of neighbors instead of being fixed on a grid like the pixels of an image. 
	- GCN is a graph neural network that are premutation [[Invariant, shift-invariant, time-invariant|invariant]] / equivalent by passing and aggregating information from neighbors.
	- It is proposed by Kipf and Welling in 2016 (R1), which was proposed to perform semi-supervised node classification.
- Mechanisms:
	- 1.  [[Message passing]]: ![[message passing#^c8a86a]]
	- 2. [[Neighborhood aggregation]]: 

- Structure:
	- [[Graph]]
	- Recall: ANN -- $x^{(l+1)}=\sigma(W_lx^{(l)}+b^l)$

- Update function of GNN for a single layer:
	- $0^{\text{th}}$ layer:
		- Embedding of node $v$ is its input feature, $x_v$.
		- $h_v^0=x_v$.
	- $k^{\text{th}}$ layer: 
		- embedding gets information from nodes that are $k$ hops away.
	- $1^{\text{st}}$ layer: 
		- [[Neighborhood aggregation]] and [[message passing]] in graph convolution networks is permutation equivariant. (R3)
		- $h_v^{1} = \sigma(W_0\sum_{u \in N(v)}{h_u^{(0)} \over |N(v)|} + B_0h_v^{(0)})$
			- $h_v^l \in R^{N \times D}$ is the hidden [[representation]] of node $v$ in the $l^{\text{th}}$ layer.
			- $\sigma$ is any activation function.
			- which $W_k$ and $B_k$ are trainable weight matrices.
			- which $|N(v)|$: Total number of of previous layer, neighborhood node.  $B$ is the neuron weightings.
			- Remember $h_v^0=x_v$ in $0^{th}$ layer.
			- The first part of the summation is [[Neighborhood aggregation]] like[[Page rank algorithm|pagerank]]; the second part is aggregating the message from itself (self-edge).
			- $\sigma$ is any kind of [[activation]], and run [[Stochastic gradient descent|SGD]] to train the weight parameters. 
	- ${l+1}^{\text{th}}$ layer: $h_v^{(l+1)}=\sigma(W_l\sum_{u \in N(v)}{h_u^{(l)} \over |N(v)|} + B_lh_v^{(l)})$
	- Final node embedding:
		- $z_v = h_v^{(K)}$
		- What's "final" meant?
- Training: (R3)
	- Unsupervised learning: 
		- $L = \sum_{z_u,z_v}CE(y_{u,v},DEC(z_u,z_v))$, where $y_{u,v}=1$ when $u$ and $v$ are similar.
	- Supervised learning: 
		- $L= \sum_{v \in V}y_vlog(\sigma(z_v^T \theta))+(1-y_v)log(1-\sigma(z_v^T\theta))$, where $y_v$ is node class label
- Inductive capability
	- Aggregation parameters $B_k$ and Updating parameter $W_k$ are shared between compute trees. So that the trained algorithm are capable of reason/predict unseen graph/node/link. 
- Attention mechanism

- a single layer of GCN
	- Network neighborhood defines a computation graph for that neuron.
	- Idea:
		- Compress a set of vectors into a single vector
	- 2 steps: 
		- [[Message computation]]: 

		- Message Aggregation:
			- Each node will aggregate the message from node's neighbors.
			- $h_v^{(l)}=AGG^{(l)}(\{m_u^{(l)}, u \in N(v) \})$
			- AGG() could be mean(), max() or avg().


![[Pasted image 20221102034122.png]]
- Fig: (R3) The same aggregation parameters are shared for all nodes 

![[Pasted image 20221102031317.png]]
- Fig: computation graph for a single neuron that work on a node. (R3)

- What is the [[objective|objective function]] of GCN??
	- 

- Steps of implementing GCN to a node: (R2)
	- 1. Collect the node representations/embeddings of all the connected neighbors. 
	- 2. Aggregate those vectors in some ways, eg: average function
	- 3. Pass to NN (that means weight matrix, and activation function). And that's only one weight matrix share across all of the nodes. For a single layer, there is one weight matrix. 

![[Pasted image 20221026160943.png]]

- Dataset used in R1
![[Pasted image 20221102022131.png]]
- Fig: R1

- Classification accuracy
![[Pasted image 20221102022117.png]]
- Fig: R1

- Propagation models (R1)
![[Pasted image 20221102022040.png]]
- Fig: R1

- Limitations: (R1)
	- Memory requirement
		- It grows linearly in the size of the dataset. Mini-batch [[Stochastic gradient descent|SGD]] can alleviate this issue.
	- Directed edges and edge features
		- GCN in R1 does not naturally support edge features and is limited to undirected graphs. RGCN should be able to handle both directed edges and edge features.

---
## Reference

1. Kipf et al. Semi-supervised classification with Graph Convolutional Network: https://paperswithcode.com/method/gcn#:~:text=A%20Graph%20Convolutional%20Network%2C%20or,which%20operate%20directly%20on%20graphs & https://arxiv.org/pdf/1609.02907v4.pdf
2.  AIOverloads Youtube video: https://www.youtube.com/watch?v=wJQQFUcHO5U
3. [[(Course) CS224W - Machine learning with graphs (stanford)]]