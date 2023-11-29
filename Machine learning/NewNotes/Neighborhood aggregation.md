---
category: []
alias: [Neighborhood message aggregation]
tags :[]
---

- 26-10-2022 19:35: created

- What is Neighborhood aggregation?
	- The embedding of each node is updated by referring to the embedding of its neighbors.
	- Intuition: (R2)
		- Nodes aggregate information form their neighbors using neural networks
		- Network neighborhood defines a computation graph.

- Formulation: (R2)
	- $h_v^{(l)}=AGG^{(l)}(\{m_u^{(l)}, u \in N(v)\})$. $AGG(.)$ could be SUM(), Mean(), Max() aggregator. But information from node $v$ itself could get lost. 

- Neighborhood aggregation is not always helpful: (R1)
	- 1. when a node's neighbors are highly dissimilar. 
	- 2. when a node's embedding is already similar with that of its neighbors. 

![[Pasted image 20220917045314.png]]
- Fig: 2-hop neighborhood aggregation (R2)

---
## Reference

1. Paper: When Do GNNs Work: Understanding and Improving Neighborhood Aggregation https://www.ijcai.org/proceedings/2020/181
2. [[(Course) CS224W - Machine learning with graphs (stanford)]]