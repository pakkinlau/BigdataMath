- 6-10-2022: created
- Node-level statistics (R1)
	- Cen be uses as features in a node classification model.
	- eg:
		- 1. Node degree: 
			- $$d_u = \sum_{v \in V} A[u,v]$$, which $\vec A$ denotes the graph adjacency matrix, and $(u,v)$ denotes the edge between $u$ and $v$.
		- 2. Node centrality
			- It measures "importance" of a node, which takes account how important a node's neighbors are.
			- Here we defines the node's centrality is proportional to the average centrality of its neighbors.
			- $$e_u = {1 \over \lambda}\sum_{v \in V} A[u,v]e_v \forall u \in V$$, where $\lambda$ is a constant. That's calculated by the standard eigenvector equation:
			- $$\lambda e = Ae$$
		- 3. Clustering coefficient
			- Clustering coefficient measures the proportion of closed triangles in a node's local neighborhood.
			- $$c_u = {|(v_1,v_2)\in E:v_1,v_2 \in N(u)|\over \begin{pmatrix} d_u \\ 2 \end{pmatrix}}$$, where $N(u)$ represent neighbor nodes of $u$ and $N(u) =\{v \in V:(u,v) \in E\}$
			- The numerator counts the number of edges between neighbors of node $u$. 
			- The denominator calculates how many pairs of nodes there are in $u$'s neighborhood. i.e.: all neighbors of vertex u are completely connected with each others. Then $c_u$ = 1.
		- 4. Graphlets


---
## Reference
1. [[(Course) CS224W - Machine learning with graphs (stanford)]]