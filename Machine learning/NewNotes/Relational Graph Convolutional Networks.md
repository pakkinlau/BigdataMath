---
category: []
alias: []
tags :[]
---

- 26-10-2022 16:02: created


![[Graph Convolutional Networks]]

- What is Relational of GCN / RGCN?
	- Like, you have a tweet and a tweeter account, RGCN is handling such heterogeneous data structure. (R1)
	- RGCN extends GCNs to operate on multigraphs, where there is more than one edge type. There are many variations on GCN layers and more being added all the time. 
	- The idea of the projection matrices would put them in the same space. So that when you sum them together, it can make some semantic sense of what's going on.
	- RGCN would have more parameters than GCN because each relation type would have its own weight matrices. 
		- Regularizing the number of weight matrices
			- 1. Basis decomposition
			- 2. 
- Library:
	- Deep graph library
	- "RGCN-hetero"

![[Pasted image 20221026181234.png]]
- Fig: (R2)


![[Pasted image 20221026161027.png]]
- Example:
	- Andy follow Zack
	- Tom retweets someone's tweet
	- You have two different node types. And two relational types. 

![[Pasted image 20221026161355.png]]
- GCN doesn't make sense in the context of multiple node and edge types exists. 
	- Eg: training the node A, you can't average A-B edge and A-C edge.
	- So P-block-Q and P-follow-Q will have different weight matrix

![[Pasted image 20221026161507.png]]

- Equation of RGCN
	- 1. $\sum_{r \in R}$ indicates it is aggregating over all relational type.
	- 2. $\sum_{j \in N_i^r}$ indicates each sum is only care about the set of triple that are in the same particular type. 
	- 3. It's not $W^l$ anymore, it's a$W_r^l$. Because each relation has its own relation matrix.
	- 4. $W_0^l$ is giving the attention to the self-connection. 

---
- Scalability
	- Rapid number of parameters growth with respect to the number of relations
	- Each relation has $L$ matrices: $W_r^{(1)},  W_r^{(2)}, \dots,W_r^{(L)}$
	- The size of each $W_r^{(l)}$ is $d^{(l+1)} \times d^{(l)}$

---
## Regularization of parameters

![[Pasted image 20221026162237.png]]
- Weight decomposition (maximal regularization)
	- 1. You specify the number of unique W that you want to have for the layer with "B"
	- 2. Each of the $W_r$ is calculated by combining those components linearly.

- 
![[Pasted image 20221026162547.png]]
![[Pasted image 20221026162708.png]]
- Block diagonal decomposition
	- It takes small matrices and stacks them diagonally in a bigger matrix. 
	- The idea is, many of the parameters / values in this matrix will be zero.

---
## Reference

1. AIOverloads Youtube video: https://www.youtube.com/watch?v=wJQQFUcHO5U
2. [[(Course) CS224W - Machine learning with graphs (stanford)]]