---
alias: [similar]
---

- 21-10-2022: created

- Some problematic models:
	- Some  [[Global matrix factorization methods]]: 
		- eg: `and` , `the` will have a large effect of their [[similarity]] despite conveying relatively little about their semantic relatedness. (R1)

- In machine learning, 
	- movie/users, words, images... can all be compared, using [[Embedding]]. (My writing)

- In [[graph]] [[feature learning|representation learning]], 
	- when we apply the pairwise decoder to a pair of embeddings $(z_i, z_j)$ we get a reconstruction of the similarity between $v_i$ and $v_j$ in the original graph, and the goal is optimize the [[encoder]] and [[Decoder]] mapping to minimize the error. 
		- eg, $DEC(ENC(v_i), ENC(v_j)) = DEC(z_i, z_j) \sim s_G(v_i, v_j)$
		- eg: set $s_G(v_i, v_j):=A_{i,j}$ and define nodes to have similarity of 1 if they are [[adjacent]] / linked, and 0 otherwise.
---
- Class of similarity measures:
	- [[dot product]]
	- [[Cosine product]]
	- [[Euclidean distance]]

---
## Reference

1. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]
2. [[(Paper) Representation learning on graphs -- Methods and applications]]