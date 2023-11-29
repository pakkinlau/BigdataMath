- 6-10-2022: created

- Types of graph: (R1)
	- Sized m adjacency matrix and $A_{ij}=1$ if there is a link between node $i$ and $j$.
	- (V/X) directed
	- (V/X) weighted
	- (V/X) ranked
	- (V/X) typed
	- (V/X) self-edge
	- (V/X) properties that depending on the neighboring structure 

- Formalism of graph
- $V$ is the vertex set
- $A$ is the adjacency matrix (most simple would be binary)
- $X \in R^{m \times |V|}$ is a matrix of node features
- $v$: a node in $V$ 
- $N(v)$: the set of neighbors of $v$.

- Characteristics:
	- There is no fixed notion of locality or sliding window on the graph.
	- Graph is permutation [[Invariant, shift-invariant, time-invariant|invariant]]
		- What is invariant?
			- ![[Invariant, shift-invariant, time-invariant#^714cff]]
		- It should be an important assumption before GNNs.
			- If a graph is not permutation invariant, then switching the order of the graph could leads to different outputs. Which makes training become impossible.
		- Graph does not have a [[canonical]] order / ()"normal" order) of the node. Which means, if we switch the order of the graph, the adjacent matrix would look different. 
		- 

---
## Reference: 
1. [[(Course) CS224W - Machine learning with graphs (stanford)]]