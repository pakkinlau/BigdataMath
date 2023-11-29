---
category: []
alias: []
tags: []
---

- 27-10-2022 03:48: created

- What is shallow embedding?
	- [[shallow]] embedding methods
		- [[Matrix factorization]]
		- [[Random walk]]
- Drawbacks of it:
	- 1. No parameters are shared between nodes in the encoder (i.e. the [[encoder]] is simply an [[Embedding]] lookup based on arbitrary node ids), 
		- which is statistically inefficient, since parameter sharing can act as a powerful form of [[regularization]]
		- and it is also computationally inefficient, since it means the number of parameters in [[shallow]] embedding method necessarily grow as $O(|V|)$.
	- 2. Fails to leverage node attributes (eg: user profiles on a social network) during [[encoder|encode]], which is often highly [[informative]] with respect to node's position and role in the graph.
	- 3. [[shallow]] embedding methods are inherently [[transductive]] (i.e. they can only generate embeddings for nodes that were present during training phase.)
		- They cannot generate embeddings for previously unseen nodes unless additional rounds of optimization are preformed to optimize the embeddings for these nodes.
		- Highly problematic for evolving graphs, massive graphs that cannot be filly stored in memory, or domains that require generalizing to new graphs after training.



---
## Reference

1. 