---
category: []
alias: []
tags :[]
---

- 26-10-2022 19:38: created

- Abstract:
	- The primary challenge in this domain is finding a way to represent, or encode, graph structure that it can be easily exploited by machine learning models. 
	- Traditionally, 
		- Traditionally, machine learning approaches relied on user-defined [[heuristics]] to extract features encoding structural information about a graph (e.g., degree statistics or kernel functions).
	- Recent years, 
		- A surge in approaches that automatically learn to encode graph structure into low-dimensional embeddings, using techniques based on deep learning and nonlinear dimensionality reduction.
	- This paper provide a conceptual review of key advancements in this area of representation learning on graphs, eg [[Matrix factorization]] methods, [[Random walk]] based algorithm, and [[Graph neural networks]].

- Session 1:
	- [[Graph representation challenge]]
	- [[feature learning]], [[representation]]


- Other closely related works
	- Latent space models of social networks (33)
	- Statistical relational learning (43)
	- Manifold learning algorithms (38)
	- Geometric deep learning (7)

- Section 2:
	- [[Encoder decoder model]]
	- [[Compress]]
	- [[feature learning]]
	- Review of methods
		- Most of them are unsupervised, without knowledge of a particular downstream machine learning task.
			- [[Matrix factorization]]
			- [[Random walk]]
		- Some supervised [[feature learning]] where the model make use of [[classification]] or [[regression]] label in order to optimize the embedding.
	- [[similarity]]

- Section 4:
	- [[Knowledge graph challenge]]


![[(Paper) Hamilton, W. L., Ying, R., & Leskovec, J. (2017). Representation learning on graphs Methods and applications.pdf]]