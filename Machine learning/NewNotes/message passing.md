---
category: []
alias: []
tags :[]
---

- 26-10-2022 19:35: created

- What is message passing? ^c8a86a
	- It is the foundational mechanism that enable neural network to perform predictions, with a graph data that contains partially labeled and partially unlabeled data.
	- Message passing algorithms are distributed algorithms that operate on graphs, where each node uses only information present locally at the node and incident edges, and send information only to its neighboring nodes. 
	- This is not a machine-learning-specific algorithm. Such computation can be performed by human.
	- Assumption:
		- There is [[homophily]] in the network, which means that is a tendency of individuals to associate and bond with similar others. 
	- Intuition
		- 1. It is propagating node features by exchanging information between adjacent nodes. Given a network with labels on some nodes, how do we assign labels to all other labels to all other nodes?
			- eg: some nodes and fraudsters and some are trusted, in a social network. How do you find other good or bad guys. 
		- 2. Correlations (dependencies) exist in networks. In other words, similar nodes are connected. 
			- eg: homophily (similar individual characteristics leads to social connections) 
			- eg: influence social connections leads to similar individual characteristics) 
		- 3. Collective classification
			- Assigning labels to all nodes in a network together.
	- Examples:
		- Approximate inference algorithms on probabilistic graphic model.
		- The value iteration algorithm for Markov decision process.
- Formulation: (R1)
	- Message: $m_u^{(l0)}=MSG^{(l)}(h_u^{(l-1)})$. $MSG(.)$ converts the prior layer message such that the message is capable of multi-set classification. (eg: $m_u^{(l)})=W^{(l)}h_u^{(l-1)}$.

- Applications:
	- Document classification
	- Part-of-speech tagging
	- Link prediction
	- Optical character recognition
	- Image/3D data segmentation
	- Entity resolution in sensor networks
	- Spam and fraud detection

- 3 approaches of [[semi-supervised]] binary node classification
	- Relational classification
	- Iterative classification
	- Correct and smooth

![[Pasted image 20220916031427.png]]
- Fig: first iteration of relational classification that update the label for node 3, by referring to its neighbor's label.
$$P(Y_v=c)={1 \over { \sum_{(u,v) \in E} A_{v,u}}} \sum_{(v,u) \in E} A_{v,u}P(Y_u=c) $$

- Classifiers: (R1)
	- Base classifier: $\phi_1(f_v)$
	- Relational classifier: $\phi_2(f_v,z_v)$

---
## Reference

1. [[(Course) CS224W - Machine learning with graphs (stanford)]]  (Lecture 5.1)