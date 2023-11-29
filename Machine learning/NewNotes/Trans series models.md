---
category: []
alias: []
tags: []
---

- 01-11-2022 00:44: created

- What is Trans series models?
	- Bordes et al. proposed the most representative classical translation model TransE , and led a large number of researchers into the study of Trans series models, in which the representative improved models include TransH, TransR  and TransD.  (R1)
	- Main idea
		- treating the process of finding valid triples as the translation operation of entities through relationships, define the corresponding score function, and then minimize the loss function to learn the representation of entities and relationships
		- Given a training set $S$ consisting of triples $(h,r,t)$ in the head and tail entity $h,t \in E$, $E$ is entity set, $r \in R$ , $R$ is relationship set. 
		- If the triple is true, then the sum of the vector representations of head entity and relation is close to the vector representations of the tail entity.
			- eg: in transE model, $\vec{h} + \vec{r} = \vec{t}$.
	- Difference between them
	- TransE
		- The first model
		- Simple
		- inflexible, knowledge might affected by irrelevant dimensions
		- Limits in dealing with 1-to-M, M-to-N
		- Cannot well distinguish entities with the same relationship.
	- TransH
		- Learns additional mapping vector $W_r$ for each relationship
		- 
	- TransR
	- TransD

- Extended writings:
	- [[(Table) Relation patterns of knowledge graph models]]


---
## Reference

1. [[(Paper) Chen, Z., Wang, Y., Zhao, B., Cheng, J., Zhao, X., & Duan, Z. (2020). Knowledge Graph Completion, A Review. _IEEE Access_, _8_, 192435–192456]]
2. [[(Video) Farshad's Trans series youtube video ]]