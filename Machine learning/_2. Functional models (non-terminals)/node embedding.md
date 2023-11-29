---
alias: [Knowledge graph embedding]
---

- 28-9-2022: created

- Related: [[Knowledge graph completion]]

- Superset:
	- [[knowledge graph]]
	- [[representation]]
	- [[Embedding]]

- Subset:
	- Node embeddings
	- Edge embeddings (which doesn't exist)

- Related:
	- [[encoder]]

- What is node embedding?
	- The idea of these [[feature learning|representation learning]] is to learn a mapping that embeds nodes, or entire graphs, as points in a low-dimensional vector space $R^d$. which $d$ is an arbitrary matrix specified by the ML designer?  (R2)
	- We at all cost trying to avoid manmade [[feature]] in node/edge/graph level.
		- Q: Why? Alleviates the need to do feature engineering every single time. 
- Goal of node embedding
	- The goal is to [[optimization|optimize]] this mapping so that Summarize their graph position and the structure of their local graph neighborhood.  of the original graph. (R2)
	- In other words, we want to project nodes into a [[latent]] space, where geometric relations in this latent space correspond to relationships (edges) in the original graph or network.

- It is a [[machine learning]] [[tasks]] of: 
	- learning a low-dimensional [[representation|representation]] of a [[knowledge graph]]'s entities and relations, while preserving their [[semantics|semantic]] meaning. 
	- Leveraging their embedded representation, knowledge graphs (KGs) can be used for various applications
		- Link [[prediction]]
		- Triple [[classification]]
		- Entity recognition
		- [[Clustering]] 
		- Relation Extraction

- Node embedding: $f:u \rightarrow R^d :f(u) = z_u$
- Link embeddings: 
- Graph embeddings: $z_G = \sum_{v \in G}z_v$

- 4 aspects of the characteristics of knowledge graph embeddings (R1)
	- Representation space
		- The low-dimensional space in which the entities and relations are represented.
	- Scoring function
		- A measure of the goodness of a triple embedded representation
	- Encoding models
		- The modality in which the embedded representation of the entities and relations interact with each other.
	- Additional information
		- Any additional information coming from the knowledge graph that can enrich the embedded representation.
		- Usually, an ad hoc scoring function is integrated into the general scoring function for each additional information.
- Embedding procedure (R1)
	- 1. the embedding vectors of the entities and relations are initialized to random values.
	- 2. starting from a training set until a stop condition is reached, the algorithm continuously optimizes the embeddings.
		- Usually, the stop condition is given by the overfitting over the training set.
	- 3. For each iteration, is sampled a batch of size from the training set, and for each triple of the batch is sampled a random corrupted fact—i.e., a triple that does not represent a true fact in the knowledge graph
		- The corruption of a triple involves substituting the head or the tail (or both) of the triple with another entity that makes the fact false.
		- The original triple and the corrupted triple are added in the training batch, and then the embeddings are updated, optimizing a scoring function.
	- 4.  At the end of the algorithm, the learned [[Embedding]] should have extracted the [[semantics|semantic]] meaning from the triples and should correctly unseen true facts in the knowledge graph


---
## Reference
1. [[(Wikipedia) Knowledge graph embedding]]
2. [[(Paper) Representation learning on graphs -- Methods and applications]]


