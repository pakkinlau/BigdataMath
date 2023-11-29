---
category: []
alias: []
tags: []
---

- 26-10-2022 22:33: created

- What are the Graph representation challenge?
	- 1. There is no straightforward way to encode the high-dimensional non-Euclidean information about graph structure into a feature vector. (R1)

![[Pasted image 20221026223423.png]]
- Fig 1: Two different views of a character-character interaction graph. (R1). The coloring for both figures were generated using different setting of the [[(library) node2vec]] embedding method

---
- 2. To extract structural information from graphs, traditional machine approaches often rely on summary graph statistics 
	- (e.g., degrees or clustering coefficients), kernel functions, or carefully engineered features to measure local neighborhood structures. 
	- However, these approaches are limited because these hand-engineered features are inflexible—i.e., they cannot [[adapt]] during the learning process—and designing these [[feature]] can be a time-consuming and expensive process.
---
	- (A) Lack of theoretical framework
		- The field lacks a consistent theoretical framework, that precisely delineate the goals of representation learning on graphs.
		- The implicit goal is to generate representations that perform well on a particular set of classification or link prediction benchmarks. But these benchmarks exacerbate the popularity of node and graph embedding techniques.
		- Moving forward as a field will require new theoretical work that more expect the models to encode this information, and what constraints should be imposed upon on these learned latent space. 
		- Theoretical foundation
			- 1. Informing consistent and meaningful benchmark task, that allow application domain experts to more effectively choose and differentiate between various approaches.
			- 2. Currently different methods are often evaluated on a variety of distinct benchmarks that emphasize various different graph properties (eg: community structures, relationship strengths between nodes, or structural roles.). However, many applications are more focused.
	- (B) Scalability
	- (C) Decoding higher-order motifs
	- (D) Model dynamic, temporal graphs
	- (E) Reasoning about large sets of candidate subgraph
	- (F) Improving interpretability


---
## Reference

1. [[(Paper) Representation learning on graphs -- Methods and applications]]